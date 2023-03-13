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
    path(r'^editar/(?P<pk>\d+)$', views.ProductoUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.ProductoDelete.as_view(), name='Delete'),

    path('tecnologiaLista/', views.TecnologiaLista.as_view(), name='tecnologias'),
    path('tecnologiaDetalle/<int:pk>/', views.TecnologiaDetalle.as_view(), name='tecnologia'),
    path('tecnologiaEdicion/<int:pk>/', views.TecnologiaUpdate.as_view(), name='editar_tecnologia'),
    path('tecnologiaBorrado/<int:pk>/', views.TecnologiaDelete.as_view(), name='eliminar_tecnologia'),
]