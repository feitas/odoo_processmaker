# -*- coding: utf-8 -*-
# Copyright 2022 Feitas (https://www.wffeitas.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

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
    'version': '14.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['web'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        # 'datas/datas.xml',
        
        'views/assets.xml',
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
    'installable': True,
    'application': False,
}