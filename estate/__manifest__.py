{
    "name": "Estate",  # The name that will appear in the App list
    "version": "16.0.0",  # Version
    "application": True,  # This line says the module is an App, and not a module
    "depends": ["base"],  # dependencies
    "data": [
        'security/ir.model.access.csv',
        'views/views.xml',  # Archivo con las vistas y acciones
        'views/menu.xml',   # Archivo con el menú        

    ],
    "installable": True,
    'license': 'LGPL-3',
}
