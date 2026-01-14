from django.db import models


class Nit(models.Model):
    nombre = models.CharField(max_length=100, default='Nombre pendiente')
    nit = models.CharField(max_length=20, unique=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.nit}"
