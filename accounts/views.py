from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views import View

from .forms import LoginForm


class Login(View):
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                if 'next' in request.GET:
                    return redirect(request.GET['next'])
                return redirect('/')
            form.add_error(None, 'Username or password is incorrect!')
        return render(request, 'form.html', context={'form': form, 'title': 'Login', 'submit': 'Login'}, status=400)

    def get(self, request):
        form = LoginForm()
        return render(request, 'form.html', context={'form': form, 'title': 'Login', 'submit': 'Login'})
