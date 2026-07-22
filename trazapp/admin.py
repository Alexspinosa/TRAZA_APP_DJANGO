from django.contrib import admin

from .models import (
    TipoCilindro,
    Color,
    Cilindro,
    Entrada,
    Salida,
    SalidaDiaria,
    TipoActividad,
    MetaDiaria,
)


# ===========================
# Catálogos
# ===========================

@admin.register(TipoCilindro)
class TipoCilindroAdmin(admin.ModelAdmin):
    list_display = ("nombre", "capacidad", "referencia")
    search_fields = ("nombre", "referencia")
    ordering = ("nombre",)
    list_per_page = 25


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "codigo_hex")
    search_fields = ("nombre",)
    ordering = ("nombre",)
    list_per_page = 25


# ===========================
# Cilindros
# ===========================

@admin.register(Cilindro)
class CilindroAdmin(admin.ModelAdmin):
    list_display = (
        "codigo_niif",
        "tipo",
        "tara",
        "color",
        "creado_en",
    )
    search_fields = ("codigo_niif",)
    list_filter = ("tipo", "color")
    ordering = ("codigo_niif",)
    list_per_page = 25


# ===========================
# Movimientos
# ===========================

@admin.register(Entrada)
class EntradaAdmin(admin.ModelAdmin):
    list_display = (
        "cilindro",
        "fecha_hora",
    )
    search_fields = ("cilindro__codigo_niif",)
    list_filter = ("fecha_hora",)
    date_hierarchy = "fecha_hora"
    ordering = ("-fecha_hora",)
    list_per_page = 25


@admin.register(Salida)
class SalidaAdmin(admin.ModelAdmin):
    list_display = (
        "cilindro",
        "fecha_hora",
    )
    search_fields = ("cilindro__codigo_niif",)
    list_filter = ("fecha_hora",)
    date_hierarchy = "fecha_hora"
    ordering = ("-fecha_hora",)
    list_per_page = 25


@admin.register(SalidaDiaria)
class SalidaDiariaAdmin(admin.ModelAdmin):
    list_display = (
        "fecha",
        "cantidad",
        "registrado_en",
    )
    ordering = ("-fecha",)
    date_hierarchy = "fecha"
    list_per_page = 25


# ===========================
# Producción
# ===========================

@admin.register(TipoActividad)
class TipoActividadAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "descripcion",
    )
    search_fields = ("nombre",)
    ordering = ("nombre",)
    list_per_page = 25


@admin.register(MetaDiaria)
class MetaDiariaAdmin(admin.ModelAdmin):
    list_display = (
        "fecha",
        "meta",
        "registrado_en",
    )
    ordering = ("-fecha",)
    date_hierarchy = "fecha"
    list_per_page = 25  