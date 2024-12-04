# \apps\maestros\urls.py
from django.urls import path

from .views.persona_views import *
from .views.pais_views import *
from .views.pais_views import *
from .views.parentesco_views import *
from .views.especialidad_views import *
from .views.tipo_documento_identidad_views import *
from .views.nivel_educativo_views import *
from .views.profesion_tecnica_views import *
from .views.banco_views import *
from .views.color_views import *
from .views.color_cabello_views import *
from .views.persona_tarifa_views import *
from .views.cliente_views import *

urlpatterns = [
    path('persona/', PersonaListView.as_view(), name='persona_list'),
    path('persona/nueva/', PersonaCreateView.as_view(), name='persona_create'),
    path('persona/<int:pk>/editar/', PersonaUpdateView.as_view(), name='persona_update'),
    path('persona/<int:pk>/eliminar/', PersonaDeleteView.as_view(), name='persona_delete'),
    
    path('pais/', PaisListView.as_view(), name='pais_list'),
    path('pais/nueva/', PaisCreateView.as_view(), name='pais_create'),
    path('pais/<int:pk>/editar/', PaisUpdateView.as_view(), name='pais_update'),
    path('pais/<int:pk>/eliminar/', PaisDeleteView.as_view(), name='pais_delete'),

    path('parentesco/', ParentescoListView.as_view(), name='parentesco_list'),
    path('parentesco/nueva/', ParentescoCreateView.as_view(), name='parentesco_create'),
    path('parentesco/<int:pk>/editar/', ParentescoUpdateView.as_view(), name='parentesco_update'),
    path('parentesco/<int:pk>/eliminar/', ParentescoDeleteView.as_view(), name='parentesco_delete'),
    
    path('especialidad/', EspecialidadListView.as_view(), name='especialidad_list'),
    path('especialidad/nueva/', EspecialidadCreateView.as_view(), name='especialidad_create'),
    path('especialidad/<int:pk>/editar/', EspecialidadUpdateView.as_view(), name='especialidad_update'),
    path('especialidad/<int:pk>/eliminar/', EspecialidadDeleteView.as_view(), name='especialidad_delete'),

    path('tipo_documento_identidad/', TipoDocumentoIdentidadListView.as_view(), name='tipo_documento_identidad_list'),
    path('tipo_documento_identidad/nueva/', TipoDocumentoIdentidadCreateView.as_view(), name='tipo_documento_identidad_create'),
    path('tipo_documento_identidad/<int:pk>/editar/', TipoDocumentoIdentidadUpdateView.as_view(), name='tipo_documento_identidad_update'),
    path('tipo_documento_identidad/<int:pk>/eliminar/', TipoDocumentoIdentidadDeleteView.as_view(), name='tipo_documento_identidad_delete'),

    path('nivel_educativo/', NivelEducativoListView.as_view(), name='nivel_educativo_list'),
    path('nivel_educativo/nueva/', NivelEducativoCreateView.as_view(), name='nivel_educativo_create'),
    path('nivel_educativo/<int:pk>/editar/', NivelEducativoUpdateView.as_view(), name='nivel_educativo_update'),
    path('nivel_educativo/<int:pk>/eliminar/', NivelEducativoDeleteView.as_view(), name='nivel_educativo_delete'),

    path('profesion_tecnica/', ProfesionTecnicaListView.as_view(), name='profesion_tecnica_list'),
    path('profesion_tecnica/nueva/', ProfesionTecnicaCreateView.as_view(), name='profesion_tecnica_create'),
    path('profesion_tecnica/<int:pk>/editar/', ProfesionTecnicaUpdateView.as_view(), name='profesion_tecnica_update'),
    path('profesion_tecnica/<int:pk>/eliminar/', ProfesionTecnicaDeleteView.as_view(), name='profesion_tecnica_delete'),

    path('banco/', BancoListView.as_view(), name='banco_list'),
    path('banco/nueva/', BancoCreateView.as_view(), name='banco_create'),
    path('banco/<int:pk>/editar/', BancoUpdateView.as_view(), name='banco_update'),
    path('banco/<int:pk>/eliminar/', BancoDeleteView.as_view(), name='banco_delete'),

    path('color/', ColorListView.as_view(), name='color_list'),
    path('color/nueva/', ColorCreateView.as_view(), name='color_create'),
    path('color/<int:pk>/editar/', ColorUpdateView.as_view(), name='color_update'),
    path('color/<int:pk>/eliminar/', ColorDeleteView.as_view(), name='color_delete'),

    path('color_cabello/', ColorCabelloListView.as_view(), name='color_cabello_list'),
    path('color_cabello/nueva/', ColorCabelloCreateView.as_view(), name='color_cabello_create'),
    path('color_cabello/<int:pk>/editar/', ColorCabelloUpdateView.as_view(), name='color_cabello_update'),
    path('color_cabello/<int:pk>/eliminar/', ColorCabelloDeleteView.as_view(), name='color_cabello_delete'),

    path('persona_tarifa/', PersonaTarifaListView.as_view(), name='persona_tarifa_list'),
    path('persona_tarifa/nueva/', PersonaTarifaCreateView.as_view(), name='persona_tarifa_create'),
    path('persona_tarifa/<int:pk>/editar/', PersonaTarifaUpdateView.as_view(), name='persona_tarifa_update'),
    path('persona_tarifa/<int:pk>/eliminar/', PersonaTarifaDeleteView.as_view(), name='persona_tarifa_delete'),

    path('cliente/', ClienteListView.as_view(), name='cliente_list'),
    path('cliente/nueva/', ClienteCreateView.as_view(), name='cliente_create'),
    path('cliente/<int:pk>/editar/', ClienteUpdateView.as_view(), name='cliente_update'),
    path('cliente/<int:pk>/eliminar/', ClienteDeleteView.as_view(), name='cliente_delete'),
    
]