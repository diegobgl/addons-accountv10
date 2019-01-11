# -*- coding: utf-8 -*-
import datetime
from odoo import api, fields, models, _
from odoo.exceptions import UserError, Warning


#________________________________________________ Model Inherit

class account_payment(models.Model):
    _inherit = 'account.payment'

    check_number = fields.Char(string='Check Number', )
    bank_id = fields.Many2one('account.payment.bank', string='Check Bank Name', )
    check_process = fields.Boolean(related='journal_id.check_process', store=True,string='Check Process', )

#________________________________________________ Model

class account_payment_bank(models.Model):
    _name = 'account.payment.bank'
    _rec_name = 'name'
    _sql_constraints = [('name_unique', 'unique (name)', 'Bank Name must be unique')]

    name = fields.Char(string='Bank Name', required=True, )
