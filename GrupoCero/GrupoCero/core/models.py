from ast import AugStore
from distutils.command.upload import upload
from django.db import models

# Create your models here.

# Modelo para Categorias
class Categoria(models.Model):
  idCategoria = models.IntegerField(primary_key = True, verbose_name = 'Id de categoria')
  nombreCategoria = models.CharField(max_length = 50, verbose_name = 'Nombre de la categoria')

  def __str__(self):
    return self.nombreCategoria

# Modelo para Arte
class Arte(models.Model):
  idprod = models.CharField(max_length = 6, primary_key = True, verbose_name = 'Idproducto')
  nombre = models.CharField(max_length = 20, verbose_name = 'Nombredelarte')
  precio = models.CharField (max_length = 20, null = True, blank = True, verbose_name = 'Precio')
  tecnica = models.CharField (max_length = 20, null = True, blank = True, verbose_name = 'Tecnica')
  autor = models.CharField (max_length = 20, null = True, blank = True, verbose_name = 'Autor')
  categoria = models.ForeignKey(Categoria, on_delete = models.PROTECT)
  estado = models.IntegerField()

  def __str__(self):
    return self.idprod

opciones_estado = [
    [0, "nueva"],
    [1, "aprobada"],
    [2, "rechazada"]
]

opciones_contacto = [
    [0, "consulta"],
    [1, "reclamo"],
    [2, "sugerencia"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=40)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_contacto)
    mensaje = models.TextField()
    
    def __str__(self):
     return self.nombre
