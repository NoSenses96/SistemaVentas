from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
from .models import Venta
from .models import Categoria
from datetime import datetime


def inicio(request):
    return render(request, 'ventas/inicio.html')


def reporte(request):
    ventas = Venta.objects.all()
    context = {
        'ventas': ventas,
    }
    return render(request, 'ventas/reporte.html', context)


def venta(request):
    categorias = Categoria.objects.all()
    context = {
        'categorias': categorias,
    }
    return render(request, 'ventas/venta.html', context)


def registrar(request):
    date = datetime.now()
    venta = Venta()
    categorias = Categoria.objects.all()
    venta.monto = request.POST['monto']
    venta.categoria = Categoria(request.POST['categoria'])
    venta.fecha = date.strftime("%c")
    if venta.save():
        return HttpResponseRedirect(reverse('ventas/exito.html'))
    else:
        return HttpResponseRedirect(reverse('ventas/fallido.html'))