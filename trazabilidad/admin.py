from django.contrib import admin
from .models import TipoActividad, Actividad

@admin.register(TipoActividad)
class TipoActividadAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'fecha_creacion', 'observacion')
    list_filter = ('fecha_creacion',)
    search_fields = ('nombre', 'observacion')

@admin.register(Actividad)
class ActividadAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo', 'fecha', 'observacion')
    list_filter = ('tipo', 'fecha')
    search_fields = ('observacion',)
