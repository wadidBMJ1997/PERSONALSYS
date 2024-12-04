from django import forms
from django.core.exceptions import ValidationError
from ..models.models_persona import Persona

class PersonaForm(forms.ModelForm):

    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {
            'estatus_persona': forms.Select(attrs={ 'class': 'form-select border border-primary', 'label': '*ESTATUS' }),
            'nombre_persona': forms.TextInput(attrs={ 'class': 'form-control border border-primary', 'placeholder': 'Ingrese su nombre' }),
            'apellido_persona': forms.TextInput(attrs={ 'class': 'form-control border border-primary', 'placeholder': 'Ingrese su apellido' }),
            'fecha_ingreso': forms.TextInput(attrs={ 'type': 'date', 'class': 'form-control border border-primary datetimepicker' }),
            'email_persona1': forms.EmailInput(attrs={ 'class': 'form-control border border-primary', 'placeholder': 'Ingrese su correo electrónico' }),
            'email_persona2': forms.EmailInput(attrs={ 'class': 'form-control border border-primary', 'placeholder': 'Ingrese su correo electrónico' }),
            'fecha_nacimiento': forms.TextInput(attrs={ 'type': 'date', 'class': 'form-control border border-primary datetimepicker' }),
            'direccion_persona': forms.TextInput(attrs={ 'class': 'form-control border border-primary', 'placeholder': 'Ingrese su dirección' }),
            'id_pais_telefono': forms.Select(attrs={ 'class': 'form-select border border-primary' }),
            'telefono_persona': forms.TextInput(attrs={ 'class': 'form-control border border-primary', 'placeholder': 'Ingrese su número de teléfono' }),
            'id_pais_telefmov1': forms.Select(attrs={ 'class': 'form-select border border-primary' }),
            'telefmov_persona1': forms.TextInput(attrs={ 'class': 'form-control border border-primary', 'placeholder': 'Ingrese su número de celular' }),
            'id_pais_telefmov2': forms.Select(attrs={ 'class': 'form-select border border-primary' }),
            'telefmov_persona2': forms.TextInput(attrs={ 'class': 'form-control border border-primary', 'placeholder': 'Ingrese su número de celular 2' }),
            'ciudad_residencia': forms.TextInput(attrs={ 'class': 'form-control border border-primary', 'placeholder': 'Ingrese su ciudad' }),
            'id_pais_residencia': forms.Select(attrs={ 'class': 'form-select border border-primary', 'label': 'Código País' }),
            'codigo_postal': forms.TextInput(attrs={ 'class': 'form-control border border-primary', 'placeholder': 'Ingrese su código postal' }),
            'aeropuerto_cercano': forms.TextInput(attrs={ 'class': 'form-control border border-primary', 'placeholder': 'Ingrese su aeropuerto de origen' }),
            'id_pais_nacimiento': forms.Select(attrs={ 'class': 'form-select border border-primary' }),
            'id_pais_nacionalidad': forms.Select(attrs={ 'class': 'form-select border border-primary' }),
            'imagen_persona1': forms.ClearableFileInput(attrs={ 'class': 'form-control border border-primary' }),
            'imagen_persona2': forms.ClearableFileInput(attrs={ 'class': 'form-control border border-primary' }),
            'id_tipodoc_identidad': forms.Select(attrs={ 'class': 'form-select border border-primary' }),
            'nro_doc_identidad': forms.TextInput(attrs={ 'class': 'form-control border border-primary', 'placeholder': 'Ingrese número de documento de identidad' }),
            'id_pais_emision_doc': forms.Select(attrs={ 'class': 'form-select border border-primary' }),
            'fecha_emision_doc': forms.TextInput(attrs={ 'type': 'date', 'class': 'form-control border border-primary datetimepicker' }),
            'fecha_vencimiento_doc': forms.TextInput(attrs={ 'type': 'date', 'class': 'form-control border border-primary datetimepicker' }),
            'copia_doc_identidad': forms.ClearableFileInput(attrs={ 'class': 'form-control border border-primary' }),
            'id_profesion': forms.Select(attrs={ 'class': 'form-select border border-primary' }),
            'id_universidad': forms.Select(attrs={ 'class': 'form-select border border-primary' }),
            'descripcion_profesional': forms.Textarea(attrs={ 'class': 'form-control border border-primary', 'placeholder': 'Describa su experiencia' }),
            'doc_carga_cv': forms.ClearableFileInput(attrs={ 'class': 'form-control border border-primary' }),
            'link_video_cv': forms.URLInput(attrs={ 'class': 'form-control border border-primary', 'placeholder': 'Ingrese enlace del video de su curriculum' }),
        }
