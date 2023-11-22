from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import Logging


def index(request, **kwargs):
    if request.method == "GET":
        return render(request, 'index.html', {'logging': Logging()})
    if user := authenticate(username=request.POST.get('user'), password=request.POST.get('password')):
        login(request, user)
        if not request.user.is_staff:
            return redirect('profile', username=request.POST.get('user'))
    messages.error(request, 'Неверный логин или пароль.')
    return redirect('index', error='log-in_error')


def profile(request, username):
    return render(request, 'registration/login.html', {'username': username})


