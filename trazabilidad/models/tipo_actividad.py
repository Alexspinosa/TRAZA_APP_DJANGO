from django.db import models


class TipoActividad(models.Model):
    tipo = models.CharField(max_length=100, default='Tipo pendiente')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    observacion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.tipo} - {self.fecha_creacion.strftime('%Y-%m-%d')}"
