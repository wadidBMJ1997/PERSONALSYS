# \HL_PROJECT\PERSONALSYS\apps\maestros\models\models_base.py
from django.db import models
from .base_gen_models import ModeloBaseGenerico


ESTATUS_GEN = [
        (True, 'Activo'),
        (False, 'Inactivo'),
        ]

# Modelo Pais - Pais
class Pais(ModeloBaseGenerico):
    CONTINENTES = (
        ("América", "América"),
        ("Europa", "Europa"),
        ("Asia", "Asía"),
        ("África", "África"),
        ("Oceanía", "Oceanía"),
        ("Antártida", "Antártida"),
        ("", "Seleccione una opción"))
    
    id_pais = models.AutoField(primary_key=True)
    estatus_pais = models.BooleanField('Estatus', 
                                          choices = ESTATUS_GEN, 
                                          default=True)
    
    codigo_iso2 = models.CharField("Código ISO2", max_length=2, null=True,
                                   blank=True)
    codigo_iso3 = models.CharField("Código ISO3", max_length=3, null=True,
                                   blank=True)
    nombre_pais = models.CharField("Pais", max_length=100, null=True, 
                                   blank=True)
    continente = models.CharField("Continente", max_length=15, 
                                  choices=CONTINENTES, default="América")
    region_continente = models.CharField("Región", max_length=30, null=True,
                                         blank=True)
    nombre_pais_ingles = models.CharField("Country", max_length=100, null=True, 
                                          blank=True)
    nombre_pais_frances = models.CharField("Pays", max_length=100, null=True, 
                                           blank=True)
    
    codigo_telefonico = models.CharField("Código Telefónico", max_length=5,
                                                 null=True, blank=True)
    
    def __str__(self):
        return f"{self.nombre_pais} - {self.codigo_telefonico}"
    
    class Meta:
        db_table = 'pais'
        verbose_name = ('País')
        verbose_name_plural = ('Paises')
        ordering = ['nombre_pais']
        
# Modelo Parentesco - Parentesco
class Parentesco(ModeloBaseGenerico):
    id_parentesco = models.AutoField(primary_key=True)
    estatus_parentesco = models.BooleanField('Estatus', 
                                          choices = ESTATUS_GEN, 
                                          default=True)
    nombre_parentesco = models.CharField("Parentesco", max_length=50, null=True, 
                                    blank=True)
    name_relationship = models.CharField("Relationship", max_length=50, null=True, 
                                    blank=True)

    def __str__(self):
        return f'{self.nombre_parentesco} {self.name_relationship}'
    
    class Meta:
        db_table = 'parentesco'
        verbose_name = ('Parentesco')
        verbose_name_plural = ('Parentescos')
        ordering = ['nombre_parentesco']
        
# Modelo Especialidad - Especialidad
class Especialidad(ModeloBaseGenerico):
    id_especialidad = models.AutoField(primary_key=True)
    estatus_especialidad = models.BooleanField('Estatus', 
                                          choices = ESTATUS_GEN, 
                                          default=True)
    nombre_especialidad = models.CharField("Especialidad", max_length=50, null=True, 
                                    blank=True)
    name_specialty = models.CharField("Specialty", max_length=50, null=True, 
                                    blank=True)
    
    def __str__(self):
        return self.nombre_especialidad
    
    class Meta:
        db_table = 'especialidad'
        verbose_name = ('especialidad')
        verbose_name_plural = ('Especialidades')
        ordering = ['nombre_especialidad']


# Modelo TipoDocumentoIdentidad - Tipo de Documento de Identidad
class TipoDocumentoIdentidad(ModeloBaseGenerico):
    id_tipodoc_identidad = models.AutoField(primary_key=True)
    estatus_tipodoc_identidad = models.BooleanField('Estatus', 
                                          choices = ESTATUS_GEN, 
                                          default=True)
    codigo_tipodoc_identidad = models.CharField("Código Documento Identidad", 
                                                max_length=1, null=True, 
                                                blank=True, unique=True)
    nombre_tipodoc_identidad = models.CharField("Tipo Documento Identidad", 
                                                max_length=40, null=True, 
                                                blank=True)
    longitud = models.SmallIntegerField("Longitud", null=True, blank=True)

    def __str__(self):
        return self.nombre_tipodoc_identidad
    
    class Meta:
        db_table = 'tipodoc_identidad'
        verbose_name = ('Tipo Documento Identidad')
        verbose_name_plural = ('Tipos Documento Identidad')
        ordering = ['nombre_tipodoc_identidad']

# Modelo NivelEducativo - Nivel Educativo
class NivelEducativo(ModeloBaseGenerico):
    id_nivel_educativo = models.AutoField(primary_key=True)
    estatus_nivel_educativo = models.BooleanField('Estatus', 
                                          choices = ESTATUS_GEN, 
                                          default=True)
    nombre_nivel_educativo = models.CharField("Nivel Educativo", max_length=30, 
                                              null=True, blank=True)
    
    def __str__(self):
        return self.nombre_nivel_educativo
    
    class Meta:
        db_table = 'niveleducativo'
        verbose_name = ('Nivel Educativo')
        verbose_name_plural = ('Niveles Educativos')
        ordering = ['nombre_nivel_educativo']

# Modelo ProfesionTecnica - Profesión Técnica
class ProfesionTecnica(ModeloBaseGenerico):
    id_profesion_tecnica = models.AutoField(primary_key=True)
    estatus_profesion_tecnica = models.BooleanField('Estatus', 
                                          choices = ESTATUS_GEN, 
                                          default=True)
    nombre_profesion_tecnica = models.CharField("Profesión Técnica", max_length=30, 
                                              null=True, blank=True)
    
    def __str__(self):
        return self.nombre_profesion_tecnica
    
    class Meta:
        db_table = 'profesiontecnica'
        verbose_name = ('Profesión Técnica')
        verbose_name_plural = ('Profesiones Técnicas')
        ordering = ['nombre_profesion_tecnica']

# Modelo Banco - Bancos
class Banco(ModeloBaseGenerico):
    id_banco = models.AutoField(primary_key=True)
    estatus_banco = models.BooleanField('Estatus', 
                                          choices = ESTATUS_GEN, 
                                          default=True)
    nombre_banco = models.CharField("Banco", max_length=30, 
                                              null=True, blank=True)
    name_bank = models.CharField("Bank", max_length=30, 
                                              null=True, blank=True)
    
    def __str__(self):
        return self.nombre_banco
    
    class Meta:
        db_table = 'bancos'
        verbose_name = ('Banco')
        verbose_name_plural = ('Bancos')
        ordering = ['nombre_banco']

# Modelo Color - Color
class Color(ModeloBaseGenerico):
    id_color = models.AutoField(primary_key=True)
    estatus_color = models.BooleanField('Estatus', 
                                          choices = ESTATUS_GEN, 
                                          default=True)
    nombre_color = models.CharField("Color", max_length=30, null=True, 
                                    blank=True)

    def __str__(self):
        return self.nombre_color
    
    class Meta:
        db_table = 'color'
        verbose_name = ('Color')
        verbose_name_plural = ('Colores')
        ordering = ['nombre_color']
                
# Modelo ColorCabello - Color de Cabello
class ColorCabello(ModeloBaseGenerico):
    id_color_cabello = models.AutoField(primary_key=True)
    estatus_color_cabello = models.BooleanField('Estatus', 
                                          choices = ESTATUS_GEN, 
                                          default=True)
    nombre_color_cabello = models.CharField("Color de Cabello", max_length=30, null=True, 
                                    blank=True)

    def __str__(self):
        return self.nombre_color_cabello
    
    class Meta:
        db_table = 'color_cabello'
        verbose_name = ('Color de Cabello')
        verbose_name_plural = ('Colores de Cabello')
        ordering = ['nombre_color_cabello']
        
# Modelo ColorOjo - Color de Ojos
class ColorOjo(ModeloBaseGenerico):
    id_color_ojo = models.AutoField(primary_key=True)
    estatus_color_ojo = models.BooleanField('Estatus', 
                                          choices = ESTATUS_GEN, 
                                          default=True)
    nombre_color_ojo = models.CharField("Color de Ojos", max_length=30, null=True, 
                                    blank=True)

    def __str__(self):
        return self.nombre_color_ojo
    
    class Meta:
        db_table = 'color_ojo'
        verbose_name = ('Color de Ojo')
        verbose_name_plural = ('Colores de Ojo')
        ordering = ['nombre_color_ojo']
        
# Modelo Ubicacion - Ubicación
class Ubicacion(ModeloBaseGenerico):
    id_ubicacion = models.AutoField(primary_key=True)
    estatus_ubicacion = models.BooleanField('Estatus', 
                                          choices = ESTATUS_GEN, 
                                          default=True)
    nombre_ubicacion = models.CharField("Ubicación", max_length=20, null=True,
                                        blank=True)
    ubicacion_fisica = models.CharField("Ubicación Física", max_length=100, 
                                        null=True, blank=True)

    def __str__(self):
        return self.nombre_ubicacion
    
    class Meta:
        db_table = 'ubicacion'
        verbose_name = ('Ubicación')
        verbose_name_plural = ('Ubicaciones')
        ordering = ['nombre_ubicacion']
        
# Modelo Zona - Zona
class Zona(ModeloBaseGenerico):
    id_zona = models.AutoField(primary_key=True)
    estatus_zona = models.BooleanField('Estatus', 
                                          choices = ESTATUS_GEN, 
                                          default=True)
    nombre_zona = models.CharField("Nombre Zona", max_length=50, null=True, 
                                    blank=True)
    descripcion_zona = models.CharField("Descripción Zona", max_length=80, null=True, 
                                    blank=True)

    def __str__(self):
        return self.nombre_zona
    
    class Meta:
        db_table = 'zona'
        verbose_name = ('Zona')
        verbose_name_plural = ('Zonas')
        ordering = ['nombre_zona']
        
# Modelo SubZona - Sub Zona
class SubZona(ModeloBaseGenerico):
    id_sub_zona = models.AutoField(primary_key=True)
    estatus_sub_zona = models.BooleanField('Estatus', 
                                          choices = ESTATUS_GEN, 
                                          default=True)
    id_zona = models.ForeignKey(Zona, on_delete=models.PROTECT, null=True,
                                blank=True)
    nombre_sub_zona = models.CharField("Sub Zona", max_length=20, 
                                          null=True, blank=True)
    descripcion_sub_zona = models.CharField("Descripción Zona", max_length=80,
                                            null=True, blank=True)

    def __str__(self):
        return self.nombre_sub_zona
    
    class Meta:
        db_table = 'sub_zona'
        verbose_name = ('Sub Zona')
        verbose_name_plural = ('Sub Zonas')
        ordering = ['nombre_sub_zona']
        
# Modelo PersonaCargo - Persona Cargo
class PersonaCargo(ModeloBaseGenerico):
    id_persona_cargo = models.AutoField(primary_key=True)
    estatus_persona_cargo = models.BooleanField('Estatus', 
                                          choices = ESTATUS_GEN, 
                                          default=True)
    nombre_cargo = models.CharField("Cargo", max_length=50, null=True, 
                                    blank=True)

    def __str__(self):
        return self.nombre_cargo
    
    class Meta:
        db_table = 'persona_cargo'
        verbose_name = ('Persona Cargo')
        verbose_name_plural = ('Personas Cargo')
        ordering = ['nombre_cargo']


