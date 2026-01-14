from django.db import models
from .capacidad import Capacidad
from .proveedor import Proveedor


class Cilindro(models.Model):
    codigo = models.CharField(
        max_length=50, unique=True, default='Codigo pendiente'
    )
    capacidad = models.ForeignKey(Capacidad, on_delete=models.PROTECT)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50, default="Disponible")

    def peso_neto(self):
        """Accede al peso neto desde la capacidad"""
        return self.capacidad.peso_neto()

    def __str__(self):
        return f"{self.codigo} - {self.capacidad.peso_lb} lb"
