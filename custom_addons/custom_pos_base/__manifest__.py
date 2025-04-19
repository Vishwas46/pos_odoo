# -*- coding: utf-8 -*-
{
    'name': 'POS Custom Brand - Tavlo',
    'version': '1.0.0',
    'category': 'Point of Sale',
    'summary': 'Replaces POS logo and title for Tavlo branding.',
    'description': """
This module overrides the default Odoo Point of Sale branding
to display the Tavlo logo and name.
""",
    'author': 'Your Name',
    'website': 'https://your.website.com',
    'license': 'LGPL-3',
    'depends': [
        'point_of_sale',
    ],
    # we no longer have any legacy <data> to import
    'data': [],
    # instead we inject our QWeb into the POS asset bundle
    'assets': {
        'point_of_sale.assets_qweb': [
            'custom_pos_base/static/src/xml/custom_templates.xml',
        ],
    },
    'images': [
        'static/description/QuantEraAI.png',
    ],
    'icon': 'static/description/QuantEraAI.png',
    'installable': True,
    'application': False,
    'auto_install': False,
}