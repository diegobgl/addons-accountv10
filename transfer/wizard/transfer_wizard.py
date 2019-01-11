# coding: utf-8
from datetime import date

from odoo import _, api, models, fields
from odoo.exceptions import ValidationError


class TransferWizard(models.TransientModel):
    """Model for Transfer Wizard"""

    _name = 'transfer.wizard'
    _description = 'Wizard to handle transfers between accounts'

    from_account_id = fields.Many2one('account.journal', 'From', required=True)
    to_account_id = fields.Many2one('account.journal', 'To', required=True)
    amount = fields.Float(required=True)
    reason = fields.Char(size=256)

    @api.constrains('from_account_id', 'to_account_id')
    def check_accounts_diff(self):
        """Checks that both accounts are not the same"""
        if self.from_account_id == self.to_account_id:
            raise ValidationError(_('Accounts cannot be the same'))

    @api.constrains('amount')
    def check_amout_positive(self):
        """Checks that amount is positive"""
        if self.amount <= 0:
            raise ValidationError(_('Amount must be positive'))

    @api.multi
    def execute(self):
        """Call from wizard to execute the transfer"""
        self.ensure_one()
        assert self.from_account_id, 'From account not set'
        assert self.to_account_id, 'To account not set'
        today = date.today()
        tag = 'TRX-{acc1}-{acc2}-{day}'.format(acc1=self.from_account_id.id,
                                               acc2=self.to_account_id.id,
                                               day=str(today))
        # Creating the first account.move.line
        first_line_data = {
            'account_id': self.from_account_id.id,
            'date_maturity': today,  # TODO No entiendo el vencimiento...
            'name': tag,
            'debit': self.amount
        }
        # Now creating the second one account.move.line
        second_line_data = first_line_data.copy()
        second_line_data.update({
            'credit': second_line_data.pop('debit'),
            'account_id': self.to_account_id.id
        })
        # Creating the account.move
        data = {
            'journal_id': self.from_account_id.id,
            'ref': tag,
            'date': today,
            'line_ids': [(0, _, first_line_data), (0, _, second_line_data)]
        }
        acc_move_id = self.env['account.move'].create(data)

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'account.move',
            'res_id': acc_move_id.id,
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new'
        }
