from django.db import models

productoOpcion = [
    ['Tecnologia', 'Tecnologia'],
    ['Deportes', 'Deportes'],
    ['Vehiculos', 'Vehiculos'],
    ['SuperMercado', 'SuperMercardo'],
    ['Hogar', 'Hogar'],
    ['RopaEstetica', 'RopaEstetica']
]

class Producto(models.Model):
    tipo = models.CharField(max_length=40, choices=productoOpcion, default='Opcion')
    nombre = models.CharField(max_length=40)
    marca = models.CharField(max_length=40)
    imagen = models.ImageField(null=False, blank=False, upload_to="imagenes/")
    descripcion = models.TextField(max_length=1000)
    precio = models.DecimalField(max_digits=15,decimal_places=3,default=0.0)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f'Nombre: {self.nombre} - Tipo: {self.tipo} - Precio: {self.precio}'