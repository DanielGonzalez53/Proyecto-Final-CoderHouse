# Generated by Django 4.1.6 on 2023-02-28 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('fechaDeNacimiento', models.DateField()),
                ('correo', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('precio', models.IntegerField(default=0)),
                ('fechaDePublicacion', models.DateField()),
                ('caracteristicas', models.CharField(max_length=40)),
                ('estado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('fechaDeNacimiento', models.DateField()),
                ('correo', models.EmailField(max_length=254)),
                ('tipoDeArticulo', models.CharField(max_length=40)),
            ],
        ),
    ]
