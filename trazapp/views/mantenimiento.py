from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib import messages

from ..models import Cilindro, TipoActividad, RegistroActividad


def _registrar_actividad(request, *, nombre, icono, accent, url_name, permite_imprimir=False):
    """
    Lógica compartida por las 4 actividades de mantenimiento.
    No se expone directamente por urls.py: cada actividad tiene su
    propia vista pública más abajo, que solo llama a esta con sus datos.

    permite_imprimir: solo True para Etiquetado. Habilita el botón de
    "Imprimir etiqueta" tras registrar, y el buscador de reimpresión.
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

        if permite_imprimir:
            return redirect(_url_con_query(url_name, codigo_niif))
        return redirect(f'trazapp:{url_name}')

    hoy = timezone.now().date()
    actividades_hoy = RegistroActividad.objects.filter(
        tipo_actividad=tipo_actividad,
        fecha_hora__date=hoy
    ).select_related('cilindro__tipo', 'cilindro__color').order_by('-fecha_hora')[:10]

    ultimo_niif = request.GET.get('ultimo', '') if permite_imprimir else ''

    return render(request, 'trazapp/mantenimiento/registrar.html', {
        'titulo': nombre,
        'icono': icono,
        'accent': accent,
        'url_name': url_name,
        'actividades_hoy': actividades_hoy,
        'permite_imprimir': permite_imprimir,
        'ultimo_niif': ultimo_niif,
    })


def _url_con_query(url_name, codigo_niif):
    from django.urls import reverse
    return f'{reverse(f"trazapp:{url_name}")}?ultimo={codigo_niif}'


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
        permite_imprimir=True,
    )


def imprimir_etiqueta(request):
    """
    Genera la vista imprimible de la etiqueta de un cilindro.
    Se usa tanto justo después de registrar (botón en pantalla)
    como para reimprimir en cualquier momento (buscador por NIF).
    """
    codigo_niif = request.GET.get('codigo_niif', '').strip()
    cilindro = None
    error = None

    if not codigo_niif:
        error = 'No se indicó un código NIIF.'
    else:
        try:
            cilindro = Cilindro.objects.select_related('tipo', 'color').get(codigo_niif=codigo_niif)
        except Cilindro.DoesNotExist:
            error = f'No existe un cilindro con el código {codigo_niif}.'

    return render(request, 'trazapp/mantenimiento/etiqueta.html', {
        'cilindro': cilindro,
        'codigo_niif': codigo_niif,
        'error': error,
    })