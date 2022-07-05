from django.contrib import admin
from .models import Categoria,Arte, Contacto

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Arte)
admin.site.register(Contacto)