# \HL_PROJECT\PERSONALSYS\apps\maestros\models\empresa.py
from django.db import models
from .base_gen_models import ModeloBaseGenerico

ESTATUS_GEN = [
        (True, 'Activo'),
        (False, 'Inactivo'),
        ]

CONDICION_EMPRESA = [
    (1, 'Directa'), 
    (2, 'Intermediario')
    ]

# Modelo Empresa
class Empresa(ModeloBaseGenerico):
    id_empresa = models.AutoField(primary_key=True)
    estatus_empresa = models.BooleanField('Estatus', 
                                          choices = ESTATUS_GEN, 
                                          default=True)
    condición_empresa = models.SmallIntegerField('Condición', 
                                                 choices=CONDICION_EMPRESA, 
                                                 default=1)
    codigo_empresa = models.CharField('Código', max_length=10, 
                                      blank=True, null=True)
    nombre_empresa = models.CharField('Empresa', max_length=80, 
                                      blank=True, null=True)
    fecha_registro_empresa = models.DateField('Fecha Registro', 
                                              blank=True, null=True)

    def __str__(self):
        return self.nombre_empresa

    class Meta:
        db_table = 'empresa'