from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('allusers/sendinterest/<int:id>/', views.sendinterest,name='sendinterest'),
    path('myrequests/', views.myrequests,name='myrequests'),



]