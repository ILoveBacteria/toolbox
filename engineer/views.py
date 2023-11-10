import requests

from django.shortcuts import redirect, reverse, render
from django.views.generic import ListView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Footprint
from .forms import FileForm


class FootprintListView(LoginRequiredMixin, ListView):
    model = Footprint


class FootprintDetailView(LoginRequiredMixin, DetailView):
    model = Footprint


class FootprintExtractor(View):
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
    with open('engineer/temp.html', 'wb') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
