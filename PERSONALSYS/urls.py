## \HL_PROJECT\PERSONALSYS\PERSONALSYS\urls.py
from django.contrib import admin
from django.urls import path, include

#from .views import InicioView  # Ajusta la importación según la ubicación exacta
from .views import home_view

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
	
    #path('', InicioView.as_view(), name='inicio'),
    path('', home_view, name='home'),
	
	path('usuarios/', include('apps.usuarios.urls')),
    path('maestros/', include('apps.maestros.urls')),
    path('procesos/', include('apps.procesos.urls')),
    # path('maestros/', include('apps.maestros.urls')),  # Asegúrate de tener la ruta correcta aquí
    # Otras rutas de tus aplicaciones...
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
