from django.db import models


class Proveedor(models.Model):
    nombre = models.CharField(max_length=100, default='Nombre pendiente')
    nit = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.nombre
