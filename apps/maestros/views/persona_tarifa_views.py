from django.urls import reverse_lazy
from ..views.cruds_views_generics import *
from ..models.persona_tarifa_models import PersonaTarifa
from ..forms.persona_tarifa_forms import PersonaTarifaForm

class ConfigViews():
    # Modelo
    model = PersonaTarifa

    #Formulario aosicado al modelo
    form_class = PersonaTarifaForm

    # Aplicación asociada al modelo
    app_label = model._meta.app_label

    # Título del lsitado del modelo
    master_title = model._meta.verbose_name_plural

    #-- Usar esta forma cuando el modelo esté compuesto de una sola palabra: Ej. Color.
    #model_string = model.__name__.lower()  #-- Usar esta forma cuando el modelo esté compuesto de una sola palabra: Ej. Color.

    #-- Usar esta forma cuando el modelo esté compuesto por más de una palabra: Ej. TipoCambio colocar "tipo_cambio".
    model_string = "persona_tarifa"

    # Permisos
    permission_add = f"{app_label}.add_{model_string}"
    permission_change = f"{app_label}.change_{model_string}"
    permission_delete = f"{app_label}.delete_{model_string}"

    # Vistas del CRUD del modelo
    list_view_name = f"{model_string}_list"
    create_view_name = f"{model_string}_create"
    update_view_name = f"{model_string}_update"
    delete_view_name = f"{model_string}_delete"

    # Plantilla para crear o actualizar el modelo
    template_form = f"{app_label}/{model_string}_form.html"

    # Plantilla para confirmar eliminación de un registro
    template_delete = "base_confirm_delete.html"

    # Plantilla de la lista del CRUD
    template_list = f'{app_label}/maestro_list.html'

    # Contexto de los datos de la lista
    context_object_name	= 'objetos'

    # Vista del home del proyecto
    home_view_name = "home"

    # Nombre de la url 
    success_url = reverse_lazy(list_view_name)

    # Campos de validacion
    fields_to_validate = [
        ('responsable_admin', 'responsable no puede estar vacio'),
        ('fecha_tarifa', 'fecha tarifa no puede estar vacio'),
        ('monto_tarifa', 'monto tarifa no puede estar vacio'),
    ]

class DataViewList():
	search_fields = ['id_persona', 'responsable_admin']
 
	ordering = ['fecha_tarifa']

	paginate_by = 8
      
	table_headers = {
        'persona': (2, 'Persona'),  
		'responsable': (2, 'Responsable'),
        'fecha': (2, 'Fecha'),
        'tarifa': (2, 'Tarifa'),
        'vigente': (2, 'Vigente'),
		'acciones': (2, 'Acciones'),
	}
     
	table_data = [
        {'field_name': 'id_persona', 'date_format': None},
		{'field_name': 'responsable_admin', 'date_format': None},
        {'field_name': 'fecha_tarifa', 'date_format': 'd/m/Y'},
        {'field_name': 'monto_tarifa', 'date_format': None},
        {'field_name': 'tarifa_vigente', 'date_format': None},
	]

# PersonaTarifaListView - Inicio
class PersonaTarifaListView(MaestroListView):
    model = ConfigViews.model
    template_name = ConfigViews.template_list
    context_object_name = ConfigViews.context_object_name

    search_fields = DataViewList.search_fields
    ordering = DataViewList.ordering

    extra_context = {
		"master_title": ConfigViews.model._meta.verbose_name_plural,
		"home_view_name": ConfigViews.home_view_name,
		"list_view_name": ConfigViews.list_view_name,
		"create_view_name": ConfigViews.create_view_name,
		"update_view_name": ConfigViews.update_view_name,
		"delete_view_name": ConfigViews.delete_view_name,
		"table_headers": DataViewList.table_headers,
		"table_data": DataViewList.table_data,
	}

# PersonaTarifaCreateView - Inicio
class PersonaTarifaCreateView(MaestroCreateView):
    model = ConfigViews.model
    list_view_name = ConfigViews.list_view_name
    form_class = ConfigViews.form_class
    template_name = ConfigViews.template_form
    success_url = ConfigViews.success_url

    #-- Indicar el permiso que requiere para ejecutar la acción.
    permission_required = ConfigViews.permission_change

    fields_to_validate = ConfigViews.fields_to_validate

    extra_context = {
        "accion": f"Editar {ConfigViews.model._meta.verbose_name}",
        "list_view_name" : ConfigViews.list_view_name
    }

    def form_valid(self, form):
        # Imprime los datos del formulario para depuración
        print("Datos del formulario:", form.cleaned_data)
        return super().form_valid(form)

    def form_invalid(self, form):
        # Imprime los errores del formulario para depuración
        print("Errores del formulario:", form.errors)
        return super().form_invalid(form)


# PersonaTarifaUpdateView
class PersonaTarifaUpdateView(MaestroUpdateView):
    model = ConfigViews.model
    list_view_name = ConfigViews.list_view_name
    form_class = ConfigViews.form_class
    template_name = ConfigViews.template_form
    success_url = ConfigViews.success_url

    #-- Indicar el permiso que requiere para ejecutar la acción.
    permission_required = ConfigViews.permission_change
	
    fields_to_validate = ConfigViews.fields_to_validate
    
    extra_context = {
         "accion": f"Editar {ConfigViews.model._meta.verbose_name}",
		"list_view_name" : ConfigViews.list_view_name
    }

# ProfesionTecnicaDeleteView
class PersonaTarifaDeleteView (MaestroDeleteView):
    model = ConfigViews.model
    list_view_name = ConfigViews.list_view_name
    
    template_name =ConfigViews.template_delete
    success_url = ConfigViews.success_url

    #-- Indicar el permiso que requiere para ejecutar la acción.
    permission_required = ConfigViews.permission_delete

    extra_context = {
        "accion": f"Eliminar {ConfigViews.model._meta.verbose_name}",
        "list_view_name" : ConfigViews.list_view_name,
		"mensaje": "Estás seguro de eliminar el registro"
    }