from django.db import models
from datetime import datetime


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    imagen = models.FileField(max_length=255)

    def __str__(self):
        return self.nombre + " " + self.imagen.name


class Venta(models.Model):
    monto = models.IntegerField(default=0)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    fecha = models.DateTimeField(blank=True, null=True, default=datetime.now())
