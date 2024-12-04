from django.db.models import Q

fields = ["nombre_persona", "apellido_persona", "nro_doc_identidad"]
query = "Per"  # Supongamos que `query` es el término de búsqueda

# Construir las expresiones Q dinámicamente
queries = [Q(**{f"{field}__icontains": query}) for field in fields]

print(queries)