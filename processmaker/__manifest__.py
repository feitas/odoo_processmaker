{
    'name': "BPM - ProcessMaker Integration",
    'summary': """
        BPM - ProcessMaker""",

    'description': """
         With this module you can manage :
         
         - Process through ProcessMaker
         
    """,
    'license': 'LGPL-3',
    'author': "Feitas",
    'website': "https://www.wffeitas.com",


    'category': 'project',
    'version': '16.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['web', 'mail'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/actions.xml',

        # 'views/assets.xml',
        'views/menu_actions.xml',
        'views/process_views.xml',
        'views/request_views.xml',
        'views/task_views.xml',
        'views/res_config_settings_views.xml',
        # 'views/views.xml',
        # 'views/process_views.xml',
        # 'views/dynamice_views.xml',
    ],
    'qweb': [
    ],
    'assets': {
        'web.assets_backend': [
            'processmaker/static/src/js/*',
        ],
    },
    'installable': True,
    'application': True,
}
