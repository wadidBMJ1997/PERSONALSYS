from django.urls import reverse_lazy

#from django.utils.decorators import method_decorator
#from django.contrib.auth.decorators import login_required
from .cruds_views_generics import *
from ..models.base_models import Banco
from ..forms.banco_forms import BancoForm


modelo = Banco

#-- Usar esta forma cuando el modelo esté compuesto de una sola palabra: Ej. Color.
model_string = modelo.__name__.lower()   # Cuando el modelo es una sola palabra.

#-- Usar esta forma cuando el modelo esté compuesto por más de una palabra: Ej. TipoCambio colocar "tipo_cambio".
#model_string = "color"

formulario = BancoForm

template_form = f"{model_string}_form.html"
home_view_name = "home"
list_view_name = f"{model_string}_list"
create_view_name = f"{model_string}_create"
update_view_name = f"{model_string}_update"
delete_view_name = f"{model_string}_delete"


# @method_decorator(login_required, name='dispatch')
class BancoListView(MaestroListView):
	model = modelo
	template_name = f"maestros/maestro_list.html"
	context_object_name = 'objetos'
	
	search_fields = [
		'codigo_banco', 
		'nombre_banco'
	]
	ordering = ['nombre_banco']
	
	#-- Encabezado de la Tabla.
	table_headers = {
		'codigo_banco': (1, 'Código Banco'),
		'nombre_banco': (4, 'Nombre Banco'),
		'descripcion_banco': (5, 'Descripción Banco'),
		'opciones': (2, 'Opciones'),
	}
	
	#-- Columnas de la Tabla.
	table_data = [
		{'field_name': 'codigo_banco', 'date_format': None},
		{'field_name': 'nombre_banco', 'date_format': None},
		{'field_name': 'descripcion_banco', 'date_format': None},
	]
	
	#cadena_filtro = "Q(nombre_color__icontains=text)"
	extra_context = {
		"master_title": model._meta.verbose_name_plural,
		"home_view_name": home_view_name,
		"list_view_name": list_view_name,
		"create_view_name": create_view_name,
		"update_view_name": update_view_name,
		"delete_view_name": delete_view_name,
		"table_headers": table_headers,
		"table_data": table_data,
	}


# @method_decorator(login_required, name='dispatch')
class BancoCreateView(MaestroCreateView):
	model = modelo
	list_view_name = list_view_name
	form_class = formulario
	template_name = f"maestros/{template_form}"
	success_url = reverse_lazy(list_view_name) # Nombre de la url.
	
	#-- Indicar el permiso que requiere para ejecutar la acción:
	# Obtener el nombre de la aplicación a la que pertenece el modelo.
	app_label = model._meta.app_label
	# Indicar el permiso en el formato: <app_name>.<permiso>_<modelo>
	permission_required = f"{app_label}.add_{model.__name__.lower()}"
	
	fields_to_validate = [
		('nombre_color', 'El nombre no puede estar vacío.'),
	]
	extra_context = {
		"accion": f"Crear {model._meta.verbose_name}",
		"list_view_name" : list_view_name
	}


# @method_decorator(login_required, name='dispatch')
class BancoUpdateView(MaestroUpdateView):
	model = modelo
	list_view_name = list_view_name
	form_class = formulario
	template_name = f"maestros/{template_form}"
	success_url = reverse_lazy(list_view_name) # Nombre de la url.
	
	#-- Indicar el permiso que requiere para ejecutar la acción:
	# Obtener el nombre de la aplicación a la que pertenece el modelo.
	app_label = model._meta.app_label
	# Indicar el permiso eN el formato: <app_name>.<permiso>_<modelo>
	permission_required = f"{app_label}.change_{model.__name__.lower()}"
	
	extra_context = {
		"accion": f"Editar {model._meta.verbose_name}",
		"list_view_name" : list_view_name
	}


# @method_decorator(login_required, name='dispatch')
class BancoDeleteView(MaestroDeleteView):
	model = modelo
	list_view_name = list_view_name
	template_name = "base_confirm_delete.html"
	success_url = reverse_lazy(list_view_name) # Nombre de la url.
	
	#-- Indicar el permiso que requiere para ejecutar la acción:
	# Obtener el nombre de la aplicación a la que pertenece el modelo.
	app_label = model._meta.app_label
	# Indicar el permiso en el formato: <app_name>.<permiso>_<modelo>
	permission_required = f"{app_label}.delete_{model.__name__.lower()}"
 	
	extra_context = {
		"accion": f"Eliminar {model._meta.verbose_name}",
		"list_view_name" : list_view_name,
		"mensaje": "Estás seguro que deseas eliminar el Banco"
	}
# ------------------------------------------------------------------------------
