from dataclasses import dataclass
from re import M
from django.shortcuts import render,redirect
from .models import *
import os 
from django.conf import settings
from django.http import HttpResponse
import json
# Create your views here.


def cargarIndex(request):
    productos = Producto.objects.all()

    plantas = Producto.objects.filter(categoria = 1, cantidad__gt=0)
    maceteros = Producto.objects.filter(categoria = 2, cantidad__gt=0)
    flores = Producto.objects.filter(categoria = 3, cantidad__gt=0)
    accesorios = Producto.objects.filter(categoria = 4, cantidad__gt=0)

    return render(request,"index.html",{"plantas":plantas, "maceteros":maceteros,"flores":flores,"accesorios":accesorios,})

def AgregarProducto(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    return render(request,"AgregarProducto.html", {"ALLcategorias":categorias, "ALLproductos":productos})


def SubirAgregarProducto(req):
    print("ELEMENTOS EN LA REQUEST ", req.POST)
    m_id = req.POST['txtID']
    m_nombre = req.POST['txtNombre']
    m_valor = req.POST['txtValor']
    m_cantidad = req.POST['txtCantidad']
    m_descripcion = req.POST['txtDescripcion']
    m_foto = req.FILES['txtImagen']
    m_categoria = Categoria.objects.get(id_categoria = req.POST['SelectCategoria'])

    Producto.objects.create(
        id_objeto = m_id,
        nombre = m_nombre,
        valor = m_valor,
        cantidad = m_cantidad,
        descripcion = m_descripcion,
        foto = m_foto,
        categoria = m_categoria
    )

    return redirect('AgregarProducto/')







