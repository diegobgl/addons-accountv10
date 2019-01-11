# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

from lxml import etree
import base64
import tempfile
from openerp import api, models, fields
import logging
from zipfile import ZipFile, BadZipfile
_logger = logging.getLogger(__name__)
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


class AccountBankStatementImport(models.TransientModel):
    _inherit = 'account.bank.statement.import'

    def _check_zip(self, data_file):
        files = [data_file]
        tmpdir = tempfile.gettempdir()
        image_list = []
        try:
            with ZipFile(StringIO(data_file), 'r') as archive:
                archive.extractall(tmpdir)
                files = [
                    archive.read(file_name) for file_name in archive.namelist()

                    ]
        except BadZipfile:
            pass
        for import_file in files:
            image_list.append(import_file)
        return image_list

    @api.multi
    def import_file(self):
        self.ensure_one()
        journal_obj = self.env['account.journal']
        journal_id_new = journal_obj.browse(self.env.context.get('journal_id', []))
        allow_zip = journal_id_new.is_zip
        if allow_zip:
            data_file = base64.b64decode(self.data_file)
            zip_file_data = self._check_zip(data_file)
            st_ids = []
            not_ids = []
            for data_file in zip_file_data:
                # Let the appropriate implementation module parse the file and return the required data
                # The active_id is passed in context in case an implementation module requires information about the wizard state (see QIF)
                currency_code, account_number, stmts_vals = self.with_context(active_id=self.ids[0])._parse_file(data_file)
                # Check raw data
                self._check_parsed_data(stmts_vals)
                # Try to find the currency and journal in odoo
                currency, journal = self._find_additional_data(currency_code, account_number)
                # If no journal found, ask the user about creating one
                if not journal:
                    # The active_id is passed in context so the wizard can call import_file again once the journal is created
                    return self.with_context(active_id=self.ids[0])._journal_creation_wizard(currency, account_number)
                # Prepare statement data to be used for bank statements creation
                stmts_vals = self._complete_stmts_vals(stmts_vals, journal, account_number)
                # Create the bank statements
                statement_ids, notifications = self._create_bank_statements(stmts_vals)
                st_ids.extend(statement_ids)
                not_ids.extend(notifications)
                # Now that the import worked out, set it as the bank_statements_source of the journal
                journal.bank_statements_source = 'file_import'
                # Finally dispatch to reconciliation interface
                action = self.env.ref('account.action_bank_reconcile_bank_statements')
            return {
                'name': action.name,
                'tag': action.tag,
                'context': {
                    'statement_ids': st_ids,
                    'notifications': not_ids
                },
                'type': 'ir.actions.client',
            }
        else:
            """ Process the file chosen in the wizard, create bank statement(s) and go to reconciliation. """
            self.ensure_one()
            # Let the appropriate implementation module parse the file and return the required data
            # The active_id is passed in context in case an implementation module requires information about the wizard state (see QIF)
            currency_code, account_number, stmts_vals = self.with_context(active_id=self.ids[0])._parse_file(base64.b64decode(self.data_file))
            # Check raw data
            self._check_parsed_data(stmts_vals)
            # Try to find the currency and journal in odoo
            currency, journal = self._find_additional_data(currency_code, account_number)
            # If no journal found, ask the user about creating one
            if not journal:
                # The active_id is passed in context so the wizard can call import_file again once the journal is created
                return self.with_context(active_id=self.ids[0])._journal_creation_wizard(currency, account_number)
            # Prepare statement data to be used for bank statements creation
            stmts_vals = self._complete_stmts_vals(stmts_vals, journal, account_number)
            # Create the bank statements
            statement_ids, notifications = self._create_bank_statements(stmts_vals)
            # Now that the import worked out, set it as the bank_statements_source of the journal
            journal.bank_statements_source = 'file_import'
            # Finally dispatch to reconciliation interface
            action = self.env.ref('account.action_bank_reconcile_bank_statements')
            return {
                'name': action.name,
                'tag': action.tag,
                'context': {
                    'statement_ids': statement_ids,
                    'notifications': notifications
                },
                'type': 'ir.actions.client',
            }

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
