from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from django.http import JsonResponse
from .models import Venta
from .models import Categoria


@login_required(login_url='/accounts/login/')
def reporte(request):
    ventas = Venta.objects.all()
    reporte = {}

    for venta in ventas:
        if venta.categoria.id in reporte:
            reporte[venta.categoria.id] += venta.monto
        else:
            reporte[venta.categoria.id] = venta.monto

    context = {
        'ventas': ventas,
        'reporte' : reporte
    }
    return render(request, 'ventas/reporte.html', context)

@login_required(login_url='/accounts/login/')
def ventas_por_dia(request):
    context = {
        'categorias': Categoria.objects.all(),
    }
    return render(request, 'ventas/ventas-por-dia.html', context)

def reporte_por_dia(request):
    if request.is_ajax and request.method == "POST":
        fecha = datetime.strptime(request.POST.get('fecha', False), '%d/%m/%Y').date()
        ventas = Venta.objects.filter(fecha__fecha = fecha)
        reporte = {}

        for venta in ventas:
            if venta.categoria.id in reporte:
                reporte[venta.categoria.id] += venta.monto
            else:
                reporte[venta.categoria.id] = venta.monto

        return JsonResponse({"reporte": reporte}, status=200)
    else:
        return JsonResponse({"error": ""}, status=400)

@login_required(login_url='/accounts/login/')
def venta(request):
    categorias = Categoria.objects.all()
    context = {
        'categorias': categorias,
    }
    return render(request, 'ventas/venta.html', context)

def registrar(request):
    date = datetime.now()
    venta = Venta()
    venta.monto = request.POST['monto']
    venta.categoria = Categoria(request.POST.get('categoria', False))
    venta.fecha = date.now()
    venta.save()
    messages.success(request, "Your data has been saved!")
    return HttpResponseRedirect(reverse('venta'))


def registrousuario(request):
    user = User.objects.create_user(
        request.POST.get('nombre', False),
        request.POST.get('correo', False),
        request.POST.get('contrasenna', False)
    )
    user.save()


def customlogin(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/venta/')
    else:
        return HttpResponseRedirect('/accounts/login/')


def borrarventa(request):
    venta = Venta.objects.get(id=request.GET['id'])
    venta.delete()
    return HttpResponse('bien')
