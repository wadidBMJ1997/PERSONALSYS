from django import forms
from ..models.base_models import Pais
from django.core.exceptions import ValidationError
from diseno_base.diseno_bootstrap import (
    formclasstext, formclassselect, formclassdate)


class PaisForm(forms.ModelForm):
    
    class Meta:
        model = Pais
        fields = '__all__'
               
        
        widgets = {
            # Estatus y Fecha de Ingreso
            'estatus_pais': 
                forms.Select(attrs={**formclassselect, 'label': '*ESTATUS'}),
            'codigo_iso2': 
                forms.TextInput(attrs={**formclasstext,
                                       'label': 'Código ISO2',
                                       'placeholder': 'Ingrese el código ISO2',}),
            'codigo_iso3': 
                forms.TextInput(attrs={**formclasstext,
                                       'label': 'Código ISO3',
                                       'placeholder': 'Ingrese el código ISO3',}),
            'nombre_pais': 
                forms.TextInput(attrs={**formclasstext,
                                       'label': 'Pais',
                                       'placeholder': 'Ingrese el nombre del pais',}),
            'continente': 
                forms.TextInput(attrs={**formclasstext,
                                       'label': 'Continente',
                                       'placeholder': 'Ingrese el continente',}),
            'region_continente': 
                forms.TextInput(attrs={**formclasstext,
                                       'label': 'Región Continente',
                                       'placeholder': 'Ingrese la Región Continente',}),
            'nombre_pais_ingles': 
                forms.TextInput(attrs={**formclasstext,
                                       'label': 'Country',
                                       'placeholder': 'Ingrese el nombre del pais en inglés',}),
            'nombre_pais_frances': 
                forms.TextInput(attrs={**formclasstext,
                                       'label': 'Pays',
                                       'placeholder': 'Ingrese el nombre del pais en Francés',}),
            'codigo_telefonico': 
                forms.TextInput(attrs={**formclasstext,
                                       'label': 'Pays',
                                       'placeholder': 'Ingrese código telefónico del pais',}),
        }