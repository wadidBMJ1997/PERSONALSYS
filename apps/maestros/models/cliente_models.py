# \HL_PROJECT\PERSONALSYS\apps\maestros\models\empresa.py
from django.db import models
from .base_gen_models import ModeloBaseGenerico

ESTATUS_GEN = [
        (True, 'Activo'),
        (False, 'Inactivo'),
        ]

CONDICION_CLIENTE = [
    (1, 'Directo'), 
    (2, 'Intermediario')
    ]

# Modelo Cliente
class Cliente(ModeloBaseGenerico):
    id_cliente = models.AutoField(primary_key=True)
    estatus_cliente = models.BooleanField('Estatus', 
                                          choices = ESTATUS_GEN, 
                                          default=True)
    condición_cliente = models.SmallIntegerField('Condición', 
                                                 choices=CONDICION_CLIENTE, 
                                                 default=1, 
                                                 blank=True, null=True                                             
                                                 )
    codigo_cliente = models.CharField('Código', max_length=10, 
                                      blank=True, null=True)
    nombre_cliente = models.CharField('Cliente', max_length=80, 
                                      blank=True, null=True)
    fecha_registro_cliente = models.DateField('Fecha Registro', 
                                              blank=True, null=True)

    def __str__(self):
        return self.nombre_cliente

    class Meta:
        db_table = 'cliente'
        verbose_name = ('Cliente')
        verbose_name_plural = ('Clientes')
        ordering = ['nombre_cliente', 'codigo_cliente']
