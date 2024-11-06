from django.shortcuts import render, redirect
from .forms import CategoriaForm, ProductoForm, ProveedorForm
from .models import Categoria, Producto, Proveedor
from django.db.models import ProtectedError
from django.urls import reverse
from django.shortcuts import get_object_or_404

# Create your views here.

def home(request):
    return render(request, 'index.html')

def crud_producto(request):
    producto = Producto.objects.all() 
    return render(request, 'crud_producto.html', {'productos': producto}) 

def crud_proveedor(request):
    proveedor = Proveedor.objects.all() 
    return render(request, 'crud_proveedor.html', {'proveedor': proveedor}) 

def crud_categoria(request):
    categorias = Categoria.objects.all() 
    return render(request, 'crud_categoria.html', {'categorias': categorias}) 


def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('crud_producto') 
    else:
        form = ProductoForm()  

    return render(request, 'crear_producto.html', {'form': form})

def crear_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('crud_proveedor') 
    else:
        form = ProveedorForm()  

    return render(request, 'crear_proveedor.html', {'form': form})

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('crud_categoria') 
    else:
        form = CategoriaForm()

    return render(request, 'crear_categoria.html', {'form': form})


def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto.delete() 
    return redirect('crud_producto') 

def eliminar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    proveedor.delete() 
    return redirect('crud_proveedor')  

def eliminar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    try:
        categoria.delete()
        return redirect('crud_categoria')  

    except ProtectedError:
        return redirect('crud_categoria') 


def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('crud_producto')
    else:
        form = ProductoForm(instance=producto)

    return render(request, 'editar_producto.html', {'form': form, 'producto': producto})

def editar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('crud_categoria')
    else:
        form = CategoriaForm(instance=categoria)

    return render(request, 'editar_categoria.html', {'form': form, 'categoria': categoria})

def editar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('crud_proveedor')
    else:
        form = ProveedorForm(instance=proveedor)

    return render(request, 'editar_proveedor.html', {'form': form, 'proveedor': proveedor})
