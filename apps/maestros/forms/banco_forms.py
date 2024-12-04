from django import forms
from ..models.base_models import Banco
from django.core.exceptions import ValidationError
from diseno_base.diseno_bootstrap import (
    formclasstext, formclassselect, formclassdate)


class BancoForm(forms.ModelForm):
    
    class Meta:
        model = Banco
        fields = '__all__'

        widgets = {
                
                'estatus_banco': 
                    forms.Select(attrs={**formclassselect}),
                
                
                'nombre_banco': 
                    forms.TextInput(attrs={**formclasstext,'placeholder': 'Nombre banco'}),
                
                'name_bank': 
                    forms.TextInput(attrs={**formclasstext,'placeholder': 'Name bank' }),
                
            
        }