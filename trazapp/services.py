from django.db import transaction
from django.utils import timezone

from .models import Cilindro, Entrada, Salida


@transaction.atomic
def registrar_entrada(codigo_niif):
    """
    Registra la entrada de un cilindro a la planta.
    """

    codigo_niif = codigo_niif.strip().upper()

    try:
        cilindro = Cilindro.objects.get(codigo_niif=codigo_niif)
    except Cilindro.DoesNotExist:
        raise ValueError("El código NIIF no existe.")

    entrada = Entrada.objects.create(
        cilindro=cilindro
    )

    return entrada


@transaction.atomic
def registrar_salida(codigo_niif):
    """
    Registra la salida de un cilindro.
    """

    codigo_niif = codigo_niif.strip().upper()
    hoy = timezone.now().date()

    try:
        cilindro = Cilindro.objects.get(codigo_niif=codigo_niif)
    except Cilindro.DoesNotExist:
        raise ValueError("El cilindro no existe.")

    if Salida.objects.filter(
        cilindro=cilindro,
        fecha_hora__date=hoy
    ).exists():
        raise ValueError("El cilindro ya tiene una salida registrada hoy.")

    salida = Salida.objects.create(
        cilindro=cilindro
    )

    return salida