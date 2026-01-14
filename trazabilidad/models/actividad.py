from django.db import models
from .tipo_actividad import TipoActividad


class Actividad(models.Model):
    nombre = models.CharField(max_length=100, default='Nombre pendiente')
    descripcion = models.TextField(blank=True, null=True)
    tipo_actividad = models.ForeignKey(TipoActividad, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
