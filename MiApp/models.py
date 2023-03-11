from django.db import models
from autoslug import AutoSlugField

class Categoria(models.Model):
    nombre = models.CharField(max_length=40)
    slug = AutoSlugField(populate_from='nombre')
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f'Nombre: {self.nombre}'
    
    class Meta:
         verbose_name_plural='Categoria'

class Productos(models.Model):
    codigo = models.CharField(max_length=100,primary_key=True)
    nombre = models.CharField(max_length=40)
    fechaDePublicacion = models.DateField()
    slug = AutoSlugField(populate_from='nombre')
    imagen = models.CharField(max_length=250)
    marca = models.CharField(max_length=40)
    descripcion = models.TextField(blank=True,null=True)
    precio = models.DecimalField(max_digits=15,decimal_places=3,default=0.0)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    destacado = models.BooleanField(default=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f'Nombre: {self.nombre} - Precio: {self.precio} - Fecha de Publicacion: {self.fechaDePublicacion}'
    
    class Meta:
        verbose_name_plural='Producto'

class Vendedor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    fechaDeNacimiento = models.DateField()
    correo = models.EmailField()

    def __str__(self):
        return f'Nombre: {self.nombre} - Apellido: {self.apellido} - Fecha de Nacimiento: {self.fechaDeNacimiento} - Correo Electronico: {self.correo}'