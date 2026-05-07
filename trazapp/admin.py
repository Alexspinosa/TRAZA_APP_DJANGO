from django.contrib import admin

# Register your models here.

from .models import TipoCilindro, Color, Cilindro, Entrada, SalidaDiaria, TipoActividad, MetaDiaria


@admin.register(TipoCilindro)
class TipoCilindroAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'capacidad', 'referencia']
    search_fields = ['nombre', 'referencia']


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'codigo_hex']
    search_fields = ['nombre']


@admin.register(Cilindro)
class CilindroAdmin(admin.ModelAdmin):
    list_display = ['codigo_niif', 'tipo', 'tara', 'color', 'creado_en']
    search_fields = ['codigo_niif']
    list_filter = ['tipo', 'color']


@admin.register(Entrada)
class EntradaAdmin(admin.ModelAdmin):
    list_display = ['cilindro', 'fecha_hora']
    search_fields = ['cilindro__codigo_niif']
    list_filter = ['fecha_hora']


@admin.register(SalidaDiaria)
class SalidaDiariaAdmin(admin.ModelAdmin):
    list_display = ['fecha', 'cantidad', 'registrado_en']


@admin.register(TipoActividad)
class TipoActividadAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion']
    search_fields = ['nombre']


@admin.register(MetaDiaria)
class MetaDiariaAdmin(admin.ModelAdmin):
    list_display = ['fecha', 'meta', 'registrado_en']
