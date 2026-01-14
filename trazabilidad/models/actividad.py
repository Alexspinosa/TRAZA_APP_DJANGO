
from django.db import models
from .tipo_actividad import TipoActividad

class Actividad(models.Model):
    tipo = models.ForeignKey(TipoActividad, on_delete=models.PROTECT)
    fecha = models.DateTimeField(auto_now_add=True)
    observacion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.tipo.nombre} - {self.fecha.strftime('%Y-%m-%d %H:%M')}"
