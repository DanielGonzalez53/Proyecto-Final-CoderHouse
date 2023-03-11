from django.contrib import admin
from .models import Vendedor, Productos, Categoria

# Register your models here.

admin.site.register(Vendedor)
admin.site.register(Productos)
admin.site.register(Categoria)