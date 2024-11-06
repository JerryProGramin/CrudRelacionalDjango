from django.urls import path
from .views import home, crear_categoria, crear_producto, crear_proveedor, editar_categoria, editar_producto, editar_proveedor, eliminar_categoria, eliminar_producto, eliminar_proveedor, crud_categoria, crud_producto, crud_proveedor

urlpatterns = [
    path('', home, name='home'), 

    path('producto/crud_producto/', crud_producto, name='crud_producto'),
    path('proveedor/crud_proveedor/', crud_proveedor, name='crud_proveedor'),  
    path('categoria/crud_categoria/', crud_categoria, name='crud_categoria'), 

    path('producto/editar/<int:producto_id>/', editar_producto, name='editar_producto'),
    path('proveedor/editar/<int:proveedor_id>/', editar_proveedor, name='editar_proveedor'),
    path('categoria/editar/<int:categoria_id>/', editar_categoria, name='editar_categoria'),

    path('producto/crear_producto/', crear_producto, name='crear_producto'),
    path('proveedor/crear_proveedor/', crear_proveedor, name='crear_proveedor'),
    path('categoria/crear_categoria/', crear_categoria, name='crear_categoria'),

    path('producto/eliminar/<int:producto_id>/', eliminar_producto, name='eliminar_producto'),
    path('proveedor/eliminar/<int:proveedor_id>/', eliminar_proveedor, name='eliminar_proveedor'),
    path('categoria/eliminar/<int:categoria_id>/', eliminar_categoria, name='eliminar_categoria'),
]