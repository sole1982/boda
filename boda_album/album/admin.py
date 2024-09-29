from django.contrib import admin
from .models import Foto
# Register your models here.

@admin.register(Foto)
class FotoAdmin(admin.ModelAdmin):
    list_display = ('nombre_invitado', 'fecha_subida', 'imagen_preview')  # Campos que se mostrarán en el panel de administración
    search_fields = ('nombre_invitado',)  # Campo de búsqueda por nombre
    list_filter = ('fecha_subida',)  # Filtros por fecha de subida

    def imagen_preview(self, obj):
        return obj.imagen.url if obj.imagen else "Sin imagen"
    
    imagen_preview.short_description = "Vista previa"