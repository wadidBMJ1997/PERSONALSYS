# from django.db import models
# from django.contrib.auth.models import AbstractUser  #, User
# 
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# 
# class User(AbstractUser):
# 	email = models.EmailField("Correo electrónico")                                           # Campo requerido (obligatorio).
# 	email_alt = models.EmailField("Correo alternativo", max_length=50, null=True, blank=True) # Campo nuevo (personalizado).
# 	telefono = models.CharField("Teléfono", max_length=9, null=True, blank=True)              # Campo nuevo (personalizado).
# 
# 
# #-- Al crear un nuevo usuario este quede activo por defecto.
# @receiver(post_save, sender=User)
# def set_user_active(sender, instance, created, **kwargs):
# 	if created and not instance.is_active:
# 		instance.is_active = True
# 		instance.save()

from django.db import models

# Create your models here.

