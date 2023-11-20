from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('authentication/', views.authentication, name='authentication'),
    path('profile/<str:user>/<str:password>', views.profile, name='profile'),
]
