from django.db import models

class Tecnologia(models.Model):
    nombre = models.CharField(max_length=40)
    marca = models.CharField(max_length=40)
    tipo = models.CharField(max_length=40)
    imagen = models.ImageField()
    descripcion = models.TextField(max_length=200)
    precio = models.DecimalField(max_digits=15,decimal_places=3,default=0.0)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f'Nombre: {self.nombre} - Tipo: {self.tipo} - {self.precio}'

class Deportes(models.Model):
    nombre = models.CharField(max_length=40)
    marca = models.CharField(max_length=40)
    tipo = models.CharField(max_length=40)
    imagen = models.ImageField()
    descripcion = models.TextField(max_length=200)
    precio = models.DecimalField(max_digits=15,decimal_places=3,default=0.0)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f'Nombre: {self.nombre} - Tipo: {self.tipo} - {self.precio}'

class Vehiculos(models.Model):
    nombre = models.CharField(max_length=40)
    marca = models.CharField(max_length=40)
    tipo = models.CharField(max_length=40)
    imagen = models.ImageField()
    descripcion = models.TextField(max_length=200)
    precio = models.DecimalField(max_digits=15,decimal_places=3,default=0.0)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f'Nombre: {self.nombre} - Tipo: {self.tipo} - {self.precio}'

class Supermercado(models.Model):
    nombre = models.CharField(max_length=40)
    marca = models.CharField(max_length=40)
    tipo = models.CharField(max_length=40)
    imagen = models.ImageField()
    descripcion = models.TextField(max_length=200)
    fecha_vencimiento = models.DateField()
    precio = models.DecimalField(max_digits=15,decimal_places=3,default=0.0)
    activo = models.BooleanField(default=True)
    def __str__(self):
        return f'Nombre: {self.nombre} - Tipo: {self.tipo} - {self.precio}'

class Hogar(models.Model):
    nombre = models.CharField(max_length=40)
    marca = models.CharField(max_length=40)
    tipo = models.CharField(max_length=40)
    imagen = models.ImageField()
    descripcion = models.TextField(max_length=200)
    precio = models.DecimalField(max_digits=15,decimal_places=3,default=0.0)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f'Nombre: {self.nombre} - Tipo: {self.tipo} - {self.precio}'

class RopaEstetica(models.Model):
    nombre = models.CharField(max_length=40)
    marca = models.CharField(max_length=40)
    tipo = models.CharField(max_length=40)
    imagen = models.ImageField()
    descripcion = models.TextField(max_length=200)
    precio = models.DecimalField(max_digits=15,decimal_places=3,default=0.0)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f'Nombre: {self.nombre} - Tipo: {self.tipo} - {self.precio}'