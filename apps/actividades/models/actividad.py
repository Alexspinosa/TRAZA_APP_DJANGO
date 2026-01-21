from django.db import models
from .tipo_actividad import TipoActividad


class Actividad(models.Model):
    tipo_actividad = models.ForeignKey(
        TipoActividad,
        on_delete=models.PROTECT,
        related_name="actividades"
    )
    fecha = models.DateTimeField(auto_now_add=True)
    observaciones = models.TextField(blank=True)

    # Relaciones clave (se conectan con otras apps)
    cilindro = models.ForeignKey(
        "cilindros.Cilindro",
        on_delete=models.PROTECT,
        related_name="actividades"
    )
    responsable = models.ForeignKey(
        "usuarios.Usuario",
        on_delete=models.PROTECT,
        related_name="actividades"
    )

    class Meta:
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"
        ordering = ["-fecha"]

    def __str__(self):
        return f"{self.tipo_actividad} - {self.cilindro}"
