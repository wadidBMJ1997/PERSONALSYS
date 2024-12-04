# D:\HL_PROJECT\PERSONALSYS\apps\procesos\urls.py
from django.urls import path
from .views.proyecto_views import (FacturaListView, FacturaCreateView, 
                                  FacturaUpdateView, FacturaDeleteView)
from .views.consultas_proyecto_views import buscar_persona
from .views.detalle_proyecto_views import DetalleProyectoWordView


urlpatterns = [
   path('proyecto/listar/', FacturaListView.as_view(), name='proyecto_list'),
   path('proyecto/crear/', FacturaCreateView.as_view(), name='proyecto_create'),
   path('proyecto/editar/<int:pk>/', FacturaUpdateView.as_view(), name='proyecto_update'),
   path('proyecto/eliminar/<int:pk>/', FacturaDeleteView.as_view(), name='proyecto_delete'),
   
   path('buscar/persona/', buscar_persona, name='buscar_persona'),
   path('detalle_proyecto_generado/', DetalleProyectoWordView.as_view(), name='detalle_proyecto'),

]