import json
import os
import django
import sys

# Añadir la ruta del proyecto al sys.path
sys.path.append("D:/HL_PROJECT/PERSONALSYS")

# Configura el entorno de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PERSONALSYS.settings")
django.setup()

from apps.maestros.models.base_models import Pais

# Ruta al archivo JSON
json_file_path = os.path.join('D:/HL_PROJECT/PERSONALSYS/data_load', 'pais.json')

# Leer el archivo JSON
with open(json_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Cargar los países
for pais_data in data:
    Pais.objects.update_or_create(
        id_pais=pais_data['id_pais'],
        defaults={
            'estatus_pais': pais_data['estatus_pais'],
            'codigo_iso2': pais_data['codigo_iso2'],
            'codigo_iso3': pais_data['codigo_iso3'],
            'nombre_pais': pais_data['nombre_pais'],
            'continente': pais_data['continente'],
            'region_continente': pais_data['region_continente'],
            'nombre_pais_ingles': pais_data['nombre_pais_ingles'],
            'nombre_pais_frances': pais_data['nombre_pais_frances'],
            'codigo_telefonico': pais_data['codigo_telefonico'],
        }
    )

# Mostrar los datos cargados
paises = Pais.objects.all()
for pais in paises:
    print(f"ID: {pais.id_pais}, Estatus: {pais.estatus_pais}, Código ISO2: {pais.codigo_iso2}, Nombre: {pais.nombre_pais}")

print("Datos cargados exitosamente!")
