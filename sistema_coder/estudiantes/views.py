from datetime import datetime

from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse

from estudiantes.models import Cliente, Producto, Receta
from estudiantes.forms import RecetaFormulario, ProductoFormulario, ClienteFormulario


def inicio(request):
    return render(
        request=request,
        template_name='estudiantes/inicio.html',
    )


def listar_clientes(request):

    contexto = {
        'clientes': Cliente.objects.all()
    }
    return render(
        request=request,
        template_name='estudiantes/lista_clientes.html',
        context=contexto,
    )

def crear_cliente(request):
    if request.method == "POST":
        formulario = ClienteFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            Clientes = Cliente(nombre=data['nombre'], apellido=data['apellido'])
            Clientes.save()
            url_exitosa = reverse('listar_clientes')
            return redirect(url_exitosa)
    else:  # GET
        formulario = ClienteFormulario()
    return render(
        request=request,
        template_name='estudiantes/formulario_cliente.html',
        context={'formulario': formulario},
    )

def buscar_cliente(request):
    if request.method == "POST":
        data = request.POST
        clientes = Cliente.objects.filter(
            Q(nombre__contains=data['busqueda']) | Q(apellido__contains=data['busqueda'])
        )
        contexto = {
            'cliente': clientes
        }
        return render(
            request=request,
            template_name='estudiantes/lista_clientes.html',
            context=contexto,
        )

def listar_productos(request):
    contexto = {
        'productos': Producto.objects.all()
    }
    return render(
        request=request,
        template_name='estudiantes/lista_productos.html',
        context=contexto,
    )

def crear_producto(request):
    if request.method == "POST":
        formulario = ProductoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            Productos = Producto(nombre=data['nombre'], precio=data['precio'])
            Productos.save()
            url_exitosa = reverse('listar_productos')
            return redirect(url_exitosa)
    else:  # GET
        formulario = ProductoFormulario()
    return render(
        request=request,
        template_name='estudiantes/formulario_producto.html',
        context={'formulario': formulario},
    )

def buscar_productos(request):
    if request.method == "POST":
        data = request.POST
        productos = Producto.objects.filter(
            Q(nombre__contains=data['busqueda'])
        )
        contexto = {
            'producto': productos
        }
        return render(
            request=request,
            template_name='estudiantes/lista_productos.html',
            context=contexto,
        )

def listar_recetas(request):
    contexto = {
        'Recetas': Receta.objects.all()
    }
    return render(
        request=request,
        template_name='estudiantes/lista_recetas.html',
        context=contexto,
    )

def crear_receta(request):
    if request.method == "POST":
        formulario = RecetaFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            Recetas = Receta(nombre=data['nombre'], bio=data['receta'])
            Recetas.save()
            url_exitosa = reverse('listar_resetas')
            return redirect(url_exitosa)
    else:  # GET
        formulario = RecetaFormulario()
    return render(
        request=request,
        template_name='estudiantes/formulario_receta.html',
        context={'formulario': formulario},
    )

def buscar_receta(request):
    if request.method == "POST":
        data = request.POST
        recetas = Receta.objects.filter(
            Q(nombre__contains=data['busqueda']) | Q(bio__icontains=data['busqueda'])
        )
        contexto = {
            'recetas': recetas
        }
        return render(
            request=request,
            template_name='estudiantes/lista_recetas.html',
            context=contexto,
        )