# Modelos para el control de producción

from django.db import models

from .cilindro import Cilindro


class TipoActividad(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    descripcion = models.TextField(blank=True, verbose_name='Descripción')

    class Meta:
        verbose_name = 'Tipo de Actividad'
        verbose_name_plural = 'Tipos de Actividad'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class RegistroActividad(models.Model):
    cilindro = models.ForeignKey(Cilindro, on_delete=models.CASCADE, related_name='actividades', verbose_name='Cilindro')
    tipo_actividad = models.ForeignKey(TipoActividad, on_delete=models.CASCADE, related_name='registros', verbose_name='Tipo de actividad')
    fecha_hora = models.DateTimeField(auto_now_add=True, verbose_name='Fecha y hora')
    observaciones = models.TextField(blank=True, verbose_name='Observaciones')

    class Meta:
        verbose_name = 'Registro de Actividad'
        verbose_name_plural = 'Registros de Actividad'
        ordering = ['-fecha_hora']

    def __str__(self):
        return f'{self.cilindro.codigo_niif} - {self.tipo_actividad.nombre}'


class MetaDiaria(models.Model):
    fecha = models.DateField(unique=True, verbose_name='Fecha')
    meta = models.PositiveIntegerField(verbose_name='Meta de cilindros')
    registrado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Meta Diaria'
        verbose_name_plural = 'Metas Diarias'
        ordering = ['-fecha']

    def __str__(self):
        return f'{self.fecha} - Meta: {self.meta}'