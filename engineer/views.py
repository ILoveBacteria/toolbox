import os

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View

from engineer.forms import FileForm
from engineer.models import Footprint
from toolbox.settings import env
from toolbox.settings.base import MEDIA_ROOT


from django.http import JsonResponse
from django.db.models import F, ExpressionWrapper, FloatField, Min, Q
import random

from engineer.models import Vocabulary, UserProfile
from datetime import date, timedelta


from django.core.paginator import Paginator
from engineer.forms import VocabForm


def edit_vocab_view(request, vocab_id):
    vocab = Vocabulary.objects.get(id=vocab_id)
    if request.method == 'POST':
        form = VocabForm(request.POST, instance=vocab)
        if form.is_valid():
            form.save()
            return redirect('vocab_list')
    else:
        form = VocabForm(instance=vocab)
    return render(request, 'engineer/edit_vocab.html', {'form': form})


def delete_vocab_view(request, vocab_id):
    vocab = Vocabulary.objects.get(id=vocab_id)
    if request.method == 'POST':
        vocab.delete()
        return redirect('vocab_list')
    return render(request, 'engineer/confirm_delete.html', {'vocab': vocab})


def add_vocab_view(request):
    if request.method == 'POST':
        form = VocabForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vocab_list')
    else:
        form = VocabForm()
    return render(request, 'engineer/add_vocab.html', {'form': form})


def vocab_list_view(request):
    search_query = request.GET.get('q', '')
    vocabs = Vocabulary.objects.all()
    if search_query:
        vocabs = vocabs.filter(Q(word__icontains=search_query))

    paginator = Paginator(vocabs.order_by('id'), 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'engineer/vocab_list.html', {
        'page_obj': page_obj,
        'search_query': search_query
    })


def update_vocab_view(request):
    if request.method == 'POST':
        vocab_id = request.POST.get('id')
        action = request.POST.get('action')
        vocab = Vocabulary.objects.get(id=vocab_id)
        vocab.seen += 1
        if action == "know":
            vocab.know += 1
        vocab.save()
        
        # We need to refresh from DB to get the correct know_rate property
        vocab.refresh_from_db()

        return JsonResponse({
            "example": vocab.example,
            "translation": vocab.translation,
            "seen": vocab.seen,
            "know": vocab.know,
            "know_rate": vocab.know_rate,
        })


def vocab_view(request):
    """
    Selects and displays a vocabulary word for the user to review.

    This view implements a tiered selection strategy to choose a word:
    1.  **New Words (40% chance):** Words the user has never seen (`seen == 0`).
    2.  **Struggling Words (50% chance):** Words with a know-rate of less than 60%.
        These are words that need the most practice.
    3.  **Review Words (10% chance):** Words the user knows well (know-rate >= 60%).
        These are shown occasionally to reinforce memory.

    This approach avoids the repetition of showing the same difficult words too often
    and ensures a healthy mix of new, challenging, and known vocabulary.
    """
    # Get or create the UserProfile
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    # Update streak count
    user_profile.update_streak()
    user_profile.refresh_from_db() # Ensure we have the latest streak value

    # --- New Word Selection Logic ---

    # 1. Define the word tiers using database queries for efficiency.
    new_words = Vocabulary.objects.filter(seen=0)

    # Annotate existing words with their know_ratio to filter them into tiers.
    annotated_words = Vocabulary.objects.filter(seen__gt=0).annotate(
        know_ratio=ExpressionWrapper(
            F("know") * 1.0 / F("seen"),
            output_field=FloatField()
        )
    )
    struggling_words = annotated_words.filter(know_ratio__lt=0.6)
    review_words = annotated_words.filter(know_ratio__gte=0.6)

    # 2. Decide which tier to pick a word from.
    word_pool = None
    roll = random.random()  # Get a random float between 0.0 and 1.0

    if new_words.exists() and roll < 0.4:
        # 40% chance to pick from new words
        word_pool = new_words
    elif struggling_words.exists() and roll < 0.9:
        # 50% chance for struggling words (0.4 to 0.9 range)
        word_pool = struggling_words
    elif review_words.exists():
        # 10% chance for review words (or if other pools were empty)
        word_pool = review_words
    else:
        # Fallback: if the chosen pool was empty but others are not, pick from any available pool.
        available_pools = [pool for pool in [new_words, struggling_words, review_words] if pool.exists()]
        if available_pools:
            word_pool = random.choice(available_pools)

    # 3. Select a random word from the chosen tier.
    vocab = None
    if word_pool:
        count = word_pool.count()
        if count > 0:
            random_index = random.randint(0, count - 1)
            vocab = word_pool[random_index]

    return render(request, "engineer/vocab.html", {
        "vocab": vocab,
        "user_profile": user_profile
    })


def update_vocab(request):
    if request.method == "POST":
        word_id = request.POST.get("id")
        action = request.POST.get("action")
        try:
            vocab = Vocabulary.objects.get(id=word_id)
        except Vocabulary.DoesNotExist:
            return JsonResponse({"error": "Word not found"}, status=404)

        # Update vocab atomically
        vocab.seen = F("seen") + 1
        if action == "know":
            vocab.know = F("know") + 1
        vocab.save(update_fields=["seen", "know"])
        vocab.refresh_from_db()

        # Update user profile
        user_profile = UserProfile.objects.get(user=request.user)
        if action == "know":
            user_profile.total_known = F("total_known") + 1
            user_profile.save(update_fields=["total_known"])

        if action == "dont_know":
            return JsonResponse({"translation": vocab.translation})

        return JsonResponse({"success": True})

    return JsonResponse({"error": "Invalid request"}, status=400)


class FootprintListView(LoginRequiredMixin, ListView):
    model = Footprint


class FootprintDetailView(LoginRequiredMixin, DetailView):
    model = Footprint


class FootprintExtractor(LoginRequiredMixin, View):
    def get(self, request):
        form = FileForm()
        return render(request, template_name='engineer/footprint_extractor.html',
                      context={'title': 'Footprint Extractor', 'form': form})

    def post(self, request):
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            handle_uploaded_file(file)
        return render(request, template_name='engineer/footprint_extractor.html',
                      context={'title': 'Footprint Extractor', 'form': form})


def handle_uploaded_file(f):
    os.makedirs(MEDIA_ROOT, exist_ok=True)
    # Use os.path.join for cross-platform compatibility
    with open(os.path.join(MEDIA_ROOT, 'temp.html'), 'wb') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
