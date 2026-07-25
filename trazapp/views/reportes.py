from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib import messages

from ..models import Entrada, Salida, MetaDiaria


def registrar_meta(request):
    """Registrar meta diaria"""
    hoy = timezone.now().date()

    if request.method == 'POST':
        meta = request.POST.get('meta')
        MetaDiaria.objects.update_or_create(
            fecha=hoy,
            defaults={'meta': meta}
        )
        messages.success(request, f'Meta del día registrada: {meta} cilindros.')
        return redirect('trazapp:home')

    meta_hoy = MetaDiaria.objects.filter(fecha=hoy).first()
    return render(request, 'trazapp/registrar_meta.html', {
        'meta_hoy': meta_hoy
    })


def reporte_diario(request):
    """Reporte del día"""
    hoy = timezone.now().date()

    entradas = Entrada.objects.filter(fecha_hora__date=hoy).count()
    cantidad_salida = Salida.objects.filter(fecha_hora__date=hoy).count()
    meta = MetaDiaria.objects.filter(fecha=hoy).first()

    cantidad_meta = meta.meta if meta else 0

    cumplimiento = 0
    if cantidad_meta > 0:
        cumplimiento = round((entradas / cantidad_meta) * 100, 1)

    diferencia = entradas - cantidad_salida

    return render(request, 'trazapp/reporte_diario.html', {
        'hoy': hoy,
        'entradas': entradas,
        'cantidad_salida': cantidad_salida,
        'cantidad_meta': cantidad_meta,
        'cumplimiento': cumplimiento,
        'diferencia': diferencia,
    })