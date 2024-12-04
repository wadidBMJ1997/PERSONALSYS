# Crear un diccionario de campos y sus valores 'col' y 'section'
col_dict = {
'Información Personal': {
    'nombre_persona': {'label': 'Nombres', 'col': 5},
    'apellido_persona': {'label': 'Apellidos', 'col': 5},
    'fecha_ingreso': {'label': 'Fecha Ingreso', 'col': 2},
    'email_persona1': {'label': 'e-MAIL principal', 'col': 5},
    'email_persona2': {'label': 'e-MAIL secundario', 'col': 5},
    'fecha_nacimiento': {'label': 'Fecha Nacim.', 'col': 2},
    'direccion_persona': {'label': 'Dirección', 'col': 12},
},
'Apariencia Personal y Tallas': {
    'id_color_cabello': {'label': 'Color de Cabello', 'col': 3},
    'id_color_ojos': {'label': 'Color de Ojos', 'col': 3},
    'estatura': {'label': 'Estatura (pies)', 'col': 3},
    'peso': {'label': 'Peso (libras)', 'col': 3},
    'talla_tshirt': {'label': 'Talla de TShirt', 'col': 4},
    'talla_coverall': {'label': 'Talla de Coverall', 'col': 4},
    'talla_pantalon': {'label': 'Talla de Pantalon', 'col': 4},
},
# ... Otras secciones
}

# Asignar cada campo a una sección del acordeón
sections = {
    'Información Personal': [
        {'field': 'nombre_persona', 'label': 'Nombres', 'row': 1, 'col': 5},
        {'field': 'apellido_persona', 'label': 'Apellidos', 'row': 1, 'col': 5},
        {'field': 'fecha_ingreso', 'label': 'Fecha Ingreso', 'row': 1, 'col': 2},
        {'field': 'email_persona1', 'label': 'e-MAIL principal', 'row': 2, 'col': 5},
        {'field': 'email_persona2', 'label': 'e-MAIL secundario', 'row': 2, 'col': 5},
        {'field': 'fecha_nacimiento', 'label': 'Fecha Nacim.', 'row': 2, 'col': 2},
        # ... Otros campos
    ],
    'Apariencia Personal y Tallas': [
        {'field': 'id_color_cabello', 'label': 'Color de Cabello', 'row': 1, 'col': 3},
        {'field': 'id_color_ojos', 'label': 'Color de Ojos', 'row': 1, 'col': 3},
        {'field': 'estatura', 'label': 'Estatura (pies)', 'row': 1, 'col': 3},
        {'field': 'peso', 'label': 'Peso (libras)', 'row': 1, 'col': 3},
        {'field': 'talla_tshirt', 'label': 'Talla de TShirt', 'row': 2, 'col': 4},
        {'field': 'talla_coverall', 'label': 'Talla de Coverall', 'row': 2, 'col': 4},
        {'field': 'talla_pantalon', 'label': 'Talla de Pantalón', 'row': 2, 'col': 4},
        # ... Otros campos
    ],
    'Información de Contacto en Caso de Emergencia': [
        {'field': 'nombre_apellidos_contacto', 'label': 'Nombre y Apellidos de Contacto', 'row': 1, 'col': 12},
        {'field': 'id_pais_telefcont', 'label': 'País Teléfono', 'row': 2, 'col': 4},
        {'field': 'telefono_contacto', 'label': 'Teléfono Contacto', 'row': 2, 'col': 4},
        {'field': 'email_contacto', 'label': 'e-Mail Contacto', 'row': 2, 'col': 4},
        # ... Otros campos
    ],
    # ... Otras secciones
}