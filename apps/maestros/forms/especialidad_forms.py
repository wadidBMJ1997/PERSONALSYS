from django import forms
from ..models.base_models import Especialidad
from django.core.exceptions import ValidationError
from diseno_base.diseno_bootstrap import (
    formclasstext, formclassselect, formclassdate)


class EspecialidadForm(forms.ModelForm):
    
    class Meta:
        model = Especialidad
        fields = '__all__'

        widgets = {
                
                'estatus_especialidad': 
                    forms.Select(attrs={**formclassselect}),
                
                
                'nombre_especialidad': 
                    forms.TextInput(attrs={**formclasstext,'placeholder': 'Nombre especialidad'}),
                
                'name_specialty': 
                    forms.TextInput(attrs={**formclasstext,'placeholder': 'Name spacialty'}),
        }