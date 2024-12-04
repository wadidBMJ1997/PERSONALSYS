from django.db import models
from .base_gen_models import ModeloBaseGenerico
from .persona_models import Persona

ESTATUS_GEN = [
        (True, 'Activo'),
        (False, 'Inactivo')
    ]

ESTATUS_TARIFA = [
    (True, 'Activo'),
    (False, 'Inactivo')
    ]

# Modelo PersonaTarifa
class PersonaTarifa(ModeloBaseGenerico):
    id_persona_tarifa = models.AutoField(primary_key=True)
    estatus_persona_tarifa = models.BooleanField("Estatus", 
                                                 default=True, 
                                                 choices=ESTATUS_GEN)
    id_persona = models.ForeignKey(Persona, on_delete=models.PROTECT, 
                                         null=True, blank=True)
    responsable_admin = models.CharField("Responsable", max_length=60, 
                                      null=True, blank=True)
    tarifa_vigente = models.BooleanField("Vigente", default=False, 
                                                 choices=ESTATUS_TARIFA)
    fecha_tarifa = models.DateField("Fecha Tarifa", null=True, blank=True)
    monto_tarifa = models.DecimalField("Tarifa", 
                                       max_digits=12, decimal_places=2, 
                                       null=True, blank=True)
    
    def __str__(self):
        return self.responsable_admin
    
    class Meta:
        db_table = 'persona_tarifa'
        verbose_name = ('Persona Tarifa')
        verbose_name_plural = ('Personas Tarifas')
        ordering = ['responsable_admin']
