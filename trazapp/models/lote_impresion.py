# Modelos que genera el lote de impresión, que se utiliza para generar los reportes de impresión y control de producción.

from django.conf import settings
from django.db import models
from django.utils import timezone


class LoteImpresion(models.Model):
    consecutivo = models.CharField(max_length=20, unique=True, editable=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    cilindros = models.ManyToManyField('Cilindro', related_name='lotes_impresion')

    def save(self, *args, **kwargs):
        if not self.consecutivo:
            hoy = timezone.now().strftime('%Y%m%d')
            ultimo = LoteImpresion.objects.filter(consecutivo__startswith=hoy).count()
            self.consecutivo = f"{hoy}-{ultimo + 1:03d}"  # ej: 20260730-001
        super().save(*args, **kwargs)

    def __str__(self):
        return self.consecutivo