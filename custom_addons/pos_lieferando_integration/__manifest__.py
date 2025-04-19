# -*- coding: utf-8 -*-
{
    'name': "POS Lieferando Integration",
    'version': '1.0',
    'summary': """
        Integrates Lieferando (Just Eat Takeaway) orders into the Odoo Point of Sale.
    """,
    'description': """
        - Fetches new orders from Lieferando API.
        - Allows viewing and managing Lieferando orders within the POS interface.
        - Updates order status back to Lieferando.
        - Requires configuration with Lieferando API credentials.
    """,
    'author': "Your Company Name",
    'website': "https://www.yourcompany.com",
    'category': 'Point of Sale',
    'license': 'LGPL-3', # Or your chosen license

    # Dependencies: Base Odoo POS module is 'point_of_sale'. Add others as needed.
    'depends': [
        'point_of_sale',
        # 'pos_delivery_base', # Uncomment if you create the base delivery module
        # Add any other dependencies here (e.g., 'base', 'web', 'mail')
        ],

    # Data files always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/pos_config_views.xml', # Add settings to POS config
        'views/lieferando_order_views.xml', # Views for backend management if needed
        # Add other XML views here
    ],

    # Assets for the POS frontend
    'assets': {
        'point_of_sale.assets': [
            'pos_lieferando_integration/static/src/js/**/*.js',
            'pos_lieferando_integration/static/src/xml/**/*.xml', # OWL templates for UI
            'pos_lieferando_integration/static/src/css/**/*.css',
        ],
    },

    'installable': True,
    'application': False, # Typically integrations are not full 'applications'
    'auto_install': False,
}