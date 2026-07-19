# Modelos Tipo de moviento 

from django.db import models
from .cilindro import Cilindro


class Entrada(models.Model):
    cilindro = models.ForeignKey(Cilindro, on_delete=models.CASCADE, related_name='entradas', verbose_name='Cilindro')
    fecha_hora = models.DateTimeField(auto_now_add=True, verbose_name='Fecha y hora')

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
        ordering = ['-fecha_hora']

    def __str__(self):
        return f'{self.cilindro.codigo_niif} - {self.fecha_hora.strftime("%d/%m/%Y %H:%M")}'


class Salida(models.Model):
    cilindro = models.ForeignKey(Cilindro, on_delete=models.CASCADE, related_name='salidas', verbose_name='Cilindro')
    fecha_hora = models.DateTimeField(auto_now_add=True, verbose_name='Fecha y hora')

    class Meta:
        verbose_name = 'Salida'
        verbose_name_plural = 'Salidas'
        ordering = ['-fecha_hora']

    def __str__(self):
        return f'{self.cilindro.codigo_niif} - {self.fecha_hora.strftime("%d/%m/%Y %H:%M")}'


class SalidaDiaria(models.Model):
    fecha = models.DateField(unique=True, verbose_name='Fecha')
    cantidad = models.PositiveIntegerField(verbose_name='Cantidad de cilindros')
    registrado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Salida Diaria'
        verbose_name_plural = 'Salidas Diarias'
        ordering = ['-fecha']

    def __str__(self):
        return f'{self.fecha} - {self.cantidad} cilindros'