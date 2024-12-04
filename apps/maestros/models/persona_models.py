# \HL_PROJECT\PERSONALSYS\apps\maestros\models\persona_models.py
from django.db import models
from .base_gen_models import ModeloBaseGenerico
from .base_models import *
from apps.procesos.models.proyecto_models import *

from .utils import custom_upload_to

def upload_to_persona(instance, filename):
    return custom_upload_to(instance, filename, 'imagenes_personas')

def upload_to_pasaporte(instance, filename):
    return custom_upload_to(instance, filename, 'imagenes_pasaportes')

def upload_to_visa(instance, filename):
    return custom_upload_to(instance, filename, 'imagenes_visa')

def upload_to_certificacion(instance, filename):
    return custom_upload_to(instance, filename, 'imagenes_certificaciones')

def upload_to_certificacpdf(instance, filename):
    return custom_upload_to(instance, filename, 'pdf_certificaciones')

# Modelo Persona
class Persona(ModeloBaseGenerico):
    TALLA_TSHIRT_CHOICES = [
        ("S", 'Small'),
        ("M", 'Medium'),
        ("L", 'Large'),
        ("XL", 'X Large'),
        ("2XL", '2X Large'),
        ("3XL", '3X Large'),
    ]
    
    TALLA_COVERALL_CHOICES = [
        ("48", 'Size 48'),
        ("50", 'Size 50'),
        ("52", 'Size 52'),
        ("54", 'Size 54'),
        ("56", 'Size 56'),
        ("58", 'Size 58'),
    ]
    
    TALLA_PANT_CHOICES = [
        ("30:32", 'Size 30:32'),
        ("32:32", 'Size 32:32'),
        ("34:32", 'Size 34:32'),
        ("34:34", 'Size 34:34'),
        ("34:36", 'Size 34:36'),
        ("36:32", 'Size 36:32'),
        ("36:34", 'Size 36:34'),
        ("36:36", 'Size 36:36'),
        ("38:32", 'Size 38:32'),
        ("36:34", 'Size 36:34'),
        ("36:36", 'Size 36:36'),
        ("40:32", 'Size 40:32'),
        ("40:34", 'Size 40:34'),
        ("40:36", 'Size 40:36'),
    ]
    
    YES_NO_CHOICES = [
        (1, 'Yes'),
        (2, 'No'),
    ]
    
    ESTATUS_GEN = [
        (True, 'Activo'),
        (False, 'Inactivo'),
    ]
    
    ESTATUS_BLACK = [
        (True, 'En Lista'),
        (False, 'No está en Lista'),
    ]

    TIPOS_VISA_AMER = [
        ('B1', 'B1'),
        ('B2', 'B2'),
        ('B1B2', 'B1B2'),
        ('C1D', 'C1D'),
        ('ESTA', 'ESTA'),
        ('Green Card', 'Green Card'),
        ('Otros', 'Otros'),
        ('No tiene', 'No tiene'),
    ]
    
    # ID del modelo Persona
    id_persona = models.AutoField(primary_key=True)
    
    # Información Personal
    estatus_persona = models.BooleanField("Estatus", default=True, 
                                          choices=ESTATUS_GEN)
    codigo_persona = models.CharField("Código", max_length=14, 
                                      null=True, blank=True)
    nombre_persona = models.CharField("Nombres", max_length=60, 
                                      null=True, blank=True)
    apellido_persona = models.CharField("Apellidos", max_length=60, 
                                        null=True, blank=True)
    fecha_ingreso = models.DateField("Fecha Ingreso", 
                                     null=True, blank=True)
    email_persona1 = models.CharField("e-MAIL Principal", max_length=100, 
                                      null=True, blank=True)
    email_persona2 = models.CharField("e-MAIL Alternativo", 
                                      max_length=100, 
                                      null=True, blank=True)
    fecha_nacimiento = models.DateField("Fecha Nac.", 
                                        null=True, blank=True)
    direccion_persona = models.CharField("Dirección", max_length=100, 
                                         null=True, blank=True)
    id_pais_telefono = models.ForeignKey(Pais, on_delete=models.PROTECT, 
                                         null=True, blank=True, 
                                         related_name='pais_telefono', 
                                         verbose_name="Código País")
    telefono_persona = models.CharField("Teléfono", max_length=12, 
                                        null=True, blank=True)
    id_pais_telefmov1 = models.ForeignKey(Pais, on_delete=models.PROTECT, 
                                          null=True, blank=True, 
                                          related_name='pais_telefmov1',
                                          verbose_name="Código País")
    telefmov_persona1 = models.CharField("Celular", max_length=12, 
                                         null=True, blank=True)
    id_pais_telefmov2 = models.ForeignKey(Pais, on_delete=models.PROTECT, 
                                          null=True, blank=True, 
                                          related_name='pais_telefmov2',
                                          verbose_name="Código País")
    telefmov_persona2 = models.CharField("Celular", max_length=12, 
                                         null=True, blank=True)
    ciudad_residencia = models.CharField("Ciudad", max_length=50, null=True, 
                                        blank=True)
    id_pais_residencia = models.ForeignKey(Pais, on_delete=models.PROTECT, 
                                           null=True, blank=True, 
                                           related_name='pais_residencia', 
                                           verbose_name="Código País")
    codigo_postal = models.CharField("Código Postal", max_length=12, 
                                     null=True, blank=True)
    aeropuerto_cercano = models.CharField("Aeropuerto de Salida", max_length=50,
                                          null=True, blank=True)
    id_pais_nacimiento = models.ForeignKey(Pais, on_delete=models.PROTECT, 
                                           null=True, blank=True, 
                                           related_name='pais_nacimiento',
                                           verbose_name='Pais de Nacimiento')
    id_pais_nacionalidad = models.ForeignKey(Pais, on_delete=models.PROTECT, 
                                             null=True, blank=True, 
                                             related_name='pais_nacionalidad',
                                             verbose_name='Nacionalidad')
    id_pais_otranacional = models.ForeignKey(Pais, on_delete=models.PROTECT, 
                                             null=True, blank=True, 
                                             related_name='otra_nacionalidad',
                                             verbose_name='Otra Nacionalidad')
                                  
    # Imágenes de la persona
    imagen_persona1 = models.ImageField(upload_to=upload_to_persona, null=True, blank=True)
    imagen_persona2 = models.ImageField(upload_to=upload_to_persona, null=True, blank=True)
    
    # Pasaporte
    id_tipodoc_identidad = models.ForeignKey(TipoDocumentoIdentidad, 
                                             on_delete=models.RESTRICT, 
                                             null=True, blank=True,
                                             verbose_name="Tipo de Documento")
    nro_doc_identidad = models.CharField("Número Documento Identidad", 
                                                max_length=15, null=True, 
                                                blank=True)
    id_pais_emision_doc = models.ForeignKey(Pais, on_delete=models.PROTECT, 
                                            null=True, blank=True, 
                                            related_name='pais_emision_doc')
    fecha_emision_doc = models.DateField("Fecha Emisión Documento", null=True, 
                                         blank=True)
    fecha_vencimiento_doc = models.DateField("Fecha Vencimiento Documento", 
                                             null=True, blank=True)
    observaciones_documento_id = models.CharField("Observaciones del Documento", max_length=100, 
                                         null=True, blank=True)
    
    # Imágenes del pasaporte
    imagen_pasaporte1 = models.ImageField(upload_to=upload_to_pasaporte, null=True, blank=True)
    imagen_pasaporte2 = models.ImageField(upload_to=upload_to_pasaporte, null=True, blank=True)
    
    # Visa Americana
    id_pais_emision_visa1 = models.ForeignKey(Pais, on_delete=models.PROTECT, 
                                            null=True, blank=True, 
                                            related_name='pais_emisor_visa1')
    fecha_emision_visa1 = models.DateField("Fecha Emisión Visa 1", null=True, 
                                         blank=True)
    fecha_vencimiento_visa1 = models.DateField("Fecha Vencimiento Visa 1", 
                                             null=True, blank=True)
    tipo_visa1 = models.CharField("Tipo de Visa 1", max_length=20, 
                                  null=True, blank=True,
                                  choices=TIPOS_VISA_AMER)
    numero_visa1 = models.CharField("Número de Visa 1", max_length=15, 
                                         null=True, blank=True)
    
    # Imágenes de las visa Americana
    imagen_visa1 = models.ImageField(upload_to=upload_to_visa, null=True, blank=True)
    imagen_visa2 = models.ImageField(upload_to=upload_to_visa, null=True, blank=True)
    
    # Otras Visas
    id_pais_emision_visa2 = models.ForeignKey(Pais, on_delete=models.PROTECT, 
                                            null=True, blank=True, 
                                            related_name='pais_emisor_visa2')
    fecha_emision_visa2 = models.DateField("Fecha Emisión Visa 2", null=True, 
                                         blank=True)
    fecha_vencimiento_visa2 = models.DateField("Fecha Vencimiento Visa 2", 
                                             null=True, blank=True)
    tipo_visa2 = models.CharField("Tipo de Visa 2", max_length=20, 
                                  null=True, blank=True)
    numero_visa2 = models.CharField("Número de Visa 2", max_length=15, 
                                         null=True, blank=True)
        
    # Imágenes de otras visas
    imagen_visa3 = models.ImageField(upload_to=upload_to_visa, null=True, blank=True)
    imagen_visa4 = models.ImageField(upload_to=upload_to_visa, null=True, blank=True)
    
    # Especialidades
    id_especialidad1 = models.ForeignKey(Especialidad, on_delete=models.PROTECT,
                                      related_name='especialidad_principal',
                                      null=True, blank=True,
                                      verbose_name="Especialidad Principal")
    institucion_especialidad1 = models.CharField("Institucion Educativa", 
                                                 max_length=60, null=True, blank=True)
    fecha_ini_especialidad1 = models.DateField("Fecha Inicio", null=True, blank=True)
    anhos_especialidad1 = models.SmallIntegerField("Años Especialidad 1", 
                                                   null=True, blank=True)
    observacion_especialidad1 = models.CharField("Observaciones especialidad1", 
                                                 max_length=80, null=True, blank=True)
    id_especialidad2 = models.ForeignKey(Especialidad, on_delete=models.PROTECT,
                                      related_name='especialidad_secundaria',
                                      null=True, blank=True,
                                      verbose_name="Especialidad Secundaria")
    institucion_especialidad2 = models.CharField("Institucion Educativa", 
                                                 max_length=60, null=True, blank=True)
    fecha_ini_especialidad2 = models.DateField("Fecha Inicio", null=True, blank=True)
    anhos_especialidad2 = models.SmallIntegerField("Años Especialidad 2", 
                                                   null=True, blank=True)
    observacion_especialidad2 = models.CharField("Observaciones especialidad2", 
                                                 max_length=80, null=True, blank=True)
    
    # Certificaciones de Especialización
    imagen_certificacion1 = models.ImageField(upload_to=upload_to_certificacion, 
                                              null=True, blank=True)
    imagen_certificacion2 = models.ImageField(upload_to=upload_to_certificacion, 
                                              null=True, blank=True)
    imagen_certificacion3 = models.ImageField(upload_to=upload_to_certificacion, 
                                              null=True, blank=True)
    imagen_certificacion4 = models.ImageField(upload_to=upload_to_certificacion, 
                                              null=True, blank=True)
    imagen_certificacion5 = models.ImageField(upload_to=upload_to_certificacion, 
                                              null=True, blank=True)
    imagen_certificacion6 = models.ImageField(upload_to=upload_to_certificacion, 
                                              null=True, blank=True)
    imagen_certificacion7 = models.ImageField(upload_to=upload_to_certificacion, 
                                              null=True, blank=True)
    imagen_certificacion8 = models.ImageField(upload_to=upload_to_certificacion, 
                                              null=True, blank=True)
    
    pdf_certificacion1 = models.FileField(upload_to=upload_to_certificacpdf, 
                                              null=True, blank=True)
    pdf_certificacion2 = models.FileField(upload_to=upload_to_certificacpdf, 
                                              null=True, blank=True)
    pdf_certificacion3 = models.FileField(upload_to=upload_to_certificacpdf, 
                                              null=True, blank=True)
    pdf_certificacion4 = models.FileField(upload_to=upload_to_certificacpdf, 
                                              null=True, blank=True)
    pdf_certificacion5 = models.FileField(upload_to=upload_to_certificacpdf, 
                                              null=True, blank=True)
    pdf_certificacion6 = models.FileField(upload_to=upload_to_certificacpdf, 
                                              null=True, blank=True)
    pdf_certificacion7 = models.FileField(upload_to=upload_to_certificacpdf, 
                                              null=True, blank=True)
    pdf_certificacion8 = models.FileField(upload_to=upload_to_certificacpdf, 
                                              null=True, blank=True)
    
    # Referencias Laborales
    empresa_trabajo1 = models.CharField("Empresa 1", max_length=50,
                                          null=True, blank=True)
    fecha_ini_empresa1 = models.DateField("Fecha Inicio", null=True, blank=True)
    fecha_fin_empresa1 = models.DateField("Fecha Fin", null=True, blank=True)
    contacto_empresa1 = models.CharField("Persona Contacto", max_length=50,
                                          null=True, blank=True)
    email_contacto1 = models.CharField("e-MAIL Principal", max_length=100, 
                                       null=True, blank=True)
    id_pais_contacto1 = models.ForeignKey(Pais, on_delete=models.PROTECT, 
                                          null=True, blank=True, 
                                          related_name='pais_contacto1')
    telefono_contacto1 = models.CharField("Teléfono", max_length=12, 
                                         null=True, blank=True)
    empresa_trabajo2 = models.CharField("Empresa 2", max_length=50,
                                          null=True, blank=True)
    fecha_ini_empresa2 = models.DateField("Fecha Inicio", null=True, blank=True)
    fecha_fin_empresa2 = models.DateField("Fecha Fin", null=True, blank=True)
    contacto_empresa2 = models.CharField("Persona Contacto", max_length=50,
                                          null=True, blank=True)
    email_contacto2 = models.CharField("e-MAIL Principal", max_length=100, 
                                       null=True, blank=True)
    id_pais_contacto2 = models.ForeignKey(Pais, on_delete=models.PROTECT, 
                                          null=True, blank=True, 
                                          related_name='pais_contacto2')
    id_pais_contacto2 = models.ForeignKey(Pais, on_delete=models.PROTECT, 
                                          null=True, blank=True, 
                                          related_name='pais_contacto')
    telefono_contacto2 = models.CharField("Teléfono", max_length=12, 
                                         null=True, blank=True)
    empresa_trabajo3 = models.CharField("Empresa 3", max_length=50,
                                          null=True, blank=True)
    fecha_ini_empresa3 = models.DateField("Fecha Inicio", null=True, blank=True)
    fecha_fin_empresa3 = models.DateField("Fecha Fin", null=True, blank=True)
    contacto_empresa3 = models.CharField("Persona Contacto", max_length=50,
                                          null=True, blank=True)
    email_contacto3 = models.CharField("e-MAIL Principal", max_length=100, 
                                       null=True, blank=True)
    id_pais_contacto3 = models.ForeignKey(Pais, on_delete=models.PROTECT, 
                                          null=True, blank=True, 
                                          related_name='pais_contacto3')
    telefono_contacto3 = models.CharField("Teléfono", max_length=12, 
                                         null=True, blank=True)
    
    # Información Bancaria
    id_banco = models.ForeignKey(Banco, on_delete=models.PROTECT, 
                                 null=True, blank=True)
    cuenta_bancaria = models.CharField("Nro de Cuenta", max_length=25,
                                          null=True, blank=True)
    titular_cuenta_bancaria = models.CharField("Titular de la Cuenta", max_length=60,
                                          null=True, blank=True)
    codigo_swift = models.CharField("Código Swift", max_length=20,
                                          null=True, blank=True)
    id_pais_banco = models.ForeignKey(Pais, on_delete=models.PROTECT, null=True, 
                                  blank=True, related_name='pais_banco')
    direccion_banco = models.CharField("Dirección Banco", max_length=60,
                                          null=True, blank=True)
    codigo_postal_banco = models.CharField("Código Postal", max_length=10,
                                          null=True, blank=True)
    observaciones_cuenta = models.CharField("Observaciones de la Cuenta", max_length=80,
                                          null=True, blank=True)
    #Se añadió los campos cuidad_bamco y cadigo_corto_banco
    ciudad_banco = models.CharField("Ciudad Banco", max_length=60,
                                          null=True, blank=True)
    codigo_corto_banco = models.CharField("Códico corto del Banco", max_length=12,
                                          null=True, blank=True)
  

    # Proyectos con nosotros
    id_proyecto1 = models.ForeignKey(Proyecto, on_delete=models.PROTECT, null=True,
                                  blank=True, related_name='proyecto1')
    id_espec_proyecto1 = models.ForeignKey(Especialidad, on_delete=models.PROTECT,
                                      related_name='especialidad_proyecto1',
                                      null=True, blank=True)
    fecha_ini_proyecto1 = models.DateField("Fecha Inicio", null=True, blank=True)
    fecha_fin_proyecto1 = models.DateField("Fecha Fin", null=True, blank=True)
    observaciones_proyecto1 = models.CharField("Observaciones", max_length=80,
                                               null=True, blank=True)
    id_proyecto2 = models.ForeignKey(Proyecto, on_delete=models.PROTECT, null=True,
                                  blank=True, related_name='proyecto2')
    id_espec_proyecto2 = models.ForeignKey(Especialidad, on_delete=models.PROTECT,
                                      related_name='especialidad_proyecto2',
                                      null=True, blank=True)
    fecha_ini_proyecto2 = models.DateField("Fecha Inicio", null=True, blank=True)
    fecha_fin_proyecto2 = models.DateField("Fecha Fin", null=True, blank=True)
    observaciones_proyecto2 = models.CharField("Observaciones", max_length=80,
                                               null=True, blank=True)
    id_proyecto3 = models.ForeignKey(Proyecto, on_delete=models.PROTECT, null=True,
                                  blank=True, related_name='proyecto3')
    id_espec_proyecto3 = models.ForeignKey(Especialidad, on_delete=models.PROTECT,
                                      related_name='especialidad_proyecto3',
                                      null=True, blank=True)
    fecha_ini_proyecto3 = models.DateField("Fecha Inicio", null=True, blank=True)
    fecha_fin_proyecto3 = models.DateField("Fecha Fin", null=True, blank=True)
    observaciones_proyecto3 = models.CharField("Observaciones", max_length=80,
                                               null=True, blank=True)
    
    # Historial de Accidentes
    
    # Apariencia Personal
    estatura = models.DecimalField("Estatura (pies)", max_digits = 5, 
                                   decimal_places = 2, null=True, blank=True)
    peso = models.DecimalField("Peso (libras)", max_digits = 5, decimal_places = 2,
                               null=True, blank=True)
    talla_tshirt = models.CharField("Talla T-Shirt", max_length=4, 
                                    choices=TALLA_TSHIRT_CHOICES, 
                                    default="L", null=True, blank=True)
    talla_coverall = models.CharField("Talla Coverall", max_length=4, 
                                    choices=TALLA_COVERALL_CHOICES, 
                                    default="52", null=True, blank=True)
    talla_pantalon = models.CharField("Talla Pantalón", max_length=5, 
                                    choices=TALLA_PANT_CHOICES, 
                                    default="34:34", null=True, blank=True)
    
    # Información de Contacto en Caso de Emergencia
    nombre_apellidos_contacto = models.CharField("Nombres y Apellidos", 
                                                 max_length=60, null=True, 
                                                 blank=True)
    id_pais_telefcont = models.ForeignKey(Pais, on_delete=models.PROTECT, 
                                          null=True, blank=True, 
                                          related_name='pais_telefcont')
    telefono_contacto = models.CharField("Teléfono Contacto", max_length=12, 
                                         null=True, blank=True)
    email_contacto = models.CharField("e-MAIL Contacto", max_length=100, 
                                      null=True, blank=True)
    id_parentesco = models.ForeignKey(Parentesco, on_delete=models.PROTECT,
                                      null=True, blank=True)
    
    # Black List
    estatus_black = models.BooleanField("Black List", default=False, 
                                        choices=ESTATUS_BLACK)
    motivo_black = models.TextField(verbose_name="Motivo Black List", 
                                    null=True, blank=True)
    fecha_black = models.DateField("Fecha Black List", null=True, blank=True)

    # Otros
    fecha_cese = models.DateField(null=True, blank=True)
    observacion_cese = models.TextField(verbose_name="Observaciones de Cese",
                                        null=True, blank=True)
        
    def __str__(self):
        return f'{self.apellido_persona} {self.nombre_persona }'
    
    # Método que permite generar mostrar el display de estatus
    # def estatus_persona_display(self):
    #    return "Activo" if self.estatus_producto else "Inactivo"

    class Meta:
        db_table = 'personal'
        verbose_name = ('Persona')
        verbose_name_plural = ('Personas')
        ordering = ['apellido_persona', 'nombre_persona']

