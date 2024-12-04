from django.apps import AppConfig


class ProcesosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.procesos'
    
    def ready(self):
        import apps.procesos.models.proyecto_models
