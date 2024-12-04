from django.db import models, transaction
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models.persona_models import Persona

@receiver(pre_save, sender=Persona)
def generar_codigo_persona(sender, instance, **kwargs):
    if not instance.codigo_persona:  # Solo genera el código si no está ya asignado
        # Asegura que la transacción sea atómica
        with transaction.atomic():
            fecha_ingreso_str = instance.fecha_ingreso.strftime('%Y%m%d')
            codigo_iso2 = instance.id_pais_nacionalidad.codigo_iso2 if instance.id_pais_nacionalidad else 'XX'
            codigo_prefix = f"{fecha_ingreso_str}{codigo_iso2}"

            # Busca el último código con el mismo prefix
            ultima_persona = Persona.objects.filter(
                codigo_persona__startswith=codigo_prefix
            ).order_by('codigo_persona').last()

            if ultima_persona:
                ultimo_codigo = ultima_persona.codigo_persona[-4:]
                nuevo_codigo = int(ultimo_codigo) + 1
            else:
                nuevo_codigo = 1

            # Genera el nuevo código con el formato deseado
            instance.codigo_persona = f"{codigo_prefix}{nuevo_codigo:04d}"
