from django.shortcuts import redirect, reverse
from django.views.generic import ListView, DetailView, View

from .models import Footprint


class FootprintListView(ListView):
    model = Footprint


class FootprintDetailView(DetailView):
    model = Footprint


class FootprintRefresh(View):
    def post(self, request):
        return redirect(reverse('footprint_list'))
