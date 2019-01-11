# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

from openerp import models, fields, api


class AccountJournal(models.Model):
    _inherit = "account.journal"

    is_zip = fields.Boolean(string='Allow zip file',)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
