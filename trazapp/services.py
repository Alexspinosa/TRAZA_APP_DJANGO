from django.db import transaction

from .models import Cilindro, Entrada


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