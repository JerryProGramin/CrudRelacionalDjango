from django import forms 
from .models import Categoria, Producto, Proveedor

class CategoriaForm(forms.ModelForm):
    class Meta:
        model=Categoria
        fields=[
            'nombre',
            'descripcion',
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre de la categoria'}),
            'descripcion': forms.TextInput(attrs={'placeholder': 'Descripcion de la categoria'}),
        }

class ProveedorForm(forms.ModelForm):
    class Meta:
        model=Proveedor
        fields=[
            'nombre',
            'direccion',
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre del proveedor'}),
            'direccion': forms.TextInput(attrs={'placeholder': 'Direccion de la categoria'}),
        }

class ProductoForm(forms.ModelForm):
    class Meta:
        model=Producto
        fields=[
            'nombre',
            'descripcion',
            'proveedor',
            'categoria',
            'precio',
            'stock',
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre del producto'}),
            'descripcion': forms.TextInput(attrs={'placeholder': 'Descripcion del producto'}),
            'proveedor': forms.Select(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={
                'placeholder': 'Precio del producto', 
                'step': '0.01',   
                'min': '0',       
            }),
            'stock': forms.NumberInput(attrs={
                'placeholder': 'Stock del producto', 
                'min': '0',       
                'step': '1',     
            }),
        }