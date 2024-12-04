from django.db import models
from PERSONALSYS.apps.maestros.models.base_gen_models import ModeloBaseGenerico
from PERSONALSYS.apps.maestros.models.base_models import *

class Persona(ModeloBaseGenerico):
    id_persona = models.AutoField(primary_key=True)
    estatus_persona = models.BooleanField("Activo", default=True)
    
    nombre_persona = models.CharField("Nombres", max_length=60, null=True, 
                                      blank=True)
    apellido_persona = models.CharField("Apellidos", max_length=60, null=True, 
                                      blank=True)
    email_persona = models.CharField("e-MAIL", max_length=100, null=True, 
                               blank=True)
    fecha_ingreso = models.DateField("Fecha", null=True, blank=True)
    direccion_persona = models.CharField("Dirección", max_length=100, 
                                         null=True, blank=True)
    id_pais_telefono = models.ForeignKey(Pais, on_delete=models.PROTECT, null=True, 
                                  blank=True, related_name='pais_telefono')
    telefono_persona = models.CharField("Teléfono", max_length=12, null=True, 
                                        blank=True)
    id_pais_telefmov = models.ForeignKey(Pais, on_delete=models.PROTECT, null=True, 
                                  blank=True, related_name='pais_telefmov')
    telefmov_persona = models.CharField("Teléfono", max_length=12, null=True, 
                                        blank=True)
    ciudad_persona = models.CharField("Teléfono", max_length=12, null=True, 
                                        blank=True)

    id_tipodoc_identidad = models.ForeignKey(TipoDocumentoIdentidad, 
                                             on_delete=models.RESTRICT, 
                                             null=True, blank=True,
                                             verbose_name="Tipo de Documento")
    nro_doc_identidad = models.CharField("Número Documento Identidad", 
                                                max_length=15, null=True, 
                                                blank=True)
    
    fecha_cese = models.DateField(null=True, blank=True)
    observacion_persona = models.TextField(verbose_name="Observación Persona", 
                                           null=True, blank=True)
    
    id_persona_cargo = models.ForeignKey(PersonaCargo, on_delete=models.PROTECT, 
                                         null=True, blank=True)
    
    
    def __str__(self):
        return self.nombre_persona

    class Meta:
        db_table = 'personal'
        
