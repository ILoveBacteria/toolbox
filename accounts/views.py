from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views import View

from .forms import LoginForm


class Login(View):
    def post(self):
        form = LoginForm(self.request.POST)
        if form.is_valid():
            user = authenticate(self.request, username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user is not None:
                login(self.request, user)
                if (next_view := self.request.GET['next']) is not None:
                    return redirect(next_view)
                return redirect('/')
            form.add_error(None, 'Username or password is incorrect!')
        return render(self.request, 'accounts/login.html', context={'form': form, 'title': 'Login'}, status=400)

    def get(self):
        form = LoginForm()
        return render(self.request, 'accounts/login.html', context={'form': form, 'title': 'Login'})
