# Creamos las vista de la APP

from django.urls import path
from . import views

app_name = 'trazapp'

urlpatterns = [
    # Inicio
    path('', views.home, name='home'),

    # Entradas
    path('entrada/', views.registrar_entrada, name='registrar_entrada'),
    path('cilindro/crear/', views.crear_cilindro, name='crear_cilindro'),

    # Salida diaria
    path('salida/', views.registrar_salida, name='registrar_salida'),

    # Meta diaria
    path('meta/', views.registrar_meta, name='registrar_meta'),

    # Reporte
    path('reporte/', views.reporte_diario, name='reporte_diario'),

    # Secciones del menú sin modelo propio todavía (solo vista/formulario)
    path('vista/<slug:slug>/', views.vista_pendiente, name='vista_pendiente'),

    # Mantenimiento — ruta por actividad
    path('actividad/pintura/', views.registrar_pintura, name='registrar_pintura'),
    path('actividad/reparacion/', views.registrar_reparacion, name='registrar_reparacion'),
    path('actividad/cambio-valvula/', views.registrar_cambio_valvula, name='registrar_cambio_valvula'),
    path('actividad/etiquetado/', views.registrar_etiquetado, name='registrar_etiquetado'),
    path('actividad/etiquetado/', views.registrar_etiquetado, name='registrar_etiquetado'),
    path('actividad/etiquetado/imprimir/', views.imprimir_etiqueta, name='imprimir_etiqueta'),  
    path('actividad/etiquetado/imprimir-lote/', views.imprimir_lote, name='imprimir_lote'),     
]
