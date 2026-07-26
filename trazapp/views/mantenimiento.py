from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib import messages

from ..models import Cilindro, TipoActividad, RegistroActividad


def _registrar_actividad(request, *, nombre, icono, accent, url_name):
    """
    Lógica compartida por las 4 actividades de mantenimiento.
    No se expone directamente por urls.py: cada actividad tiene su
    propia vista pública más abajo, que solo llama a esta con sus datos.
    """
    tipo_actividad, _creado = TipoActividad.objects.get_or_create(nombre=nombre)

    if request.method == 'POST':
        codigo_niif = request.POST.get('codigo_niif', '').strip()
        observaciones = request.POST.get('observaciones', '').strip()

        if not codigo_niif:
            messages.error(request, 'Ingresa un código NIIF.')
            return redirect(f'trazapp:{url_name}')

        try:
            cilindro = Cilindro.objects.get(codigo_niif=codigo_niif)
        except Cilindro.DoesNotExist:
            messages.warning(request, f'El cilindro {codigo_niif} no existe.')
            return redirect(f'trazapp:{url_name}')

        RegistroActividad.objects.create(
            cilindro=cilindro,
            tipo_actividad=tipo_actividad,
            observaciones=observaciones,
        )
        messages.success(request, f'{nombre} registrada para el cilindro {codigo_niif}.')
        return redirect(f'trazapp:{url_name}')

    hoy = timezone.now().date()
    actividades_hoy = RegistroActividad.objects.filter(
        tipo_actividad=tipo_actividad,
        fecha_hora__date=hoy
    ).select_related('cilindro__tipo', 'cilindro__color').order_by('-fecha_hora')[:10]

    return render(request, 'trazapp/pintura/registrar.html', {
        'titulo': nombre,
        'icono': icono,
        'accent': accent,
        'url_name': url_name,
        'actividades_hoy': actividades_hoy,
    })


def registrar_pintura(request):
    """Registrar actividad de Pintura sobre un cilindro."""
    return _registrar_actividad(
        request,
        nombre='Pintura', icono='format_paint', accent='teal',
        url_name='registrar_pintura',
    )


def registrar_reparacion(request):
    """Registrar actividad de Reparación sobre un cilindro."""
    return _registrar_actividad(
        request,
        nombre='Reparación', icono='build', accent='amber',
        url_name='registrar_reparacion',
    )


def registrar_cambio_valvula(request):
    """Registrar actividad de Cambio de válvula sobre un cilindro."""
    return _registrar_actividad(
        request,
        nombre='Cambio de válvula', icono='plumbing', accent='indigo',
        url_name='registrar_cambio_valvula',
    )


def registrar_etiquetado(request):
    """Registrar impresión/reimpresión de etiqueta de un cilindro."""
    return _registrar_actividad(
        request,
        nombre='Etiquetado', icono='sell', accent='rose',
        url_name='registrar_etiquetado',
    )