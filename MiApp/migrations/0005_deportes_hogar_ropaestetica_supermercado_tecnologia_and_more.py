# Generated by Django 4.1.6 on 2023-03-12 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MiApp', '0004_categoria_productos_delete_cliente_delete_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deportes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('marca', models.CharField(max_length=40)),
                ('tipo', models.CharField(max_length=40)),
                ('imagen', models.ImageField(upload_to='')),
                ('descripcion', models.TextField(max_length=200)),
                ('precio', models.DecimalField(decimal_places=3, default=0.0, max_digits=15)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hogar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('marca', models.CharField(max_length=40)),
                ('tipo', models.CharField(max_length=40)),
                ('imagen', models.ImageField(upload_to='')),
                ('descripcion', models.TextField(max_length=200)),
                ('precio', models.DecimalField(decimal_places=3, default=0.0, max_digits=15)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='RopaEstetica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('marca', models.CharField(max_length=40)),
                ('tipo', models.CharField(max_length=40)),
                ('imagen', models.ImageField(upload_to='')),
                ('descripcion', models.TextField(max_length=200)),
                ('precio', models.DecimalField(decimal_places=3, default=0.0, max_digits=15)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Supermercado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('marca', models.CharField(max_length=40)),
                ('tipo', models.CharField(max_length=40)),
                ('imagen', models.ImageField(upload_to='')),
                ('descripcion', models.TextField(max_length=200)),
                ('fecha_vencimiento', models.DateField()),
                ('precio', models.DecimalField(decimal_places=3, default=0.0, max_digits=15)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tecnologia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('marca', models.CharField(max_length=40)),
                ('tipo', models.CharField(max_length=40)),
                ('imagen', models.ImageField(upload_to='')),
                ('descripcion', models.TextField(max_length=200)),
                ('precio', models.DecimalField(decimal_places=3, default=0.0, max_digits=15)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('marca', models.CharField(max_length=40)),
                ('tipo', models.CharField(max_length=40)),
                ('imagen', models.ImageField(upload_to='')),
                ('descripcion', models.TextField(max_length=200)),
                ('precio', models.DecimalField(decimal_places=3, default=0.0, max_digits=15)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='productos',
            name='categoria',
        ),
        migrations.DeleteModel(
            name='Vendedor',
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.DeleteModel(
            name='Productos',
        ),
    ]
