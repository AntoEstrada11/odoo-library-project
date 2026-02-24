{
    'name': 'Gestión de Biblioteca',
    'summary': 'Módulo central para administración de libros',
    'version': '19.0.1.0.0',
    'category': 'Services/Library',
    'author': 'Tu Nombre',
    'license': 'LGPL-3',
    'depends': ['base'],  # 'base' es el núcleo de Odoo
    'data': [
        'security/ir.model.access.csv',
        'views/library_book_views.xml',
    ],
    'application': True,  # Permite que aparezca como App principal en el menú
    'installable': True,
}