from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib import messages


# Secciones del menú que aún no tienen modelo propio en la base de datos.
# Ya tienen su vista y formulario reales; lo que falta es crear el modelo
# que guarde la información de forma permanente.
#
# tipo 'registro'  -> formulario para capturar un dato sobre un cilindro
# tipo 'consulta'  -> pantalla de búsqueda/listado
VISTAS_PENDIENTES = {
    'inspeccion-visual': {
        'tipo': 'registro', 'titulo': 'Inspección visual', 'icono': 'shield',
        'campo_label': 'Resultado', 'campo_tipo': 'select',
        'campo_opciones': ['Aprobado', 'Rechazado'],
    },
    'prueba-hidrostatica': {
        'tipo': 'registro', 'titulo': 'Prueba hidrostática', 'icono': 'speed',
        'campo_label': 'Presión de prueba (psi)', 'campo_tipo': 'number',
    },
    'baja-rechazo': {
        'tipo': 'registro', 'titulo': 'Baja / rechazo', 'icono': 'report',
        'campo_label': 'Motivo de la baja', 'campo_tipo': 'textarea',
    },
    'registrar-llenado': {
        'tipo': 'registro', 'titulo': 'Registrar llenado', 'icono': 'water_drop',
        'campo_label': 'Peso bruto (kg)', 'campo_tipo': 'number',
    },
    'verificacion-peso': {
        'tipo': 'registro', 'titulo': 'Verificación de peso', 'icono': 'scale',
        'campo_label': 'Peso verificado (kg)', 'campo_tipo': 'number',
    },
    'etiquetado-sello': {
        'tipo': 'registro', 'titulo': 'Sello de seguridad', 'icono': 'verified',
        'campo_label': 'Número de sello', 'campo_tipo': 'text',
    },
    'bodega-llenos': {
        'tipo': 'consulta', 'titulo': 'Bodega de llenos', 'icono': 'warehouse',
    },
    'bodega-vacios': {
        'tipo': 'consulta', 'titulo': 'Bodega de vacíos', 'icono': 'warehouse',
    },
    'rastreo-cilindro': {
        'tipo': 'consulta', 'titulo': 'Rastreo de cilindro', 'icono': 'route',
    },
    'historial-general': {
        'tipo': 'consulta', 'titulo': 'Historial general', 'icono': 'history',
    },
}


def vista_pendiente(request, slug):
    """
    Muestra la vista real (formulario o consulta) de una sección que todavía
    no tiene modelo propio. No guarda nada de forma permanente todavía —
    eso se conecta cuando construyamos el modelo de cada sección.
    """
    info = VISTAS_PENDIENTES.get(slug)
    if not info:
        raise Http404('Vista no encontrada')

    if info['tipo'] == 'registro' and request.method == 'POST':
        codigo_niif = request.POST.get('codigo_niif', '').strip()
        valor_campo = request.POST.get('campo_extra', '').strip()

        if not codigo_niif:
            messages.error(request, 'Ingresa un código NIIF.')
        else:
            messages.info(
                request,
                f'Vista previa — {info["titulo"]} para {codigo_niif} '
                f'({info["campo_label"]}: {valor_campo or "—"}). '
                'Aún no se guarda de forma permanente: falta conectar el modelo.'
            )
        return redirect('trazapp:vista_pendiente', slug=slug)

    return render(request, f'trazapp/vistas_pendientes/{info["tipo"]}.html', {
        'info': info,
        'slug': slug,
    })