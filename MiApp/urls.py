from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('about', views.about, name='About'),
    path('quieroVender', views.quieroVender, name='QuieroVender')
]