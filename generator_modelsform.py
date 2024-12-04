import importlib.util
import os

def load_structure(module_path):
    module_name = os.path.splitext(os.path.basename(module_path))[0]
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.fields_modelsform

def generate_modelform(model_name, structure_file, model_output_file, form_output_file):
    fields = load_structure(structure_file)
    
    # Generar contenido del modelo
    model_template = ""
    for field in fields:
        name = field["name"]
        type_model = field["type_model"]
        args_model = field["args_model"]
        model_template += f"    {name} = models.{type_model}({args_model})\n"

    # Escribir el archivo del modelo
    with open(model_output_file, 'w', encoding='utf-8') as f:
        f.write("from django.db import models\n")
        f.write("from apps.maestros.models.models_base_gen import ModeloBaseGenerico\n")
        f.write("from apps.maestros.models.models_base import *\n")
        f.write("from .utils import custom_upload_to, upload_to_persona\n\n")
        f.write(f"class {model_name}(ModeloBaseGenerico):\n")
        f.write(model_template)
        f.write("\n    def __str__(self):\n")
        f.write(f"        return self.nombre_persona\n\n")
        f.write("    class Meta:\n")
        f.write("        db_table = 'personal'\n")
    
    # Generar contenido del formulario
    form_template = f"class {model_name}Form(forms.ModelForm):\n\n"
    form_template += "    class Meta:\n"
    form_template += f"        model = {model_name}\n"
    form_template += "        fields = '__all__'\n"
    form_template += "        widgets = {\n"

    for field in fields:
        if field["type_widget"]:
            name = field["name"]
            type_widget = field["type_widget"]
            attrs = field["attrs"]
            attrs_str = ', '.join([f"'{k}': '{v}'" for k, v in attrs.items()])
            form_template += f"            '{name}': forms.{type_widget}(attrs={{ {attrs_str} }}),\n"

    form_template += "        }\n"

    # Escribir el archivo del formulario
    with open(form_output_file, 'w', encoding='utf-8') as f:
        f.write("from django import forms\n")
        f.write("from django.core.exceptions import ValidationError\n")
        f.write(f"from ..models.models_{model_name.lower()} import {model_name}\n\n")
        f.write(form_template)

# Ejemplo de uso
generate_modelform("Persona", "estructura_modeloform.py", "models_generado.py", "forms_generado.py")
