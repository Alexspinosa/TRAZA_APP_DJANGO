# Modelos para el control de producción

from django.db import models


class TipoActividad(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    descripcion = models.TextField(blank=True, verbose_name='Descripción')

    class Meta:
        verbose_name = 'Tipo de Actividad'
        verbose_name_plural = 'Tipos de Actividad'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


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