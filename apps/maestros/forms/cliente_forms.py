# D:\HL_PROJECT\PERSONALSYS\apps\maestros\forms\empresa_forms.py
from django import forms
from ..models.cliente_models import Cliente
from django.core.exceptions import ValidationError
from diseno_base.diseno_bootstrap import (
    formclasstext, formclassselect, formclassdate)

class ClienteForm(forms.ModelForm):
    
    class Meta:
        model = Cliente
        fields = '__all__'
        
        widgets = {
            # Estatus
            'estatus_cliente': 
                forms.Select(attrs={**formclassselect}),
            # Condición del cliente
            'condicion_cliente': 
                forms.Select(attrs={**formclassselect}),
            # Código del cliente
            'codigo_cliente': 
                forms.TextInput(attrs={**formclasstext, 
                                       'placeholder': 'Ingrese el código',}),
            # Nombre del cliente
            'nombre_cliente': 
                forms.TextInput(attrs={**formclasstext, 
                                       'placeholder': 'Ingrese la empresa',}),
            # Fecha de registro de la empresa
            'fecha_registro_cliente': 
                forms.TextInput(attrs={**formclassdate, "type": 'date'}),
        }        
