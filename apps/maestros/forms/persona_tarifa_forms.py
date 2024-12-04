from django import forms
from ..models.persona_tarifa_models import PersonaTarifa
from django.core.exceptions import ValidationError
from diseno_base.diseno_bootstrap import (
    formclasstext, formclassselect, formclassdate)


class PersonaTarifaForm(forms.ModelForm):
    
    class Meta:
        model = PersonaTarifa
        fields = '__all__'

        widgets = {
                'estatus_persona_tarifa': 
                    forms.Select(attrs={**formclassselect}),
                'id_persona':
                    forms.Select(attrs={**formclassselect}),
                'responsable_admin': 
                    forms.TextInput(attrs={**formclasstext,'placeholder': 'Responsable'}),
                'tarifa_vigente':
                    forms.Select(attrs={**formclassselect}),
                'fecha_tarifa':
                    forms.TextInput(attrs={**formclassdate, 'type':'date'}),
                'monto_tarifa':              
                    forms.NumberInput(attrs={**formclasstext})
        }
