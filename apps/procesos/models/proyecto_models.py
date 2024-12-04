from django.db import models
from apps.maestros.models.base_gen_models import ModeloBaseGenerico
from apps.maestros.models.base_models import *
from apps.maestros.models.cliente_models import Cliente

CONDICION_PROYECTO = [
        (1, 'En Preparación'),
        (2, 'En Proceso'),
        (3, 'Suspendido'),
        (4, 'Finalizado'),
    ]

TIPO_PROYECTO = [
        (1, 'Dry Dock'),
        (2, 'Sealing'),
        (3, 'Survey'),
        (4, 'Survey - Dry Dock'),
        (5, 'Survey - Sealing'),
    ]

TICKET_HOTEL = [
        (True, 'Pagamos Nosotros'),
        (False, 'Paga la Naviera'),
        ]

CONFIRMADO = [
        (True, 'Confirmado'),
        (False, 'No Confirmado'),
        ]

# Modelo Proyecto
class Proyecto(ModeloBaseGenerico):
    # ID del modelo Proyecto
    id_proyecto = models.AutoField(primary_key=True)
    
    # Información General
    id_cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, 
                                            null=True, blank=True, 
                                            related_name='id_empresa_ini',
                                            verbose_name ='Empresa INI')
    
    gerente_proyecto = models.CharField("Gerente Proyecto", max_length=40, null=True, 
                                      blank=True)
    
    orden_compra = models.CharField("Orden Compra", max_length=10, null=True, 
                                      blank=True)
    
    id_cliente_pm = models.ForeignKey(Cliente, on_delete=models.PROTECT, 
                                             null=True, blank=True, 
                                             related_name='id_empresa_pm',
                                             verbose_name ='Empresa PM')

    id_cliente_po = models.ForeignKey(Cliente, on_delete=models.PROTECT, 
                                            null=True, blank=True,
                                            related_name='id_empresa_po',
                                            verbose_name ='Empresa PO')
    
    condicion_proyecto = models.SmallIntegerField('Condición', 
                                                  choices=CONDICION_PROYECTO,
                                                  default=1)
    tipo_proyecto = models.SmallIntegerField('Tipo', 
                                                  choices=TIPO_PROYECTO,
                                                  default=1)
    codigo_proyecto = models.CharField("Código", max_length=60, null=True, 
                                      blank=True)
    nombre_proyecto = models.CharField("Proyecto", max_length=60, null=True, 
                                      blank=True)
    fecha_registro_proyecto = models.DateField('Fecha Registro', blank=True, null=True)
    fecha_inicio_proyecto = models.DateField('Fecha Inicio', blank=True, null=True)
    fecha_final_proyecto = models.DateField('Fecha Final', blank=True, null=True)
    
    ticket_hotel = models.BooleanField("Ticket", default=True,
                                           choices=TICKET_HOTEL)
    ubicacion_inicial = models.CharField("Ubicación Inicial", max_length=60, null=True, 
                                      blank=True)
    ubicacion_final = models.CharField("Ubicación Final", max_length=60, null=True, 
                                      blank=True)
    vessel_name  = models.CharField("Nombre del Vhiculo", max_length=20, null=True, 
                                      blank=True)  
    observaciones_proyecto = models.CharField("Observaciones", max_length=80, null=True, 
                                      blank=True)
    
    @property
    def tipo_proyecto_label(self):
         return self.get_tipo_proyecto_display()
    
    def __str__(self):
        # return self.codigo_proyecto
        return self.codigo_proyecto if self.codigo_proyecto else "Sin codigo"

    class Meta:
        db_table = 'proyecto'

# Modelo DetalleProyecto
class DetalleProyecto(ModeloBaseGenerico):
    id_detalle_proyecto = models.AutoField(primary_key=True)
    id_proyecto = models.ForeignKey(Proyecto, on_delete=models.PROTECT, 
                                    null=True, blank=True)
    codigo_persona = models.CharField("Código", max_length=14, 
                                      null=True, blank=True)
    nombre_persona = models.CharField("Nombres", max_length=60, 
                                      null=True, blank=True)
    apellido_persona = models.CharField("Apellidos", max_length=60, 
                                        null=True, blank=True)
    puesto_trabajo = models.CharField("Puesto", max_length=40, 
                                        null=True, blank=True)
    pais_ciudadania =  models.CharField("Puesto", max_length=40, 
                                        null=True, blank=True)
    aeropuerto_cercano = models.CharField("Aeropuesto Cercano", 
                                          max_length=60, 
                                          null=True, blank=True)
    dob = models.DateField("D.O.B", 
                           null=True, blank=True)
    numero_pasaporte = models.CharField("Pasaporte", max_length=40, 
                                 null=True, blank=True)
    fecha_exp_pasaporte = models.DateField("Fecha Exp. Pas.", 
                                        null=True, blank=True)
    tipo_visa = models.CharField("Tipo Visa", max_length=10, 
                                 null=True, blank=True)
    numero_visa = models.CharField("Número Visa", max_length=15, 
                                 null=True, blank=True)
    #Campos añadidos email persona, fech. exp. visa y compañía
    email_persona = models.CharField("e-MAIL Principal", max_length=100, 
                                      null=True, blank=True)
    fecha_exp_visa = models.DateField("Fecha Exp. Visa", 
                                        null=True, blank=True)
    companhia = models.CharField("Compañía", max_length=100, null= True, blank=True)
    fecha_inicio_persona = models.DateField('Fecha Inicio', blank=True, null=True)
    fecha_final_persona = models.DateField('Fecha Final', blank=True, null=True)
    confirmado  = models.BooleanField("Confirmado", default=True,
                                           choices=CONFIRMADO)

    def __str__(self):
        return self.codigo_persona
    
    class Meta:
        db_table = 'detalle_proyecto'

