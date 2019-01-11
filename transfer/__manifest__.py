# coding: utf-8
{
    'name': 'Transferencia entre Cuentas',
    'author': 'Falcon Solutions SpA',
    'version': '10.0.1.0.0',
    'category': 'Accounting',
    'website': 'https://www.odoo.com',
    'depends': ['account'],
    'sumary': 'Account transfers',
    'description': """
    This module handles transferences between two accounts, making use of a
    simple wizard
    """,
    'data': [
        'wizard/transfer_wizard_view.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
}
