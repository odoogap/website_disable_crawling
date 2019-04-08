# -*- coding: utf-8 -*-
{
    'name': 'Website Disable Crawling',
    'version': '11.0.1.0',
    'author': 'OdooGap',
    'summary': 'Disables Crawling',
    'description': """
This module provides two ways to disable crawling:
- Set a config parameter to disable crawling globally for every website;
- Disable crawling in the website configuration to disable crawling for a specific website.
""",
    'category': 'Website',
    'depends': ['website'],
    'data': [
        'data/ir_config_parameter_data.xml',
        'views/website_templates.xml',
        'views/website_views.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
