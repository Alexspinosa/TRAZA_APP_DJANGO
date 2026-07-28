from .general import home
from .entradas_salidas import registrar_entrada, crear_cilindro, registrar_salida
from .mantenimiento import (
    registrar_pintura,
    registrar_reparacion,
    registrar_cambio_valvula,
    registrar_etiquetado,
    imprimir_etiqueta
)
from .pendientes import vista_pendiente
from .reportes import registrar_meta, reporte_diario