{
    'name': "Codesk Solutions",
    'version': '1.0',
    'depends': ['base','sale','hr','sale_management','hr_holidays','account','invoice_stock_move'],
    'author': "Reem",
    'description': """
    Codesk Solutions Module
    """,
    'data': [
        'views/hr_leave_type_view.xml',
        'views/res_currency_view.xml',
        'views/product_category_view.xml',
        'views/product_template_view.xml',
        'views/account_move_view.xml',


    ],
    'installable': True,
    'auto_install': False,
    'license': 'AGPL-3',
    }