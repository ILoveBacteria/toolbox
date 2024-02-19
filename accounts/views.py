from django.contrib.auth import login, logout as dj_logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect, reverse
from django.urls import reverse_lazy
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.generic import FormView

from toolbox.settings.base import ALLOWED_HOSTS


class Login(FormView):
    form_class = AuthenticationForm
    template_name = 'form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        login(self.request, form.get_user())
        to = self.request.GET.get('next') or self.success_url
        if url_has_allowed_host_and_scheme(url=to, allowed_hosts=ALLOWED_HOSTS):
            return redirect(to)
        return HttpResponseBadRequest()


def logout(request):
    dj_logout(request)
    return redirect(reverse('home'))
