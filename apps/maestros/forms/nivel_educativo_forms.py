from django import forms
from ..models.base_models import NivelEducativo
from django.core.exceptions import ValidationError
from diseno_base.diseno_bootstrap import (
    formclasstext, formclassselect, formclassdate)


class NivelEducativoForm(forms.ModelForm):
    
    class Meta:
        model = NivelEducativo
        fields = '__all__'

        widgets = {
                
                'estatus_nivel_educativo': 
                    forms.Select(attrs={**formclassselect}),
                
                
                'nombre_nivel_educativo': 
                    forms.TextInput(attrs={**formclasstext,'placeholder': 'Nivel educativo'}),
                
            
        }