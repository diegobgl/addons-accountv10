# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import UserError, Warning

#________________________________________________ Model Inherit

class account_journal(models.Model):
    _inherit = 'account.journal'

    check_process = fields.Boolean(string='Check Process', )