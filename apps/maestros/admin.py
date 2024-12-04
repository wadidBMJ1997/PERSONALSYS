
# D:\HL_PROJECT\PERSONALSYS\apps\maestros\admin.py
from django.contrib import admin
from .models.base_models import *
from .models.persona_models import Persona
from .models.empresa_models import Empresa
from .models.persona_tarifa_models import PersonaTarifa
from import_export.admin import ImportExportModelAdmin


@admin.register(Empresa)
class EmpresaAdmin(ImportExportModelAdmin):
    fields = ["estatus_empresa", "condición_empresa", "codigo_empresa",
              "nombre_empresa", "fecha_registro_empresa",
              "usuario", "estacion", "fcontrol"]
    import_id_fields = ["id_empresa"]
    readonly_fields = ("usuario", "estacion", "fcontrol")
    list_display = ("estatus_empresa", "condición_empresa", "codigo_empresa",
              "nombre_empresa", "fecha_registro_empresa")
    list_filter = ("codigo_empresa", "nombre_empresa")
    search_fields = ("codigo_empresa", "nombre_empresa")
    

@admin.register(Pais)
class PaisAdmin(ImportExportModelAdmin):
    fields = ["estatus_pais", "codigo_iso2", "codigo_iso3", "nombre_pais",
              "continente", "region_continente", "nombre_pais_ingles",
              "nombre_pais_frances", "codigo_telefonico",
              "usuario", "estacion", "fcontrol"]
    import_id_fields = ['id_pais']
    readonly_fields = ("usuario", "estacion", "fcontrol")
    list_display = ("nombre_pais", "nombre_pais_ingles", "continente", 
                    "codigo_telefonico", "codigo_iso2", "codigo_iso3")
    list_filter = ("nombre_pais", "continente")
    search_fields = ("nombre_pais", "continente")
    
@admin.register(Banco)
class BancoAdmin(ImportExportModelAdmin):
    fields = ["estatus_banco", "nombre_banco", "name_bank",
              "usuario", "estacion", "fcontrol"]
    import_id_fields = ['id_banco']
    readonly_fields = ("usuario", "estacion", "fcontrol")
    list_display = ("estatus_banco", "nombre_banco", "name_bank")
    list_filter = ("nombre_banco",)
    search_fields = ("nombre_banco", "name_bank")

@admin.register(Especialidad)
class EspecialidadAdmin(ImportExportModelAdmin):
    fields = ["estatus_especialidad", "nombre_especialidad", "name_specialty"]
    import_id_fields = ['id_especialidad']
    readonly_fields = ("usuario", "estacion", "fcontrol")
    list_display = ("estatus_especialidad", "nombre_especialidad")
    list_filter = ("nombre_especialidad",)
    search_fields = ("nombre_especialidad",)

@admin.register(Parentesco)
class ParentescoAdmin(ImportExportModelAdmin):
    fields = ["estatus_parentesco", "nombre_parentesco", "name_relationship"]
    import_id_fields = ['id_parentesco']
    readonly_fields = ("usuario", "estacion", "fcontrol")
    list_display = ("estatus_parentesco", "nombre_parentesco", "name_relationship")
    list_filter = ("nombre_parentesco",)
    search_fields = ("nombre_parentesco", "name_relationship")

# Modelo Ubicacion - Ubicación
@admin.register(Ubicacion)
class UbicacionAdmin(admin.ModelAdmin):
    fields = ["nombre_ubicacion", "ubicacion_fisica",
              "usuario", "estacion", "fcontrol"]
    readonly_fields = ("usuario", "estacion", "fcontrol")
    list_display = ("nombre_ubicacion", "ubicacion_fisica")
    list_filter = ("nombre_ubicacion", )
    search_fields = ("nombre_ubicacion", )

# Modelo Color - Color
@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    fields = ["nombre_color", "usuario", "estacion", "fcontrol"]
    readonly_fields = ("usuario", "estacion", "fcontrol")
    list_display = ("nombre_color",)
    list_filter = ("nombre_color",)
    search_fields = ("nombre_color",)

# Modelo TipoDocumentoIdentidad - Tipo de Documento de Identidad
@admin.register(TipoDocumentoIdentidad)
class TipoDocumentoIdentidadAdmin(admin.ModelAdmin):
    fields = ["nombre_tipodoc_identidad", "codigo_tipodoc_identidad", 
              "longitud", "usuario", "estacion", "fcontrol"]
    readonly_fields = ("usuario", "estacion", "fcontrol")
    list_display = ("nombre_tipodoc_identidad", "codigo_tipodoc_identidad",
                    "longitud")
    list_filter = ("nombre_tipodoc_identidad",)
    search_fields = ("nombre_tipodoc_identidad",)

# Modelo Zona - Zona
@admin.register(Zona)
class ZonaAdmin(admin.ModelAdmin):
    fields = ["nombre_zona", "descripcion_zona", "usuario", "estacion", 
              "fcontrol"]
    readonly_fields = ("usuario", "estacion", "fcontrol")
    list_display = ("nombre_zona", "descripcion_zona")
    list_filter = ("nombre_zona", "descripcion_zona")
    search_fields = ("nombre_zona", "descripcion_zona")

# Modelo SubZona - Sub Zona
@admin.register(SubZona)
class SubZonaAdmin(admin.ModelAdmin):
    fields = ["id_zona", "nombre_sub_zona", "descripcion_sub_zona",
              "usuario", "estacion", "fcontrol"]
    readonly_fields = ("usuario", "estacion", "fcontrol")
    list_display = ("get_zona", "nombre_sub_zona")
    list_filter = ("id_zona__nombre_zona", "nombre_sub_zona")
    search_fields = ("id_zona__nombre_zona", "nombre_sub_zona")

    def get_zona(self, obj):
        return obj.id_zona.nombre_zona if obj.id_zona else ""
    
    get_zona.short_description = "Zona"
    
# Modelo PersonaCargo - Persona Cargo
@admin.register(PersonaCargo)
class PersonaCargoAdmin(admin.ModelAdmin):
    fields = ["nombre_cargo", "usuario", "estacion", "fcontrol"]
    readonly_fields = ("usuario", "estacion", "fcontrol")
    list_display = ("nombre_cargo",)
    list_filter = ("nombre_cargo",)
    search_fields = ("nombre_cargo",)
    
# Modelo Persona - Persona
@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    fields = ['estatus_persona', 'nombre_persona', 'apellido_persona', 
              'email_persona1', 'email_persona2', 'fecha_ingreso', 'direccion_persona',
              'id_pais_telefono', 'telefono_persona', 'id_pais_telefmov',
              'telefmov_persona', 'ciudad_persona', 'id_pais_persona',
              'codigo_postal', 'aeropuerto_origen', 'fecha_nacimiento', 
              'id_pais_nacimiento', 'id_pais_nacionalidad', 'social_security',
              'id_tipodoc_identidad', 'nro_doc_identidad', 
              'id_pais_emision_doc', 'fecha_emision_doc', 
              'fecha_vencimiento_doc',
              'fecha_cese', 
              'observacion_persona', 'id_persona_cargo', 
              "usuario", "estacion", "fcontrol"]
    readonly_fields = ("usuario", "estacion", "fcontrol")
    list_display = ("nro_doc_identidad", "nombre_persona", "estatus_persona", )
    list_filter = ("id_tipodoc_identidad", "nro_doc_identidad", 
                   "nombre_persona", "estatus_persona",)
    search_fields = ("nro_doc_identidad", "nombre_persona",)

@admin.register(PersonaTarifa)
class PersonaTarifaAdmin(admin.ModelAdmin):
    pass