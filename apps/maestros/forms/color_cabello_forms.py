from django import forms
from ..models.base_models import ColorCabello
from django.core.exceptions import ValidationError
from diseno_base.diseno_bootstrap import (
    formclasstext, formclassselect, formclassdate)


class ColorCabelloForm(forms.ModelForm):
    
    class Meta:
        model = ColorCabello
        fields = '__all__'

        widgets = {
                #Estatus
                'estatus_color_cabello': 
                    forms.Select(attrs={**formclassselect}),
                
                #Nombre color de cabello 
                'nombre_color_cabello': 
                    forms.TextInput(attrs={**formclasstext,'placeholder': 'Nombre de color de cabello'}),
        }
       
