from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('loginuser/', views.loginuser,name='loginuser'),
    path('register/', views.register,name='register'),
    path('dash/', views.dash,name='dash'),
    path('allusers/', views.allusers,name='allusers'),
    path('logoutuser/', views.logoutuser,name='logoutuser'),
    
]