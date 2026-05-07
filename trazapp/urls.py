#Creamos las vista de la APP

from django.urls import path
from . import views

app_name = 'trazapp'

urlpatterns = [
    # Inicio
    path('', views.inicio, name='home'),

    # Entradas
    path('entrada/', views.registrar_entrada, name='registrar_entrada'),
    path('cilindro/crear/', views.crear_cilindro, name='crear_cilindro'),

    # Salida diaria
    path('salida/', views.registrar_salida, name='registrar_salida'),

    # Meta diaria
    path('meta/', views.registrar_meta, name='registrar_meta'),

    # Reporte
    path('reporte/', views.reporte_diario, name='reporte_diario'),
]
