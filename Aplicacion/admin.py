from django.contrib import admin
from .models import Categoria, Producto, Proveedor

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Proveedor)
admin.site.register(Producto)
