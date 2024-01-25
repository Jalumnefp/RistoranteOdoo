# -*- coding: utf-8 -*-
{
    'name': "Ristorante",
    'summary': "Este módulo es un trabajo de sge para administrar un restaurante",
    'description': """
        Este módulo te permite manejar todos aspectos de un restaurante. Como por ejemplo el personal, los clientes, los menús, las reservas, los platos, las mesas, etc. El objetivo es aplicar todo lo que hemos aprendido en la asignatura hasta el momento y crear un módulo com distintas funcionalidades.
    """,
    'author': "Sekiro Team",
    'website': "https://www.yourcompany.com",
    'category': 'Administration',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'demo': ['demo/demo.xml',],
}
