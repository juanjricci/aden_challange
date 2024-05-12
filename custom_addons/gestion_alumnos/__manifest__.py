{
    'name': "Gestion de Alumnos",
    'version': '1.0.0',
    'depends': ['base'],
    'author': "Juan Ricci",
    'category': 'Administration',
    'description': """
    Este es un módulo de gestión de alumnos
    """,
    # data files always loaded at installation
    'data': [
        'views/alumno_view.xml',
        'views/programas_view.xml',
        'views/inscripciones_view.xml',
        'security/ir.model.access.csv',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        # 'demo/demo_data.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
}