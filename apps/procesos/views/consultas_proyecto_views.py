from django.http import JsonResponse
from django.db.models import Q
from django.db.models import F
from ...maestros.models.persona_models import Persona
import json

def buscar_persona(request):
    busqueda = request.GET.get('busqueda', '')

    # Construir filtros dinámicos basados en el parámetro de búsqueda
    personas = Persona.objects.all()

    if busqueda:
        personas = personas.filter(
            Q(codigo_persona__icontains=busqueda) |
            Q(apellido_persona__icontains=busqueda) |
            Q(id_especialidad1__nombre_especialidad__icontains=busqueda)
        )

    resultados = [
        {
            'codigo': persona.codigo_persona,
            'apellido': persona.apellido_persona,
            'nombre': persona.nombre_persona,
            'especialidad': persona.id_especialidad1.nombre_especialidad if persona.id_especialidad1 else '',
        }
        for persona in personas
    ]
    
    print('resultados', resultados)

    return JsonResponse(resultados, safe=False)
