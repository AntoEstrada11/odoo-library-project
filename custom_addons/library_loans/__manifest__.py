{
    'name': 'Biblioteca: Préstamos',
    'version': '19.0.1.0.0',
    'depends': ['library_books', 'base'],
    'data': [
        'security/ir.model.access.csv',
        'views/loan_views.xml'
    ],
    'installable': True,
    'application': True,
}