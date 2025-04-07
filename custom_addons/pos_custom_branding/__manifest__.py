# -*- coding: utf-8 -*-
{
    'name': 'POS Custom Branding - Tavlo',
    'version': '1.0',
    'summary': 'Replaces POS logo and title for Tavlo branding.',
    'description': """
        This module overrides the default Odoo Point of Sale branding
        to display the Tavlo logo and name.
    """,
    'category': 'Point of Sale',
    'author': 'Your Name', # Optional: Change to your name/company
    'depends': ['point_of_sale'], # Crucial: Depends on the core POS module
    'data': [
        # If using 'data', Odoo loads this XML on module install/update
        # 'views/templates.xml', # Use this OR 'assets', not both for the same file
    ],
    'assets': {
        # 'assets' is often preferred for POS UI changes
        'point_of_sale.assets': [
            # Path relative to the module root
            'pos_custom_branding/static/src/img/QuantEraAI.png', # Make image available
            'pos_custom_branding/views/templates.xml', # Load your XML template overrides
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}