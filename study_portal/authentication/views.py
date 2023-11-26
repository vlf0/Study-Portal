from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .forms import Logging, Registration

User = get_user_model()


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
        data = {'username': kwargs['username']}
    return render(request, 'registration/login.html', data)


def new_user(request):
    if request.method == "POST":
        instance = {
                'email': request.POST.get('email'),
                'name': request.POST.get('name'),
                'password': request.POST.get('password')
                }
        user = User.objects.create_user(instance['name'], instance['email'], instance['password'])
        user.save()
        # Need to change to another redirecting
        # return redirect('profile', username=instance['name'])
    return render(request, 'registration/registration.html', {'registration': Registration()})


def check_username(request):
    print('check_username', request.method)
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username=username).exists()
    }
    return JsonResponse(data)



