from django import forms
from ..models.base_models import Parentesco
from django.core.exceptions import ValidationError
from diseno_base.diseno_bootstrap import (
    formclasstext, formclassselect, formclassdate)


class ParentescoForm(forms.ModelForm):
    
    class Meta:
        model = Parentesco
        fields = '__all__'

        widgets = {
                
                'estatus_parentesco': 
                    forms.Select(attrs={**formclassselect}),
                
                
                'nombre_parentesco': 
                    forms.TextInput(attrs={**formclasstext,'placeholder': 'Nombre parentesco'}),
                
                'name_relationship': 
                    forms.TextInput(attrs={**formclasstext,'placeholder': 'Nombre relacionado'}),
        }