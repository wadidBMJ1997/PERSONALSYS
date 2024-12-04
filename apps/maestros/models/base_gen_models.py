# \HL_PROJECT\PERSONALSYS\apps\maestros\models\models_base_gen.py
import socket
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User  # Importa el modelo User de Django

class ModeloBaseGenerico(models.Model):
    usuario = models.CharField(max_length=20, null=True, blank=True)
    estacion = models.CharField(max_length=20, null=True, blank=True)
    fcontrol = models.CharField(max_length=22, null=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        # Obtiene el usuario actual
        if not self.usuario:
            # Reemplaza con el valor correcto
            try:
                # Intenta obtener el usuario actual si ha iniciado sesión
                self.usuario = User.objects.get(username="nombre_de_usuario_actual")
            except User.DoesNotExist:
                # Si el usuario no existe o no ha iniciado sesión, 
                # puedes establecer un valor predeterminado
                self.usuario = "UserPrueba"  # O el valor que desees como predeterminado 

        # Obtiene el nombre del equipo (estación) en Windows
        if not self.estacion:
            self.estacion = socket.gethostname()

        # Obtiene la fecha y hora actual en el formato deseado
        if not self.fcontrol:
            # Reemplaza con el formato deseado
            self.fcontrol = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  

        super(ModeloBaseGenerico, self).save(*args, **kwargs)