from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('acercaDeMi', views.acercaDeMi, name='AcercaDeMi'),
]