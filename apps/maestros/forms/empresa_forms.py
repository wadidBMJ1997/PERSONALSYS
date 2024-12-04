# D:\HL_PROJECT\PERSONALSYS\apps\maestros\forms\empresa_forms.py
from django import forms
from ..models.empresa_models import Empresa
from django.core.exceptions import ValidationError
from diseno_base.diseno_bootstrap import (
    formclasstext, formclassselect, formclassdate)

class EmpresaForm(forms.ModelForm):
    
    class Meta:
        model = Empresa
        fields = '__all__'
        
        widgets = {
            # Estatus
            'estatus_empresa': 
                forms.Select(attrs={**formclassselect}),
            # Condición de la Empresa
            'condicion_empresa': 
                forms.Select(attrs={**formclassselect}),
            # Código de la empresa
            'codigo_empresa': 
                forms.TextInput(attrs={**formclasstext, 
                                       'placeholder': 'Ingrese el código',}),
            # Nombre de la empresa
            'nombre_empresa': 
                forms.TextInput(attrs={**formclasstext, 
                                       'placeholder': 'Ingrese la empresa',}),
            # Fecha de registro de la empresa
            'fecha_registro_empresa': 
                forms.TextInput(attrs={**formclassdate, "type": 'date'}),
        }        
