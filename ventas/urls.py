"""tienda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


from . import views


urlpatterns = [
    path('', views.customlogin, name='index'),
    path('admin/', admin.site.urls),
    path('reporte/', views.reporte, name='reporte'),
    path('venta/', views.venta, name='venta'),
    path('registrar/', views.registrar, name='registrar'),
    path('borrarventa/', views.borrarventa, name='borrarventa'),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]