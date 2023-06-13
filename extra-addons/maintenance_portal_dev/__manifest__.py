# -*- coding: utf-8 -*-
{
    "name": "maintenance_portal_dev",
    "summary": """
        Modulo CRM para la gestión de visitas""",
    "description": """
        Modulo CRM para la gestión de visitas...
    """,
    "author": "Beitech",
    "website": "http://www.beitechcom",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Maintenance",
    "version": "0.1",
    # any module necessary for this one to work correctly
    "depends": ["base", "maintenance"],
    # always loaded
    "data": [
        # 'security/ir.model.access.csv',
        "views/views.xml",
        "views/templates.xml",
    ],
    # only loaded in demonstration mode
    "demo": [
        "demo/demo.xml",
    ],
    "application": False,
}
