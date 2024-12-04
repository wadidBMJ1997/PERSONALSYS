from django.db import models
from PERSONALSYS.apps.maestros.models.base_gen_models import ModeloBaseGenerico
from PERSONALSYS.apps.maestros.models.base_models import *
from .utils import custom_upload_to, upload_to_persona

class Persona(ModeloBaseGenerico):
    id_persona = models.AutoField(primary_key=True)
    estatus_persona = models.BooleanField("Estatus", default=True, choices=[(True, 'Activo'), (False, 'Inactivo')])
    nombre_persona = models.CharField("Nombres", max_length=60, null=True, blank=True)
    apellido_persona = models.CharField("Apellidos", max_length=60, null=True, blank=True)
    fecha_ingreso = models.DateField("Fecha Ingreso", null=True, blank=True)
    email_persona1 = models.CharField("e-MAIL Principal", max_length=100, null=True, blank=True)
    email_persona2 = models.CharField("e-MAIL Alternativo", max_length=100, null=True, blank=True)
    fecha_nacimiento = models.DateField("Fecha Nac.", null=True, blank=True)
    direccion_persona = models.CharField("Dirección", max_length=100, null=True, blank=True)
    id_pais_telefono = models.ForeignKey(Pais, on_delete=models.PROTECT, null=True, blank=True, related_name='pais_telefono', verbose_name="Código País")
    telefono_persona = models.CharField("Teléfono", max_length=12, null=True, blank=True)
    id_pais_telefmov1 = models.ForeignKey(Pais, on_delete=models.PROTECT, null=True, blank=True, related_name='pais_telefmov1')
    telefmov_persona1 = models.CharField("Celular", max_length=12, null=True, blank=True)
    id_pais_telefmov2 = models.ForeignKey(Pais, on_delete=models.PROTECT, null=True, blank=True, related_name='pais_telefmov2')
    telefmov_persona2 = models.CharField("Celular", max_length=12, null=True, blank=True)
    ciudad_residencia = models.CharField("Ciudad", max_length=50, null=True, blank=True)
    id_pais_residencia = models.ForeignKey(Pais, on_delete=models.PROTECT, null=True, blank=True, related_name='pais_residencia')
    codigo_postal = models.CharField("Código Postal", max_length=12, null=True, blank=True)
    aeropuerto_cercano = models.CharField("Aeropuerto Cercano", max_length=50, null=True, blank=True)
    id_pais_nacimiento = models.ForeignKey(Pais, on_delete=models.PROTECT, null=True, blank=True, related_name='pais_nacimiento')
    id_pais_nacionalidad = models.ForeignKey(Pais, on_delete=models.PROTECT, null=True, blank=True, related_name='pais_nacionalidad')
    imagen_persona1 = models.ImageField(upload_to=upload_to_persona, null=True, blank=True)
    imagen_persona2 = models.ImageField(upload_to=upload_to_persona, null=True, blank=True)
    id_tipodoc_identidad = models.ForeignKey(TipoDocumentoIdentidad, on_delete=models.RESTRICT, null=True, blank=True, verbose_name="Tipo de Documento")
    nro_doc_identidad = models.CharField("Número Documento Identidad", max_length=15, null=True, blank=True)
    id_pais_emision_doc = models.ForeignKey(Pais, on_delete=models.PROTECT, null=True, blank=True, related_name='pais_emision_doc')
    fecha_emision_doc = models.DateField("Fecha Emisión Documento", null=True, blank=True)
    fecha_vencimiento_doc = models.DateField("Fecha Vencimiento Documento", null=True, blank=True)
    copia_doc_identidad = models.FileField(upload_to=custom_upload_to, null=True, blank=True)
    id_profesion = models.ForeignKey(Profesion, on_delete=models.PROTECT, null=True, blank=True, related_name='profesion_persona')
    id_universidad = models.ForeignKey(Universidad, on_delete=models.PROTECT, null=True, blank=True, related_name='universidad_persona')
    descripcion_profesional = models.TextField("Descripción Profesional", null=True, blank=True)
    doc_carga_cv = models.FileField(upload_to=custom_upload_to, null=True, blank=True)
    link_video_cv = models.URLField("Enlace Video Curriculum", max_length=250, null=True, blank=True)

    def __str__(self):
        return self.nombre_persona

    class Meta:
        db_table = 'personal'
