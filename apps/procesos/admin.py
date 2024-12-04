from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models.proyecto_models import Proyecto

# Register your models here.
@admin.register(Proyecto)
class ProyectoAdmin(ImportExportModelAdmin):
    fields = ["id_cliente", "id_cliente_pm", "id_cliente_po",
              "condicion_proyecto", "codigo_proyecto", 
              "nombre_proyecto", "fecha_registro_proyecto",
              "usuario", "estacion", "fcontrol"]
    import_id_fields = ["id_proyecto"]
    readonly_fields = ("usuario", "estacion", "fcontrol")
    list_display = ("id_cliente", "condicion_proyecto",
                    "codigo_proyecto", "nombre_proyecto", 
                    "fecha_registro_proyecto")
    list_filter = ("codigo_proyecto", "nombre_proyecto")
    search_fields = ("codigo_proyecto", "nombre_proyecto")
