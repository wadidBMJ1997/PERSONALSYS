# D:\SIG_PROJECTS\SIGCOERP\apps\facturacion\forms\factura_forms.py
from django import forms
from django.forms import inlineformset_factory
from ..models.proyecto_models import *

formclasstext = {'class': 'form-control border border-primary',
                 'style': 'font-size: 0.75rem; padding: 0.25rem; margin-left: 0px; margin-right: 0px;'
                 }

formclasstextsm = {'class': 'form-control form-control-sm border border-primary',
                   'style': 'font-size: 0.75rem; padding: 0.25rem; margin-left: 0px; margin-right: 0px;'
                   }

formclassselect = {'class': 'form-select border border-primary',
                   'style': 'font-size: 0.75rem; padding: 0.25rem; margin-left: 0px; margin-right: 0px;'
                   }

formclassselectsm = {'class': 'form-select form-select-sm border border-primary',
                   'style': 'font-size: 0.75rem; padding: 0.25rem; margin-left: 0px; margin-right: 0px;'
                   }

formclassdate = {'class': 'form-control border border-primary datetimepicker',
                 'style': 'font-size: 0.75rem; padding: 0.25rem; margin-left: 0px; margin-right: 0px;'
                 }

formclassdatesm = {'class': 'form-control form-select-sm border border-primary datetimepicker',
                   'style': 'font-size: 0.75rem; padding: 0.25rem; margin-left: 0px; margin-right: 0px;'}


class ProyectoForm(forms.ModelForm):
    
    class Meta:
        model = Proyecto
        fields = '__all__'

        widgets = {
            # Información General
            "id_proyecto": forms.HiddenInput(),
            
            'id_cliente': 
                forms.Select(attrs={**formclassselectsm}),
            'gerente_proyecto':
                forms.TextInput(attrs={**formclasstextsm, 
                                    'placeholder': 'Gerente del Proyecto'}),
            'orden_compra':
                forms.TextInput(attrs={**formclasstextsm, 
                                    'placeholder': 'Orden de Compra'}),
            'id_cliente_pm': 
                forms.Select(attrs={**formclassselectsm}),
            'id_cliente_po': 
                forms.Select(attrs={**formclassselectsm}),
            'condicion_proyecto': 
                forms.Select(attrs={**formclassselectsm}),
            'tipo_proyecto':
                forms.Select(attrs={**formclassselectsm}), 
            'codigo_proyecto': 
                forms.TextInput(attrs={**formclasstextsm, 
                                    'placeholder': 'Código del Proyecto'}),  
            'nombre_proyecto': 
                forms.TextInput(attrs={**formclasstextsm, 
                                    'placeholder': 'Nombre del Proyecto'}),
            'fecha_registro_proyecto': 
                forms.TextInput(attrs={"type": 'date', **formclassdatesm}),
            'fecha_inicio_proyecto': 
                forms.TextInput(attrs={"type": 'date', **formclassdatesm}),
            'fecha_final_proyecto': 
                forms.TextInput(attrs={"type": 'date', **formclassdatesm}),
            'ticket_hotel':
                forms.Select(attrs={**formclassselectsm}),
            'ubicacion_inicial':
                forms.TextInput(attrs={**formclasstextsm,
                                       'placeholder': 'Ubicación Inicial'}),
            'ubicacion_final':
                forms.TextInput(attrs={**formclasstextsm,
                                       'placeholder': 'Ubicación Final'}),
            'observaciones_proyecto':
                forms.TextInput(attrs={**formclasstextsm, 
                                    'placeholder': 'Observaciones del Proyecto'}),
            
        }
                
       
class DetalleProyectoForm(forms.ModelForm):
    
    class Meta:
        model = DetalleProyecto
        
        fields = "__all__"
        
        widgets = {
            'id_detalle_proyecto': forms.HiddenInput(),
            'id_proyecto': forms.HiddenInput(),
            
            'codigo_persona':
                forms.TextInput(attrs={**formclasstextsm}),
            'nombre_persona':
                forms.TextInput(attrs={**formclasstextsm}),
            'apellido_persona':
                forms.TextInput(attrs={**formclasstextsm}),
            'puesto_trabajo':
                forms.TextInput(attrs={**formclasstextsm}),
            'pais_ciudadania':
                forms.TextInput(attrs={**formclasstextsm}),
            'aeropuerto_cercano':
                forms.TextInput(attrs={**formclasstextsm}),
            'dob':
                forms.TextInput(attrs={"type": 'date', **formclassdatesm}),
            'numero_pasaporte':
                forms.TextInput(attrs={**formclasstextsm}),
            'fecha_exp_pasaporte':
                forms.TextInput(attrs={"type": 'date', **formclassdatesm}),
            'tipo_visa':
                forms.TextInput(attrs={**formclasstextsm}),
            'numero_visa':
                forms.TextInput(attrs={**formclasstextsm}),
            'fecha_inicio_persona':
                forms.TextInput(attrs={"type": 'date', **formclassdatesm}),
            'fecha_final_persona':
                forms.TextInput(attrs={"type": 'date', **formclassdatesm}),
            'confirmado':
                forms.Select(attrs={**formclassselectsm}),
            
        }

DetalleProyectoFormSet = inlineformset_factory(Proyecto, DetalleProyecto, form=DetalleProyectoForm, extra=0)
formset = DetalleProyectoFormSet(queryset=DetalleProyecto.objects.none())
