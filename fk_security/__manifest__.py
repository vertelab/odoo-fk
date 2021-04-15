{
    "name": "Fk Security",
    "version": "13.0.1.0.1",
    "author": "Vertel AB",
    "maintainer": "Vertel AB",
    "contributor": "Vertel AB",
    "license": "AGPL-3",
    "website": "https://vertel.se/",
    "category": "Extra Rights",
    "description": """
Fk Security \n
======================================================\n
This module adds secuirty groups in Odoo to make it \n
behave according to the requirements by Fk. \n
v13.0.1.0.1 - 1,008 Added the module to the repo \n
""",
    "depends": [
        "project_status",
        "project_milestone"
    ],
    "external_dependencies": [
    ],
    "data": [
        'data/res_groups.xml',
        'data/ir_ui_menu.xml',
        'data/ir_rule.xml',
        'security/ir.model.access.csv'
    ],
    "application": False,
    "installable": True,
}
