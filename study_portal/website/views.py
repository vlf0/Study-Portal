from django.shortcuts import render, redirect
from .forms import Logging


def index(request):
    context = {'logging': Logging}
    return render(request, 'index.html', context)
