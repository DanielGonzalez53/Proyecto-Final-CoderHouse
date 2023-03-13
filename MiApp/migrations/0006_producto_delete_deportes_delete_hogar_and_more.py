# Generated by Django 4.1.6 on 2023-03-12 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MiApp', '0005_deportes_hogar_ropaestetica_supermercado_tecnologia_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[[0, 'Tecnologia'], [1, 'Deportes'], [2, 'Vehiculos'], [3, 'Super Mecardo'], [4, 'Hogar'], [5, 'Ropa & Estetica']], default='Opcion', max_length=40)),
                ('nombre', models.CharField(max_length=40)),
                ('marca', models.CharField(max_length=40)),
                ('imagen', models.ImageField(upload_to='')),
                ('descripcion', models.TextField(max_length=200)),
                ('precio', models.DecimalField(decimal_places=3, default=0.0, max_digits=15)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Deportes',
        ),
        migrations.DeleteModel(
            name='Hogar',
        ),
        migrations.DeleteModel(
            name='RopaEstetica',
        ),
        migrations.DeleteModel(
            name='Supermercado',
        ),
        migrations.DeleteModel(
            name='Tecnologia',
        ),
        migrations.DeleteModel(
            name='Vehiculos',
        ),
    ]