from django import forms
from ..models.base_models import Color
from django.core.exceptions import ValidationError
from diseno_base.diseno_bootstrap import (
    formclasstext, formclassselect, formclassdate)


class ColorForm(forms.ModelForm):
    
    class Meta:
        model = Color
        fields = '__all__'

        widgets = {
                'estatus_color': 
                    forms.Select(attrs={**formclassselect}),
                
                
                'nombre_color': 
                    forms.TextInput(attrs={**formclasstext,'placeholder': 'Nombre color'}),
        }