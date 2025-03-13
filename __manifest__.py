{
    'name': 'Equipment Register',
    'version': '1.0',
    'category': 'Tools',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'security/equipment_security.xml',
        'views/equipment_views.xml',
        'wizard/equipment_filter_views.xml'
    ],
    'installable': True,
    'auto_install': False,
}