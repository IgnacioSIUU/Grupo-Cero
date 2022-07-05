# Generated by Django 4.0.5 on 2022-07-01 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de categoria')),
                ('nombreCategoria', models.CharField(max_length=50, verbose_name='Nombre de la categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Arte',
            fields=[
                ('idprod', models.CharField(max_length=6, primary_key=True, serialize=False, verbose_name='Idproducto')),
                ('nombre', models.CharField(max_length=20, verbose_name='Nombre del arte')),
                ('precio', models.CharField(blank=True, max_length=20, null=True, verbose_name='Precio')),
                ('tecnica', models.CharField(blank=True, max_length=20, null=True, verbose_name='Tecnica')),
                ('autor', models.CharField(blank=True, max_length=20, null=True, verbose_name='Autor')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.categoria')),
            ],
        ),
    ]
