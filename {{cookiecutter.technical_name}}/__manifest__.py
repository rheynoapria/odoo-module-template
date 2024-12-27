# -*- coding: utf-8 -*-
# Copyright {% now 'utc', '%Y' %} {{cookiecutter.author_name}}
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
# noinspection PyUnresolvedReferences,SpellCheckingInspection
{
    "name": """{{cookiecutter.name}}""",
    "summary": """{{cookiecutter.summary}}""",
    "category": "{{cookiecutter.category}}",
    "version": "{{cookiecutter.base_version}}.{{cookiecutter.version}}",
    "development_status": "Alpha",  # Options: Alpha|Beta|Production/Stable|Mature
    "auto_install": False,
    "installable": True,
    "application": {{cookiecutter.application}},
    "author": "{{cookiecutter.author_name}}",
    "support": "rheynoapria11@gmail.com",
    # "website": "{{cookiecutter.author_website}}",
    "license": "{{cookiecutter.license}}",
    # "images": [
    #     'images/main_screenshot.png'
    # ],

    # "price": 10.00,
    # "currency": "USD",

    "depends": [
        # odoo addons
        'base',
        # third party addons

        # developed addons
    ],
    "data": [
        # group
        # 'security/res_groups.xml',

        # data

        # global action
        # 'views/action/action.xml',

        # view
        # 'views/common/model_name.xml',

        # wizard
        # 'views/wizard/model_name.xml',

        # report paperformat
        # 'data/report_paperformat.xml',

        # report template
        # 'views/report/report_template_model_name.xml',

        # report action
        # 'views/action/action_report.xml',

        # assets
        # 'views/assets.xml',

        # onboarding action
        # 'views/action/action_onboarding.xml',

        # action menu
        # 'views/action/action_menu.xml',

        # action onboarding
        # 'views/action/action_onboarding.xml',

        # menu
        # 'views/menu.xml',

        # security
        # 'security/ir.model.access.csv',
        # 'security/ir.rule.csv',

        # data
    ],
    "demo": [
        # 'demo/demo.xml',
    ],
    "qweb": [
        # "static/src/xml/{QWEBFILE1}.xml",
    ],
    # "assets": {
    #     'web.assets_backend': [
    #         'your_module/static/src/xml/file.xml',
    #         'your_module/static/src/js/file.js',
    #         'your_module/static/src/css/file.css',
    #     ],
    #     'web.assets_frontend': [
            
    #     ]
    # },

    "post_load": None,
    # "pre_init_hook": "pre_init_hook",
    # "post_init_hook": "post_init_hook",
    "uninstall_hook": None,

    "external_dependencies": {"python": [], "bin": []},
    # "live_test_url": "",
    # "demo_title": "{MODULE_NAME}",
    # "demo_addons": [
    # ],
    # "demo_addons_hidden": [
    # ],
    # "demo_url": "DEMO-URL",
    # "demo_summary": "{SHORT_DESCRIPTION_OF_THE_MODULE}",
    # "demo_images": [
    #    "images/MAIN_IMAGE",
    # ]
}
