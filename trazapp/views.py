from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib import messages
from .models import Cilindro, Entrada, SalidaDiaria, MetaDiaria, TipoCilindro, Color


def home(request):
    """Pantalla principal del operario"""
    hoy = timezone.now().date()

    entradas = Entrada.objects.filter(fecha_hora__date=hoy).count()
    salida = SalidaDiaria.objects.filter(fecha=hoy).first()
    meta = MetaDiaria.objects.filter(fecha=hoy).first()

    cantidad_salida = salida.cantidad if salida else 0
    cantidad_meta = meta.meta if meta else 0

    cumplimiento = 0
    if cantidad_meta > 0:
        cumplimiento = round((entradas / cantidad_meta) * 100, 1)

    diferencia = entradas - cantidad_salida

    ultimas_entradas = Entrada.objects.filter(
        fecha_hora__date=hoy
    ).select_related('cilindro__tipo', 'cilindro__color').order_by('-fecha_hora')[:10]

    return render(request, 'trazapp/home.html', {
        'entradas': entradas,
        'cantidad_salida': cantidad_salida,
        'cantidad_meta': cantidad_meta,
        'cumplimiento': cumplimiento,
        'diferencia': diferencia,
        'ultimas_entradas': ultimas_entradas,
    })


def registrar_entrada(request):
    """Registrar entrada de cilindro por NIIF"""
    if request.method == 'POST':
        codigo_niif = request.POST.get('codigo_niif', '').strip()

        if not codigo_niif:
            messages.error(request, 'Ingresa un código NIIF.')
            return render(request, 'trazapp/registrar_entrada.html')

        try:
            cilindro = Cilindro.objects.get(codigo_niif=codigo_niif)
            Entrada.objects.create(cilindro=cilindro)
            messages.success(request, f'Entrada registrada para {codigo_niif}.')
            return redirect('trazapp:home')
        except Cilindro.DoesNotExist:
            messages.warning(request, f'Cilindro {codigo_niif} no existe. Créalo primero.')
            return redirect(f'/cilindro/crear/?codigo_niif={codigo_niif}')

    return render(request, 'trazapp/registrar_entrada.html')


def crear_cilindro(request):
    """Crear cilindro si no existe y registrar entrada"""
    codigo_niif = request.GET.get('codigo_niif', '')

    if request.method == 'POST':
        codigo_niif = request.POST.get('codigo_niif', '').strip()
        tipo_id = request.POST.get('tipo')
        tara = request.POST.get('tara')
        color_id = request.POST.get('color')

        cilindro = Cilindro.objects.create(
            codigo_niif=codigo_niif,
            tipo_id=tipo_id,
            tara=tara,
            color_id=color_id,
        )
        Entrada.objects.create(cilindro=cilindro)
        messages.success(request, f'Cilindro {codigo_niif} creado y entrada registrada.')
        return redirect('trazapp:home')

    tipos = TipoCilindro.objects.all()
    colores = Color.objects.all()
    return render(request, 'trazapp/crear_cilindro.html', {
        'codigo_niif': codigo_niif,
        'tipos': tipos,
        'colores': colores,
    })


def registrar_salida(request):
    """Registrar salida diaria"""
    hoy = timezone.now().date()

    if request.method == 'POST':
        cantidad = request.POST.get('cantidad')
        SalidaDiaria.objects.update_or_create(
            fecha=hoy,
            defaults={'cantidad': cantidad}
        )
        messages.success(request, f'Salida del día registrada: {cantidad} cilindros.')
        return redirect('trazapp:home')

    salida_hoy = SalidaDiaria.objects.filter(fecha=hoy).first()
    return render(request, 'trazapp/registrar_salida.html', {
        'salida_hoy': salida_hoy
    })


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
    salida = SalidaDiaria.objects.filter(fecha=hoy).first()
    meta = MetaDiaria.objects.filter(fecha=hoy).first()

    cantidad_salida = salida.cantidad if salida else 0
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
