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
        return JsonResponse({
            "example": vocab.example,
            "translation": vocab.translation,
            "seen": vocab.seen,
            "know": vocab.know,
            "know_rate": vocab.know_rate,
        })


def vocab_view(request):
    # Get or create the UserProfile
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    # Update streak count
    user_profile.update_streak()

    # Annotate vocab with knowledge ratio
    annotated = Vocabulary.objects.annotate(
        know_ratio=ExpressionWrapper(F("know") * 1.0 / F("seen"), output_field=FloatField())
    )
    
    min_ratio = annotated.aggregate(min_ratio=Min("know_ratio"))["min_ratio"]
    candidates = annotated.filter(know_ratio=min_ratio)

    vocab = random.choice(list(candidates)) if candidates else None

    return render(request, "engineer/vocab.html", {
        "vocab": vocab,
        "user_profile": user_profile
    })

def update_vocab(request):
    if request.method == "POST":
        word_id = request.POST.get("id")
        action = request.POST.get("action")
        vocab = Vocabulary.objects.get(id=word_id)

        # Update vocab
        vocab.seen = F("seen") + 1
        if action == "know":
            vocab.know = F("know") + 1

        vocab.save(update_fields=["seen", "know"])
        vocab.refresh_from_db()

        # Update user profile
        user_profile = UserProfile.objects.get(user=request.user)
        if action == "know":
            user_profile.total_known += 1
        user_profile.save()

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
    with open(MEDIA_ROOT / 'temp.html', 'wb') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
