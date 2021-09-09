# -*- coding: utf-8 -*-
{
    'name': "Business Rule Action",
    'summary': """
        This module helps you the view according to the decided domain on click of record""",

    'description': """
        This module helps you the view according to the decided domain on click of record
    """,
    'author': "Ksolves India Ltd.",
    'website': "https://www.ksolves.com/",
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/configuration_to_open_view.xml',
        'views/assets.xml',
    ],
}
