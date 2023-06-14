{
    'name': 'Hospital Management',
    'version': '1.0.0',
    'category': 'Hospital',
    'sequence': -1,
    'author': 'Beitech',
    'summary': 'Hospital management system',
    'description': """
    Hospital management system
    """,
    'depends': ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/female_patient_view.xml',
        'views/appointment_view.xml',
    ],
    'demo': [],
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}