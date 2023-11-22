from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:error>/', views.index, name='index'),
    path('profile/<str:username>/', views.profile, name='profile'),
]
