from decimal import Decimal
from django.db import models
from django.core.exceptions import ValidationError


class Capacidad(models.Model):
    referencia = models.CharField(
        max_length=100,
        help_text="Ej: Cilindro 20 lb",
        blank=True,
        null=True
    )

    peso_total_kg = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=Decimal("0"),
        help_text="Peso total del cilindro lleno"
    )

    tara_kg = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=Decimal("0"),
        help_text="Peso del cilindro vacío"
    )

    descripcion = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    def peso_neto_kg(self):
        """Cantidad de gas que contiene el cilindro"""
        return self.peso_total_kg - self.tara_kg

    def clean(self):
        if self.tara_kg > self.peso_total_kg:
            raise ValidationError(
                "La tara no puede ser mayor al peso total"
            )

    def __str__(self):
        ref = self.referencia or "Capacidad"
        return f"{ref} – {self.peso_neto_kg()} kg"
