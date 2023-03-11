from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('about', views.about, name='About'),
    path('quieroVender', views.quieroVender, name='QuieroVender'),
    path('register', views.register, name='Register'),
    path ('login', LoginView.as_view(template_name='MiApp/login.html'), name='Login'),
    path ('logout', LogoutView.as_view(template_name='MiApp/logout.html'), name='Logout'),
]