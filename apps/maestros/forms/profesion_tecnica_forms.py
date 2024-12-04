from django import forms
from ..models.base_models import ProfesionTecnica
from django.core.exceptions import ValidationError
from diseno_base.diseno_bootstrap import (
    formclasstext, formclassselect, formclassdate)


class ProfesionTecnicaForm(forms.ModelForm):
    
    class Meta:
        model = ProfesionTecnica
        fields = '__all__'

        widgets = {
                
                'estatus_profesion_tecnica': 
                    forms.Select(attrs={**formclassselect}),
                
                
                'nombre_profesion_tecnica': 
                    forms.TextInput(attrs={**formclasstext,'placeholder': 'Nombre profesion tecnica'}),
                
            
        }