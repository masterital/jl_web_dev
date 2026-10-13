# -*- coding: utf-8 -*-
{
    'name': "Sale & Invoic Product Image",

    'summary': """Sale & Invoice Show / Hide  Product Image""",

    'description': """By using this module you can show product image in back-end form view, pdf report and portal
    view of sale order and invoice.""",

    'author': 'ErpMstar Solutions',
    'category': 'Sales',
    'version': '1.1',

    # any module necessary for this one to work correctly
    'depends': ['sale_management'],

    # always loaded
    'data': [
        'views/sale_order_view_show_product_image.xml',
        'views/account_move_view_show_product_image.xml',
        'report/sale_order_report_template.xml',
        'report/account_move_report_template.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'installable': True,
    'auto_install': False,
    'price': 22,
    'currency': 'EUR',
    'application': True,
}
