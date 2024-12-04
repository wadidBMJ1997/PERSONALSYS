from django import forms
from ..models.base_models import TipoDocumentoIdentidad
from django.core.exceptions import ValidationError
from diseno_base.diseno_bootstrap import (
    formclasstext, formclassselect, formclassdate)

class TipoDocumentoIdentidadForm(forms.ModelForm):
    
    class Meta:
        model = TipoDocumentoIdentidad
        fields = '__all__'

        widgets = {
                
                'estatus_tipodoc_identidad': 
                    forms.Select(attrs={**formclassselect}),
                
                
                'codigo_tipodoc_identidad': 
                    forms.TextInput(attrs={**formclasstext,'placeholder': 'Cod. tipo documento identidad'}),
                
                'nombre_tipodoc_identidad': 
                
                    forms.TextInput(attrs={**formclasstext,'placeholder': 'Nombre tipo documento identidad'}),
                
                'longitud': 
                    forms.TextInput(attrs={**formclasstext,'placeholder': 'Longitud'}),
        }