# PERSONALSYS/apps/procesos/views/proyecto_views.py
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from django.db import transaction

from .msdt_views_generics import *
from ..models.proyecto_models import Proyecto
from ..forms.proyecto_forms import ProyectoForm, DetalleProyectoFormSet

modelo = Proyecto

#-- Usar esta forma cuando el modelo esté compuesto de una sola palabra: Ej. Color.
model_string = modelo.__name__.lower()   # Cuando el modelo es una sola palabra.

#-- Usar esta forma cuando el modelo esté compuesto por más de una palabra: Ej. TipoCambio colocar "tipo_cambio".
#model_string = "color"

formulario = ProyectoForm

template_form = f"{model_string}_form.html"
home_view_name = "home"
list_view_name = f"{model_string}_list"
create_view_name = f"{model_string}_create"
update_view_name = f"{model_string}_update"
delete_view_name = f"{model_string}_delete"


# @method_decorator(login_required, name='dispatch')
class FacturaListView(MaestroDetalleListView):
	model = modelo
	template_name = f"procesos/maestro_detalle_list.html"
	context_object_name = 'objetos'
 
	search_fields = [
     'codigo_proyecto',
	]

	ordering = ['fecha_inicio_proyecto']
	
 	#-- Encabezado de la Tabla.
	table_headers = {
		'id_cliente': (3, 'Cliente'),
    'tipo_proyecto': (2, 'Tipo'),
    'codigo_proyecto': (1, 'Código'),
    'fecha_registro_proyecto': (1, 'Registro'),
    'fecha_inicio_proyecto': (1, 'Inicio'),
    'fecha_final_proyecto': (1, 'Fin'),
    'ticket_hotel': (1, 'Ticket'),
    'opciones': (2, 'Opciones'),
	}
  
 
	#-- Columnas de la Tabla.
	table_data = [
		{'field_name': 'id_cliente', 'date_format': None},
		{'field_name': 'tipo_proyecto', 'date_format': None},
		{'field_name': 'codigo_proyecto', 'date_format': None},
		{'field_name': 'fecha_registro_proyecto', 'date_format': 'd/m/Y'},
    {'field_name': 'fecha_inicio_proyecto', 'date_format': 'd/m/Y'},
    {'field_name': 'fecha_final_proyecto', 'date_format': 'd/m/Y'},
		{'field_name': 'ticket_hotel', 'date_format': None},
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
class FacturaCreateView(MaestroDetalleCreateView):
	model = modelo
	form_class = formulario
	template_name = f"procesos/{template_form}"
	success_url = reverse_lazy(list_view_name) # Nombre de la url.
 
	#-- Indicar el permiso que requiere para ejecutar la acción:
	# Obtener el nombre de la aplicación a la que pertenece el modelo.
	app_label = model._meta.app_label
	# Indicar el permiso eN el formato: <app_name>.<permiso>_<modelo>
	permission_required = f"{app_label}.change_{model.__name__.lower()}"
	
	def get_context_data(self, **kwargs):
		data = super().get_context_data(**kwargs)
  
		#data['tipos_documento'] = TipoDocumentoIdentidad.objects.filter(estatus_tipo_documento=True)
  
		if self.request.POST:
			data['formset'] = DetalleProyectoFormSet(self.request.POST, instance=self.object)
		else:
			data['formset'] = DetalleProyectoFormSet(instance=self.object)
  
		return data

	def form_valid(self, form):
		context = self.get_context_data()
		formset = context['formset']

		with transaction.atomic():
			self.object = form.save(commit=False)
			self.object.save()

			formset.instance = self.object
			if formset.is_valid():
				formset.save()
				return redirect(list_view_name)
			else:
				return self.form_invalid(form)

	def get_success_url(self):
		return reverse(list_view_name)


# @method_decorator(login_required, name='dispatch')
class FacturaUpdateView(MaestroDetalleUpdateView):
	model = modelo
	form_class = formulario
	template_name = f"procesos/{template_form}"
	success_url = reverse_lazy(list_view_name) # Nombre de la url.
 
	#-- Indicar el permiso que requiere para ejecutar la acción:
	# Obtener el nombre de la aplicación a la que pertenece el modelo.
	app_label = model._meta.app_label
	# Indicar el permiso eN el formato: <app_name>.<permiso>_<modelo>
	permission_required = f"{app_label}.change_{model.__name__.lower()}"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
  
		# context['tipos_documento'] = TipoDocumentoIdentidad.objects.filter(estatus_tipo_documento=True)

		if self.request.POST:
			context['formset'] = DetalleProyectoFormSet(self.request.POST, instance=self.object)
		else:
			formset = DetalleProyectoFormSet(instance=self.object)
   
			context['formset'] = formset
            
		return context

	def form_valid(self, form):
		context = self.get_context_data()
		formset = context['formset']

		if formset.is_valid():
			with transaction.atomic():
				self.object = form.save()
				formset.instance = self.object
                # print(formset.cleaned_data)  # Verifica los datos limpiados
				formset.save()
            
			return redirect(self.get_success_url())
		else:
			return self.form_invalid(form)

	def get_success_url(self):
		return self.success_url


# @method_decorator(login_required, name='dispatch')
class FacturaDeleteView(MaestroDetalleDeleteView):
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
		"mensaje": "Estás seguro que deseas eliminar el Registro"
	}
# ------------------------------------------------------------------------------
