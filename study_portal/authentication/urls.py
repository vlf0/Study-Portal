from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('auth/<str:error>/', views.index, name='index'),
    path('logged/<str:out>/', views.profile, name='logged_out'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('registration/', views.new_user, name='new_user'),
    path('check_username/', views.check_username, name='check_username'),
]
