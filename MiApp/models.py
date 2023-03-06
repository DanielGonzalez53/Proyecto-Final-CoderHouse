from django.db import models

class Vendedor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    fechaDeNacimiento = models.DateField()
    correo = models.EmailField()
    tipoDeArticulo = models.CharField(max_length=40)

    def __str__(self):
        return f'Nombre: {self.nombre} - Apellido: {self.apellido} - Fecha de Nacimiento: {self.fechaDeNacimiento} - Correo Electronico: {self.correo} - Tipo de Articulo: {self.tipoDeArticulo}'

class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    fechaDeNacimiento = models.DateField()
    correo = models.EmailField()

    def __str__(self):
        return f'Nombre: {self.nombre} - Apellido: {self.apellido} - Fecha de Nacimiento: {self.fechaDeNacimiento} - Correo Electronico: {self.correo}'
    
class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.IntegerField(default=0)
    fechaDePublicacion = models.DateField()
    caracteristicas = models.CharField(max_length=40)
    estado = models.BooleanField(default=False)

    def __str__(self):
        return f'Nombre: {self.nombre} - Precio: {self.precio} - Fecha de Publicacion: {self.fechaDePublicacion} - Caracteristicas: {self.caracteristicas} - Vendido: {self.estado}'