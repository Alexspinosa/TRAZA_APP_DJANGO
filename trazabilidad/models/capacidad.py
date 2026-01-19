from decimal import Decimal
from django.db import models


class Capacidad(models.Model):
    peso_lb = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=Decimal("0"),
        help_text="Peso total del cilindro lleno"
    )
    tara_lb = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=Decimal("0"),
        help_text="Peso del cilindro vacío"
    )
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    def peso_neto(self):
        """Calcula el peso neto del contenido"""
        return self.peso_lb - self.tara_lb

    def __str__(self):
        return f"{self.peso_lb} lb (Tara {self.tara_lb} lb)"
