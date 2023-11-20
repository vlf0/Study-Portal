from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import Logging


def index(request):
    return render(request, 'index.html', {'logging': Logging()})


def authentication(request):
    username = request.POST.get('user')
    password = request.POST.get('password')
    user = authenticate(request, usename=username, password=password)
    print(user)
    print(request.user)
    if user := authenticate(usename=username, password=password):
        print(user)
        login(request, user)
        return redirect('profile', username=username)
    messages.error(request, 'Неверный логин или пароль.')
    return redirect('index')


def profile(request, username):
    return render(request, 'profile.html', {'username': username})


