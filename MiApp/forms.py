from django import forms
from .models import Tecnologia, Deportes, Vehiculos, Supermercado, Hogar, RopaEstetica
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


class TecnologiaFormulario(forms.ModelForm):
    class Meta:
        model = Tecnologia
        fields = '__all__'
