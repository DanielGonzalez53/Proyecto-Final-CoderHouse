from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('about', views.about, name='About'),
    path('quieroVender', views.ProductoCreacion.as_view(), name='QuieroVender'),
    path('register', views.register, name='Register'),
    path('login', LoginView.as_view(template_name='MiApp/login.html'), name='Login'),
    path('logout', LogoutView.as_view(template_name='MiApp/logout.html'), name='Logout'),
    path('quieroVender/list', views.ProductoList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.ProductoDetalle.as_view(), name='Detail'),
    #path(r'^nuevo$', views.ProductoCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.ProductoUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.ProductoDelete.as_view(), name='Delete'),
]