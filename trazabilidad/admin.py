from django.contrib import admin
from .models.actividad import Actividad
from .models.tipo_actividad import TipoActividad
from .models.nit import Nit
from .models.proveedor import Proveedor
from .models.capacidad import Capacidad
from .models.cilindro import Cilindro


# --------------------------
# Actividad
# --------------------------
@admin.register(Actividad)
class ActividadAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion', 'tipo_actividad')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('tipo_actividad',)


# --------------------------
# TipoActividad
# --------------------------
@admin.register(TipoActividad)
class TipoActividadAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo', 'fecha_creacion', 'observacion')
    search_fields = ('tipo',)
    list_filter = ('fecha_creacion',)


# --------------------------
# Nit
# --------------------------
@admin.register(Nit)
class NitAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nit', 'direccion', 'telefono')
    search_fields = ('nombre', 'nit')


# --------------------------
# Proveedor
# --------------------------
@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nit', 'direccion', 'telefono', 'email')
    search_fields = ('nombre', 'nit')


# --------------------------
# Capacidad
# --------------------------
@admin.register(Capacidad)
class CapacidadAdmin(admin.ModelAdmin):
    list_display = ('referencia', 'peso_total_kg', 'tara_kg', 'peso_neto_kg',
                    'descripcion')
    search_fields = ('descripcion',)


# --------------------------
# Cilindro
# --------------------------
@admin.register(Cilindro)
class CilindroAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'capacidad', 'peso_neto', 'proveedor', 'estado',
                    'fecha_creacion')
    search_fields = ('codigo',)
    list_filter = ('estado', 'capacidad', 'proveedor')
