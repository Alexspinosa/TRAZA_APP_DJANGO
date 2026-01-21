from django.db import models


class EstadoCilindro(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Estado del cilindro"
        verbose_name_plural = "Estados del cilindro"

    def __str__(self):
        return self.nombre


class Cilindro(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    capacidad = models.PositiveIntegerField()
    estado = models.ForeignKey(
        EstadoCilindro,
        on_delete=models.PROTECT,
        related_name="cilindros"
    )

    class Meta:
        verbose_name = "Cilindro"
        verbose_name_plural = "Cilindros"

    def __str__(self):
        return self.codigo
