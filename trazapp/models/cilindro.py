# Modelos especificaciones de Cilindros

from django.db import models


class TipoCilindro(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    capacidad = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Capacidad (kg)')
    referencia = models.CharField(max_length=50, blank=True, verbose_name='Referencia')

    class Meta:
        verbose_name = 'Tipo de Cilindro'
        verbose_name_plural = 'Tipos de Cilindro'
        ordering = ['nombre']

    def __str__(self):
        return f'{self.nombre} - {self.capacidad} kg'


class Color(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    codigo_hex = models.CharField(max_length=7, blank=True, verbose_name='Código Hex')

    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Colores'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Cilindro(models.Model):
    codigo_niif = models.CharField(max_length=50, unique=True, verbose_name='Código NIIF')
    tipo = models.ForeignKey(TipoCilindro, on_delete=models.PROTECT, verbose_name='Tipo')
    tara = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Tara (kg)')
    color = models.ForeignKey(Color, on_delete=models.PROTECT, verbose_name='Color')
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Cilindro'
        verbose_name_plural = 'Cilindros'
        ordering = ['-creado_en']

    def __str__(self):
        return f'{self.codigo_niif} - {self.tipo}'