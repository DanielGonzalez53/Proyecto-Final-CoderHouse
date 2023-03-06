from django.db import models

class Vendedor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    fechaDeNacimiento = models.DateField()
    correo = models.EmailField()

    def __str__(self):
        return f'Nombre: {self.nombre} - Apellido: {self.apellido} - Fecha de Nacimiento: {self.fechaDeNacimiento} - Correo Electronico: {self.correo}'

class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    fechaDeNacimiento = models.DateField()
    correo = models.EmailField()

    def __str__(self):
        return f'Nombre: {self.nombre} - Apellido: {self.apellido} - Fecha de Nacimiento: {self.fechaDeNacimiento} - Correo Electronico: {self.correo}'

opciones_producto = [
    [0, "Tecnologia"],
    [0, "Deportes"],
    [0, "Vehiculos"],
    [0, "Supermercado"],
    [0, "Hogar"],
    [0, "Ropa y Accesorios"]
]

class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.PositiveIntegerField(default=0)
    fechaDePublicacion = models.DateField()
    tipo_producto = models.IntegerField(choices=opciones_producto)
    estado = models.BooleanField(default=False)

    def __str__(self):
        return f'Nombre: {self.nombre} - Precio: {self.precio} - Fecha de Publicacion: {self.fechaDePublicacion} - Caracteristicas: {self.tipo_producto} - Vendido: {self.estado}'