
from django.db import models

class TipoActividad(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    observacion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.fecha_creacion.strftime('%Y-%m-%d')}"
