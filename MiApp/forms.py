from django import forms
from .models import Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Correo Electronico')
    password1 =forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 =forms.CharField(label='Confirma contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:'' for k in fields}

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['tipo', 'nombre', 'marca', 'imagen', 'descripcion', 'precio', 'activo']
