from django.urls import path

from estudiantes.views import (
    listar_clientes, listar_productos, listar_recetas,
    crear_receta, buscar_receta, crear_cliente, buscar_cliente, crear_producto, buscar_productos
)


urlpatterns = [
    path('clientes/', listar_clientes, name="listar_clientes"),
    path('productos/', listar_productos, name="listar_productos"),
    path('recetas/', listar_recetas, name="listar_recetas"),
    path('crear-receta/', crear_receta, name="crear_receta"),
    path('buscar-recetas/', buscar_receta, name="buscar_recetas"),
    path('crear-cliente/', crear_cliente, name="crear_cliente"),
    path('buscar-clientes/', buscar_cliente, name="buscar_clientes"),
    path('crear-producto/', crear_producto, name="crear_producto"),
    path('buscar-producto/', buscar_productos, name="buscar_productos"),
]