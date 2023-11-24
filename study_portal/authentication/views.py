from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import Logging, Registration
import time

# Time tracking
# t1 = time.time()
# t2 = time.time() - t1
# print(t2)


# This function works more than 0.5 s. Will attempt another build.
def index(request, **kwargs):
    if request.method == "GET":
        return render(request, 'index.html', {'logging': Logging()})
    if user := authenticate(username=request.POST.get('user'), password=request.POST.get('password')):
        login(request, user)
        if not request.user.is_staff:
            return redirect('profile', username=request.POST.get('user'))
    messages.error(request, 'Неверный логин или пароль.')
    return redirect('index', error='failed')


def profile(request, **kwargs):
    print(kwargs)
    data = {}
    if request.method == "POST":
        logout(request)
        return redirect('index')
    if kwargs:
        data = {'username': kwargs}
    return render(request, 'registration/login.html', data)


def new_user(request):
    print('new_user', request.method)
    return render(request, 'registration/registration.html', {'registration': Registration()})


def check_username(request):
    print('check_username', request.method)
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username=username).exists()
    }
    return JsonResponse(data)



