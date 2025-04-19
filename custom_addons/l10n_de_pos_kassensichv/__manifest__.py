# -*- coding: utf-8 -*-
{
    'name': "German POS KassenSichV Integration Layer",
    'version': '1.0',
    'summary': "Placeholder for KassenSichV TSE Integration.",
    'description': """
        This module will contain the integration logic or dependencies
        for a certified KassenSichV TSE solution.
    """,
    'category': 'Point of Sale',
    'author': 'Your Company Name',
    'license': 'LGPL-3',
    'depends': [
        'base', # Almost all modules depend on base
        'point_of_sale',
        # Add the *actual* certified TSE module dependency here later
        # e.g., 'pos_fiskaly',
    ],
    'data': [
        # Add security rules, views, etc. later
        # 'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}