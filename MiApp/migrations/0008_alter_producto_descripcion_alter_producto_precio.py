# Generated by Django 4.1.6 on 2023-03-13 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MiApp', '0007_alter_producto_imagen_alter_producto_precio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=15),
        ),
    ]
