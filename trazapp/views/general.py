from django.shortcuts import render
from django.utils import timezone

from ..models import Entrada, Salida, MetaDiaria


def home(request):
    """Pantalla principal del operario"""
    hoy = timezone.now().date()

    entradas = Entrada.objects.filter(fecha_hora__date=hoy).count()
    cantidad_salida = Salida.objects.filter(fecha_hora__date=hoy).count()
    meta = MetaDiaria.objects.filter(fecha=hoy).first()

    cantidad_meta = meta.meta if meta else 0

    cumplimiento = 0
    if cantidad_meta > 0:
        cumplimiento = round((entradas / cantidad_meta) * 100, 1)

    diferencia = entradas - cantidad_salida

    entradas_qs = Entrada.objects.filter(
        fecha_hora__date=hoy
    ).select_related('cilindro__tipo', 'cilindro__color')

    salidas_qs = Salida.objects.filter(
        fecha_hora__date=hoy
    ).select_related('cilindro__tipo', 'cilindro__color')

    ultimos_movimientos = sorted(
        [{'tipo_mov': 'Entrada', 'registro': e} for e in entradas_qs] +
        [{'tipo_mov': 'Salida', 'registro': s} for s in salidas_qs],
        key=lambda m: m['registro'].fecha_hora,
        reverse=True
    )[:10]

    return render(request, 'trazapp/home.html', {
        'entradas': entradas,
        'cantidad_salida': cantidad_salida,
        'cantidad_meta': cantidad_meta,
        'cumplimiento': cumplimiento,
        'diferencia': diferencia,
        'ultimos_movimientos': ultimos_movimientos,
    })