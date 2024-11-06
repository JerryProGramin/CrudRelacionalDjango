from django.db import models

# Create your models here.

class Categoria(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.nombre

class Proveedor(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nombre

class Producto(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=150)
    proveedor=models.ForeignKey(Proveedor,on_delete=models.CASCADE, editable=True)
    categoria=models.ForeignKey(Categoria,on_delete=models.PROTECT, editable=True)
    precio=models.DecimalField(max_digits=10, decimal_places=2)
    stock=models.IntegerField()

    def __str__(self) -> str:
        return self.nombre