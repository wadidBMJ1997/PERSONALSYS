# D:\HL_PROJECT\PERSONALSYS\apps\maestros\forms\persona_forms.py
from django import forms
from ..models.persona_models import Persona
from django.core.exceptions import ValidationError
from diseno_base.diseno_bootstrap import (
    formclasstext, formclassselect,
    formclassdate, formclasstextplain)

class PersonaForm(forms.ModelForm):
    
    class Meta:
        model = Persona
        fields = '__all__'
        
        widgets = {
            # Información Personal
            'estatus_persona': 
                forms.Select(attrs={**formclassselect}),

            # Código de Personal
            'codigo_persona': 
                forms.TextInput(attrs={**formclasstextplain,
                                       'readonly': 'readonly'}),    
            
            # Información Personal
            'nombre_persona': 
                forms.TextInput(attrs={**formclasstext, 
                                       'placeholder': 'Ingrese su nombre',}),
            'apellido_persona': 
                forms.TextInput(attrs={**formclasstext,
                                       'placeholder': 'Ingrese su apellido'}),
            'fecha_ingreso': 
                forms.TextInput(attrs={**formclassdate, "type": 'date'}),
            'email_persona1': 
                forms.EmailInput(attrs={**formclasstext, 
                                        'placeholder': 'Ingrese su correo electrónico'}),
            'email_persona2': 
                forms.EmailInput(attrs={**formclasstext, 
                                        'placeholder': 'Ingrese su correo electrónico'}),
            'fecha_nacimiento': 
                forms.TextInput(attrs={**formclassdate, "type": 'date'}),
            'direccion_persona': 
                forms.TextInput(attrs={**formclasstext, 
                                       'placeholder': 'Ingrese su dirección'}),
            'id_pais_telefono': 
                forms.Select(attrs={**formclassselect}),
            'telefono_persona': 
                forms.TextInput(attrs={**formclasstext, 
                                       'placeholder': 'Ingrese su número de teléfono'}),
            'id_pais_telefmov1': 
                forms.Select(attrs={**formclassselect}),
            'telefmov_persona1': 
                forms.TextInput(attrs={**formclasstext, 
                                       'placeholder': 'Ingrese su número de celular'}),
            'id_pais_telefmov2': 
                forms.Select(attrs={**formclassselect}),
            'telefmov_persona2': 
                forms.TextInput(attrs={**formclasstext, 
                                       'placeholder': 'Ingrese su número de celular 2'}),
            'ciudad_residencia': 
                forms.TextInput(attrs={**formclasstext, 
                                       'placeholder': 'Ingrese su ciudad'}),
            'id_pais_residencia': 
                forms.Select(attrs={**formclassselect}),
            'codigo_postal': 
                forms.TextInput(attrs={**formclasstext, 
                                       'placeholder': 'Ingrese su código postal'}),
            'aeropuerto_cercano': 
                forms.TextInput(attrs={**formclasstext, 
                                       'placeholder': 'Ingrese su aeropuerto de origen'}),
            'id_pais_nacimiento': 
                forms.Select(attrs={**formclassselect}),
            'id_pais_nacionalidad': 
                forms.Select(attrs={**formclassselect}),
            'id_pais_otranacional': 
                forms.Select(attrs={**formclassselect}),

            # Imágenes de la persona
            'imagen_persona1': 
                forms.ClearableFileInput(attrs={**formclasstext}),
            'imagen_persona2': 
                forms.ClearableFileInput(attrs={**formclasstext}),
            
            # Pasaporte, Visa y Documentos de Viaje
            'id_tipodoc_identidad': 
                forms.Select(attrs={**formclassselect}),
            'nro_doc_identidad': 
                forms.TextInput(attrs={**formclasstext, 
                                       'placeholder': 
                                           'Ingrese número de documento de identidad'}),
            'id_pais_emision_doc': 
                forms.Select(attrs={**formclassselect}),
            'fecha_emision_doc': 
                forms.TextInput(attrs={'type':'date', **formclassdate}),
            'fecha_vencimiento_doc': 
                forms.TextInput(attrs={"type": 'date', **formclassdate}),
            'observaciones_documento_id': 
                forms.TextInput(attrs={**formclasstext,
                                       'placeholder': 
                                           'Observaciones del documento de identidad'}),
            'id_pais_emision_visa1': 
                forms.Select(attrs={**formclassselect}),
            'fecha_emision_visa1': 
                forms.TextInput(attrs={'type':'date', **formclassdate}),
            'fecha_vencimiento_visa1': 
                forms.TextInput(attrs={'type':'date', **formclassdate}),
            'tipo_visa1': 
                forms.Select(attrs={**formclassselect}),

            'id_pais_emision_visa2': 
                forms.Select(attrs={**formclassselect}),
            'fecha_emision_visa2': 
                forms.TextInput(attrs={'type':'date', **formclassdate}),
            'fecha_vencimiento_visa2': 
                forms.TextInput(attrs={'type':'date', **formclassdate}),
            'tipo_visa2': 
                forms.TextInput(attrs={**formclasstext,
                                       'placeholder': 'Tipo Visa'}),
            
            # Imágenes del pasaporte
            'imagen_pasaporte1': 
                forms.ClearableFileInput(attrs={**formclasstext}),
            'imagen_pasaporte2': 
                forms.ClearableFileInput(attrs={**formclasstext}),
            
            # Imágenes de las visa americana
            'imagen_visa1':
                forms.ClearableFileInput(attrs={**formclasstext}),
            'imagen_visa2': 
                forms.ClearableFileInput(attrs={**formclasstext}),

            # Imágenes de otras visas
            'imagen_visa3':
                forms.ClearableFileInput(attrs={**formclasstext}),
            'imagen_visa4': 
                forms.ClearableFileInput(attrs={**formclasstext}),
            
            # Especialidades
            'id_especialidad1': forms.Select(attrs={**formclassselect}),
            'institucion_especialidad1':forms.TextInput(
                attrs={**formclasstext, 
                       'placeholder': 'Institución Educativa'}),
            'fecha_ini_especialidad1': forms.TextInput(
                attrs={'type':'date', **formclassdate}),
            'anhos_especialidad1': forms.NumberInput(
                attrs={**formclasstext, 'placeholder': 'Años'}),
            'observacion_especialidad1': forms.TextInput(
                attrs={**formclasstext, 
                       'placeholder': 'Observación Especialidad 1'}),
            'id_especialidad2': forms.Select(
                attrs={**formclassselect}),
            'institucion_especialidad2':forms.TextInput(
                attrs={**formclasstext, 
                       'placeholder': 'Institución Educativa'}),
            'fecha_ini_especialidad2': forms.TextInput(
                attrs={'type':'date', **formclassdate}),
            'anhos_especialidad2': forms.NumberInput(
                attrs={**formclasstext, 'placeholder': 'Años'}),
            'observacion_especialidad2': forms.TextInput(
                attrs={**formclasstext, 
                       'placeholder': 'Observación Especialidad 2'}),
            
            # Imágenes de Certificaciones de Especialización          
            'imagen_certificacion1': 
                forms.ClearableFileInput(attrs={**formclasstext}),
            'imagen_certificacion2': 
                forms.ClearableFileInput(attrs={**formclasstext}),
            'imagen_certificacion3': 
                forms.ClearableFileInput(attrs={**formclasstext}),
            'imagen_certificacion4': 
                forms.ClearableFileInput(attrs={**formclasstext}),
            'imagen_certificacion5': 
                forms.ClearableFileInput(attrs={**formclasstext}),
            'imagen_certificacion6': 
                forms.ClearableFileInput(attrs={**formclasstext}),
            'imagen_certificacion7': 
                forms.ClearableFileInput(attrs={**formclasstext}),
            'imagen_certificacion8': 
                forms.ClearableFileInput(attrs={**formclasstext}),

            'pdf_certificacion1': 
                forms.ClearableFileInput(attrs={**formclasstext, 
                                                'accept': 'application/pdf'}),
            'pdf_certificacion2': 
                forms.ClearableFileInput(attrs={**formclasstext, 
                                                'accept': 'application/pdf'}),
            'pdf_certificacion3': 
                forms.ClearableFileInput(attrs={**formclasstext, 
                                                'accept': 'application/pdf'}),
            'pdf_certificacion4': 
                forms.ClearableFileInput(attrs={**formclasstext, 
                                                'accept': 'application/pdf'}),
            'pdf_certificacion5': 
                forms.ClearableFileInput(attrs={**formclasstext, 
                                                'accept': 'application/pdf'}),
            'pdf_certificacion6': 
                forms.ClearableFileInput(attrs={**formclasstext, 
                                                'accept': 'application/pdf'}),
            'pdf_certificacion7': 
                forms.ClearableFileInput(attrs={**formclasstext, 
                                                'accept': 'application/pdf'}),
            'pdf_certificacion8': 
                forms.ClearableFileInput(attrs={**formclasstext, 
                                                'accept': 'application/pdf'}),

            # Referencias Laborales
            'empresa_trabajo1': forms.TextInput(
                attrs={**formclasstext, 
                       'placeholder': 'Empresa'}),
            'fecha_ini_empresa1': forms.TextInput(
                attrs={'type':'date', **formclassdate}),
            'fecha_fin_empresa1': forms.TextInput(
                attrs={'type':'date', **formclassdate}),
            'contacto_empresa1':forms.TextInput(
                attrs={**formclasstext, 
                       'placeholder': 'Contacto'}),
            'email_contacto1':forms.TextInput(
                attrs={**formclasstext, 
                       'placeholder': 'e-mail'}),
            'id_pais_contacto1': forms.Select(attrs={**formclassselect}),
            'telefono_contacto1':forms.TextInput(
                attrs={**formclasstext, 
                       'placeholder': 'Telefono'}),

            'empresa_trabajo2': forms.TextInput(
                attrs={**formclasstext, 
                       'placeholder': 'Empresa'}),
            'fecha_ini_empresa2': forms.TextInput(
                attrs={'type':'date', **formclassdate}),
            'fecha_fin_empresa2': forms.TextInput(
                attrs={'type':'date', **formclassdate}),
            'contacto_empresa2':forms.TextInput(
                attrs={**formclasstext, 
                       'placeholder': 'Contacto'}),
            'email_contacto2':forms.TextInput(
                attrs={**formclasstext, 
                       'placeholder': 'e-mail'}),
            'id_pais_contacto2': forms.Select(attrs={**formclassselect}),
            'telefono_contacto2':forms.TextInput(
                attrs={**formclasstext, 
                       'placeholder': 'Telefono'}),
            
            'empresa_trabajo3': forms.TextInput(
                attrs={**formclasstext, 
                       'placeholder': 'Empresa'}),
            'fecha_ini_empresa3': forms.TextInput(
                attrs={'type':'date', **formclassdate}),
            'fecha_fin_empresa3': forms.TextInput(
                attrs={'type':'date', **formclassdate}),
            'contacto_empresa3':forms.TextInput(
                attrs={**formclasstext, 
                       'placeholder': 'Contacto'}),
            'email_contacto3':forms.TextInput(
                attrs={**formclasstext, 
                       'placeholder': 'e-mail'}),
            'id_pais_contacto3': forms.Select(attrs={**formclassselect}),
            'telefono_contacto3':forms.TextInput(
                attrs={**formclasstext, 
                       'placeholder': 'Telefono'}),
            
            # Información Bancaria
            'id_banco': forms.Select(attrs={**formclassselect}),
            'cuenta_bancaria': forms.TextInput(
                attrs={**formclasstext, 
                       'placeholder': 'Número de Cuenta'}),
            'titular_cuenta_bancaria': forms.TextInput(
                attrs={**formclasstext, 
                       'placeholder': 'Titular de la Cuenta'}),
            'codigo_swift': forms.TextInput(
                attrs={**formclasstext, 
                       'placeholder': 'Código SWiFT'}),
            'id_pais_banco': forms.Select(attrs={**formclassselect}),
            'direccion_banco': forms.TextInput(
                attrs={**formclasstext, 
                       'placeholder': 'Dirección del Banco'}),
            'codigo_postal_banco': forms.TextInput(
                attrs={**formclasstext, 
                       'placeholder': 'Código Postal'}),
            'observaciones_cuenta': forms.TextInput(
                attrs={**formclasstext, 
                       'placeholder': 'Observaciones'}),
            'ciudad_banco': forms.TextInput(
                attrs={**formclasstext, 
                       'placeholder': 'Ciudad'}),
            'codigo_corto_banco': forms.TextInput(
                attrs={**formclasstext, 
                       'placeholder': 'Código del Banco'}),
            
            # Proyectos con nosotros

            # Historial de Accidentes
            
            # Apariencia Personal 
            'estatura': 
                forms.NumberInput(attrs={**formclasstext, 
                                         'placeholder': 'Ingrese su estatura'}),
            'peso': forms.NumberInput(attrs={**formclasstext, 
                                             'placeholder': 'Ingrese su peso'}),

            'talla_tshirt': 
                forms.Select(attrs={**formclassselect}),
            'talla_coverall': 
                forms.Select(attrs={**formclassselect}),
            'talla_pantalon': 
                forms.Select(attrs={**formclassselect}),

            # Información de Contacto en Caso de Emergencia
            'nombre_apellidos_contacto': 
                forms.TextInput(attrs={**formclasstext, 
                                       'placeholder': 
                                           'Ingrese nombres y apellidos de contacto'}),
            'id_parentesco': forms.Select(attrs={**formclassselect}),
            'id_pais_telefcont': 
                forms.Select(attrs={**formclassselect}),
            'telefono_contacto': 
                forms.TextInput(attrs={**formclasstext, 
                                       'placeholder': 
                                           'Ingrese teléfono de contacto'}),
            'email_contacto': 
                forms.EmailInput(attrs={**formclasstext, 
                                        'placeholder': 
                                            'Ingrese correo electrónico de contacto'}),
            
            # Black List            
            'estatus_black': 
                forms.Select(attrs={**formclassselect, 'label': '*ESTATUS'}),
            'fecha_black': 
                forms.TextInput(attrs={"type": 'date', **formclassdate}),                
            'motivo_black': 
                forms.Textarea(attrs={**formclasstext, 
                                      'placeholder': 
                                          'Ingrese observaciones sobre la persona'}),
            
            # Otros
            'fecha_cese': 
                forms.TextInput(attrs={"type": 'date', **formclassdate}),
            'observacion_cese': 
                forms.Textarea(attrs={**formclasstext, 
                                      'placeholder': 
                                          'Ingrese observaciones sobre la persona'}),
            
        }

