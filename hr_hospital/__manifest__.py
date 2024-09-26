{
    'name': 'Hospital Management',
    'version': '17.0.1.0.0',
    'summary': 'Manage your hospital',
    'category': 'Human Resources',
    'author': 'Oleksandr Panchenko',
    'website': 'https://odoo.school',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/doctor_views.xml',
        'views/patient_views.xml',
        'views/disease_views.xml',
        'views/visit_views.xml',
        'views/diagnosis_views.xml',
        'views/menu.xml',
        'data/person_data.xml',
        'data/disease_data.xml',
        'data/visit_data.xml',
        'data/cron_jobs.xml',
        'wizards/disease_report_views.xml',
        'wizards/doctor_reassign_wizard_views.xml',
    ],
    'demo': [
        'demo/demo_data.xml',
        'demo/diagnosis_demo_data.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
