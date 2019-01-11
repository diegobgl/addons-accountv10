# -*- coding: utf-8 -*-
{
    'name': 'Account Chart',
    'author': 'Muhamed Abd El-Rhman',
    'website': 'www.linkedin.com/in/muhamed-profile',
    'version': '1.0',
    'sequence': 1,
    'summary': 'Chart Of Account Hierarchy, Cost Center  Hierarchy',
    'description': """
Hierarchy For Accounts
**********************
- Is Parent? checkbox is equal True to be a parent account

- Only parent accounts will be displayed in parent list 

- Parent accounts will be displayed as root in the hierarchy

- Accounts that have a parent will be displayed as child in the hierarchy

    """,
    'category': 'Accounting',
    'license': 'OPL-1',
    'installable': True,
    'application': True,
    'auto_install': False,
    'depends': ['account_accountant', 'account', 'account_asset', 'base'],
    'data': [
        'views/account_account_view.xml',
        'views/domain_account_view.xml',
        'views/account_payment_view.xml',
        'views/account_journal_view.xml',
        'views/account_analytic_view.xml',
        'data/data.xml',
    ],
    'demo': [],
}
