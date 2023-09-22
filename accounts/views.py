from django.contrib.auth import login, logout as dj_logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.views.generic import FormView


class Login(FormView):
    form_class = AuthenticationForm
    template_name = 'form.html'
    success_url = '/'

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)


def logout(request):
    dj_logout(request)
    return redirect('/')
