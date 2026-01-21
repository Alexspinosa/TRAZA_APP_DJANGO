from django.db import models


class TipoMantenimiento(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True)

    class Meta:
        verbose_name = "Tipo de mantenimiento"
        verbose_name_plural = "Tipos de mantenimiento"

    def __str__(self):
        return self.nombre
