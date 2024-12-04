from django.db import models, transaction
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from .models.persona_models import Persona

@receiver(pre_save, sender=Persona)
def generar_codigo_persona(sender, instance, **kwargs):
    if not instance.codigo_persona:  # Solo genera el código si no está ya asignado
        # Asegura que la transacción sea atómica
        with transaction.atomic():
            fecha_ingreso_str = instance.fecha_ingreso.strftime('%Y%m%d')
            ultima_persona = Persona.objects.filter(
                codigo_persona__startswith=fecha_ingreso_str
            ).order_by('codigo_persona').last()

            if ultima_persona:
                ultimo_codigo = ultima_persona.codigo_persona[-5:]
                nuevo_codigo = int(ultimo_codigo) + 1
            else:
                nuevo_codigo = 1

            instance.codigo_persona = f"{fecha_ingreso_str}-{nuevo_codigo:05d}"
