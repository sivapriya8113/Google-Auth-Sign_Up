from django.contrib import admin
from django.urls import path, include

from myapp import views

urlpatterns = [
    path('',views.reg,name='register'),
    path('login/', views.login),
    path('home/', views.home),

]
