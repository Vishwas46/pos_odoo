# -*- coding: utf-8 -*-
{
    'name': "POS Delivery Base",
    'version': '1.0',
    'summary': "Base models and logic for POS delivery integrations.",
    'description': """
        Provides shared functionality or data structures for integrating
        various delivery platforms (Lieferando, Wolt, etc.) into the POS.
    """,
    'category': 'Point of Sale',
    'author': 'Your Company Name',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'point_of_sale',
    ],
    'data': [
        # Add security rules, views, etc. later
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}