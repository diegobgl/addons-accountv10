# -*- coding: utf-8 -*-
import datetime
from odoo import api, fields, models, _
from odoo.exceptions import UserError, Warning


#________________________________________________ Model Inherit

class account_analytic(models.Model):
    _inherit = 'account.analytic.account'

    parent_id = fields.Many2one('account.analytic.account', string='Parent', )
    child_ids = fields.One2many('account.analytic.account', 'parent_id', string='Child', )
    # line_ids = fields.One2many('account.analytic.line', 'account_id', compute='_compute_line', inverse='_inverse_line', store=True,  string="Analytic Lines")
    #
    # @api.multi
    # @api.depends('child_ids.line_ids')
    # def _compute_line(self):
    #     lines=[]
    #     for record in self.child_ids:
    #         for line in record.line_ids:
    #             lines.append((0, 0, {}))
    #
    #
    # @api.multi
    # def _inverse_line(self):
    #     for line in self:
    #         if not line: continue
    #
    #


