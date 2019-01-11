# -*- coding: utf-8 -*-
import datetime
from odoo import api, fields, models, _
from odoo.exceptions import UserError, Warning



#________________________________________________ Model Inherit

class account_account(models.Model):
    _inherit = 'account.account'

    child_ids = fields.One2many('account.account', 'parent_id', string='Child', readonly=True, )
    parent_id = fields.Many2one('account.account', string='Parent', )
    is_parent = fields.Boolean(string='Is Parent?',compute='_compute_is_parent', inverse='_inverse_is_parent',store=True, )

    

    @api.one
    @api.depends('child_ids')
    def _compute_is_parent(self):
        if len(self.child_ids)>0:
            self.is_parent=True
    @api.one
    @api.depends('child_ids')
    def _inverse_is_parent(self):
        for record in self:
            if not record.is_parent :continue