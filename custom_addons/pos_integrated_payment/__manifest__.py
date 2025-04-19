# -*- coding: utf-8 -*-
{
    'name': "POS Integrated Payment Enhancements",
    'version': '1.0',
    'summary': "Customizations for integrated payment flows in POS.",
    'description': """
        Adds specific workflows or UI elements to the Point of Sale
        for handling integrated payment terminals or gateways.
    """,
    'category': 'Point of Sale',
    'author': 'Your Company Name',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'point_of_sale',
        'payment', # Depends on Odoo's base payment module
    ],
    'assets': {
        # Add JS/XML assets later if needed for UI changes
        # 'point_of_sale.assets': [
        #     'pos_integrated_payment/static/src/js/**/*.js',
        #     'pos_integrated_payment/static/src/xml/**/*.xml',
        # ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}