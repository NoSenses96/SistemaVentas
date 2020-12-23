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
from django.conf import settings
from django.conf.urls.static import static


from . import views


urlpatterns = [
    path('', views.customlogin, name='index'),
    path('admin/', admin.site.urls),
    path('reporte/', views.reporte, name='reporte'),
    path('ventas-por-dia/', views.ventas_por_dia, name='ventas_por_dia'),
    path('reporte-por-dia/', views.reporte_por_dia, name='reporte_por_dia'),
    path('venta/', views.venta, name='venta'),
    path('registrar/', views.registrar, name='registrar'),
    path('borrarventa/', views.borrarventa, name='borrarventa'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]