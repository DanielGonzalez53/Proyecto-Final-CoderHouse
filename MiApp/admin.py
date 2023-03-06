from django.contrib import admin
from .models import Vendedor, Cliente, Producto

# Register your models here.

admin.site.register(Vendedor)
admin.site.register(Cliente)
admin.site.register(Producto)