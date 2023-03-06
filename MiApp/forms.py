from django import forms
from .models import Vendedor, Cliente, Producto
#from django.contrib.auth.models import User

class VendedorFormulario(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields = '__all__'

class ClienteFormulario(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class ProductoFormulario(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'