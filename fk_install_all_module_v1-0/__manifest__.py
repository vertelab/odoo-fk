{
    "name": "Fk Template Module",
    "version": "13.0.1.0.2",
    "author": "Vertel AB",
    "maintainer": "Vertel AB",
    "contributor": "Vertel AB",
    "license": "AGPL-3",
    "website": "https://vertel.se/",
    "category": "Tools",
    "description": """
Test Module \n
======================================================\n
Hover over fields to se a brief description of them \n
For more information make sure you are in debug mode \n
v13.0.1.0.1 - AFC-123 Added the module to the repo \n
Repositories\n
13.0.1.0.2 - PEP-8 refactoring.
https://github.com/muk-it/muk_base
https://github.com/muk-it/muk_web
https://github.com/odoo/odoo \n
https://github.com/OCA/account-financial-tools \n
https://github.com/OCA/project/ \n
https://github.com/OCA/timesheet \n
https://github.com/vertelab/odoo-fk
https://github.com/vertelab/odoo-l10n_se/
https://github.com/vertelab/odoo-project_scrum
https://github.com/vertelab/odoo-user-mail/

""",
    "depends": [
        "account",
        "auth_admin",  # Using admin_passwd from /etc/odoo/openerp-server.conf as password for admin
        "calendar",
        "contacts",
        "hr",
        "hr_holidays",
        "hr_skills",
        "mail",
        "muk_web_theme",  # Theme for Fk
        "note",
        "project",  # Odoo S.A.
        "hr_timesheet_sheet_policy_project_manager",  # CorporateHub, Odoo Community Association (OCA)
        "project_category",  # ADHOC SA,Tecnativa, Onestein, Odoo Community Association (OCA)
        "project_deadline",  # Onestein, Odoo Community Association (OCA)
        "project_description",  # Tecnativa, C2i Change 2 improve, Odoo Community Association (OCA)
        "project_hr",  # Tecnativa,Odoo Community Association (OCA)
        "project_list",  # CorporateHub, Odoo Community Association (OCA)
        "project_milestone",  # Patrick Wilson, Odoo Community Association (OCA)
        "project_parent_task_filter",  # C2i Change 2 improve, Odoo Community Association (OCA)
        # "project_scrum_portfolio", # Manages Project Portfolio
        "project_stage_closed",  # ACSONE SA/NV,Tecnativa,Odoo Community Association (OCA)
        "project_stage_state",  # Daniel Reis, Odoo Community Association (OCA)
        "project_status",  # Patrick Wilson, Odoo Community Association (OCA)
        "project_task_add_very_high",  # Onestein, Odoo Community Association (OCA)
        "project_task_dependency",  # Onestein,Odoo Community Association (OCA)
        "project_task_pull_request",  # SMDrugstore, Tecnativa, Odoo Community Association (OCA)
        "project_task_report",  # Eficent, Odoo Community Association (OCA)
        "project_task_timesheet_report",  # Jarsa, Odoo Community Association (OCA)
        "project_timeline",  # Tecnativa, Onestein, Odoo Community Association (OCA)
        "project_timeline_hr_timesheet",  # Onestein, Odoo Community Association (OCA)
        "project_timeline_task_dependency",  # Onestein, Odoo Community Association (OCA)
        "project_timesheet_holidays",  # Odoo S.A.
        "sale_management",
        "snippet_addons",
        "survey",
        "website"
    ],
    "external_dependencies": [
    ],
    "data": [
        'views/res_partner.xml',
        'security/ir.model.access.csv'
    ],
    "application": False,
    "installable": True,
}
