[
    {
        "name": "estatus_persona",
        "type_model": "BooleanField",
        "args_model": "\"Estatus\", default=True, choices=[(True, 'Activo'), (False, 'Inactivo')]",
        "type_widget": "Select",
        "attrs": {"class": "form-select border border-primary", "label": "*ESTATUS"},
        "section": "Información Personal",
        "row": 1,
        "cols": 4,
        "observations": "Indica si la persona está activa o inactiva."
    },
    {
        "name": "nombre_persona",
        "type_model": "CharField",
        "args_model": "\"Nombres\", max_length=60, null=True, blank=True",
        "type_widget": "TextInput",
        "attrs": {"class": "form-control border border-primary", "placeholder": "Ingrese su nombre"},
        "section": "Información Personal",
        "row": 1,
        "cols": 2,
        "observations": "Nombre completo de la persona."
    },
    {
        "name": "apellido_persona",
        "type_model": "CharField",
        "args_model": "\"Apellidos\", max_length=60, null=True, blank=True",
        "type_widget": "TextInput",
        "attrs": {"class": "form-control border border-primary", "placeholder": "Ingrese su apellido"},
        "section": "Información Personal",
        "row": 1,
        "cols": 4,
        "observations": "Apellido completo de la persona."
    },
    {
        "name": "fecha_ingreso",
        "type_model": "DateField",
        "args_model": "\"Fecha Ingreso\", null=True, blank=True",
        "type_widget": "TextInput",
        "attrs": {"type": "date", "class": "form-control border border-primary datetimepicker"},
        "section": "Información Personal",
        "row": 1,
        "cols": 2,
        "observations": "Fecha en la que la persona ingresó."
    },
    {
        "name": "imagen_pasaporte1",
        "type_model": "ImageField",
        "args_model": "upload_to=upload_to_persona, null=True, blank=True",
        "type_widget": "FileInput",
        "attrs": {"class": "form-control border border-primary", "accept": "image/*"},
        "section": "Imágenes del pasaporte",
        "row": 1,
        "cols": 6,
        "observations": "Imagen del pasaporte de la persona."
    },
    {
        "name": "imagen_pasaporte2",
        "type_model": "ImageField",
        "args_model": "upload_to=upload_to_persona, null=True, blank=True",
        "type_widget": "FileInput",
        "attrs": {"class": "form-control border border-primary", "accept": "image/*"},
        "section": "Imágenes del pasaporte",
        "row": 1,
        "cols": 6,
        "observations": "Otra imagen del pasaporte de la persona."
    },
    {
        "name": "estatura",
        "type_model": "FloatField",
        "args_model": "\"Estatura\", null=True, blank=True",
        "type_widget": "TextInput",
        "attrs": {"class": "form-control border border-primary", "placeholder": "Ingrese su estatura en metros"},
        "section": "Apariencia personal y tallas",
        "row": 1,
        "cols": 3,
        "observations": "Estatura de la persona en metros."
    },
    {
        "name": "peso",
        "type_model": "FloatField",
        "args_model": "\"Peso\", null=True, blank=True",
        "type_widget": "TextInput",
        "attrs": {"class": "form-control border border-primary", "placeholder": "Ingrese su peso en kilogramos"},
        "section": "Apariencia personal y tallas",
        "row": 1,
        "cols": 3,
        "observations": "Peso de la persona en kilogramos."
    },
    {
        "name": "talla_tshirt",
        "type_model": "CharField",
        "args_model": "\"Talla de camiseta\", max_length=10, null=True, blank=True",
        "type_widget": "TextInput",
        "attrs": {"class": "form-control border border-primary", "placeholder": "Ingrese su talla de camiseta"},
        "section": "Apariencia personal y tallas",
        "row": 1,
        "cols": 2,
        "observations": "Talla de camiseta de la persona."
    },
    {
        "name": "talla_coverall",
        "type_model": "CharField",
        "args_model": "\"Talla de coverall\", max_length=10, null=True, blank=True",
        "type_widget": "TextInput",
        "attrs": {"class": "form-control border border-primary", "placeholder": "Ingrese su talla de coverall"},
        "section": "Apariencia personal y tallas",
        "row": 1,
        "cols": 2,
        "observations": "Talla de coverall de la persona."
    },
    {
        "name": "talla_pantalon",
        "type_model": "CharField",
        "args_model": "\"Talla de pantalón\", max_length=10, null=True, blank=True",
        "type_widget": "TextInput",
        "attrs": {"class": "form-control border border-primary", "placeholder": "Ingrese su talla de pantalón"},
        "section": "Apariencia personal y tallas",
        "row": 1,
        "cols": 2,
        "observations": "Talla de pantalón de la persona."
    },
    {
        "name": "nombre_apellidos_contacto",
        "type_model": "CharField",
        "args_model": "\"Nombre y apellidos\", max_length=100, null=True, blank=True",
        "type_widget": "TextInput",
        "attrs": {"class": "form-control border border-primary", "placeholder": "Ingrese el nombre y apellidos del contacto"},
        "section": "Información en caso de emergencia",
        "row": 1,
        "cols": 8,
        "observations": "Nombre y apellidos del contacto de emergencia."
    },
    {
        "name": "parentesco",
        "type_model": "CharField",
        "args_model": "\"Parentesco\", max_length=50, null=True, blank=True",
        "type_widget": "TextInput",
        "attrs": {"class": "form-control border border-primary", "placeholder": "Ingrese el parentesco del contacto"},
        "section": "Información en caso de emergencia",
        "row": 2,
        "cols": 4,
        "observations": "Parentesco del contacto de emergencia."
    },
   
]