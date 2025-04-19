# -*- coding: utf-8 -*-
{
    'name': "POS Wolt Integration",
    'version': '1.0',
    'summary': "Integrates Wolt orders into the Odoo Point of Sale.",
    'description': """
        - Fetches new orders from Wolt API.
        - Allows viewing and managing Wolt orders within the POS interface.
        - Updates order status back to Wolt.
        - Requires configuration with Wolt API credentials.
    """,
    'author': "Your Company Name",
    'website': "https://www.yourcompany.com",
    'category': 'Point of Sale',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'point_of_sale',
        # 'pos_delivery_base', # Uncomment later if this module uses the base delivery logic
    ],
    'data': [
        # Add security rules, views, etc. later
        # 'security/ir.model.access.csv',
        # 'views/pos_config_views.xml', # Example: Add settings to POS config
    ],
    'assets': {
        # Add JS/XML assets later if needed for UI changes
        # 'point_of_sale.assets': [
        #     'pos_wolt_integration/static/src/js/**/*.js',
        #     'pos_wolt_integration/static/src/xml/**/*.xml',
        # ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}