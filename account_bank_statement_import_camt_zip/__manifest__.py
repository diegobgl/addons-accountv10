# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

{
    'name': 'Import CAMT Bank Statement Zip file',
    'version': '10.1',
    'category': 'Accounting & Finance',
    'description': """
    """,
    "author": 'Odoo Experts',
    "website": 'https://www.odooexperts.nl',
    'depends': ['account_bank_statement_import_camt'],
    'description': """
Module to import CAMT bank statements that are compressed in a ZIP format.
======================================

Improve the import of bank statement feature to support the SEPA recommanded Cash Management format (CAMT.053), compressed in a ZIP file.
    """,
    'data': [
        'data/account_bank_statement_import_zip_data.xml'
    ],
    'license': 'Other proprietary',
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
