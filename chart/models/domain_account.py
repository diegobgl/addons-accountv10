# # -*- coding: utf-8 -*-
# import datetime
# from odoo import api, fields, models, _
# from odoo.exceptions import UserError, Warning
#
#
# #________________________________________________ Model Inherit
#
# class account_move_line(models.Model):
#     _inherit = 'account.move.line'
#
#     account_id = fields.Many2one('account.account', domain="[('is_parent','=',False)]" )
#
# #________________________________________________ Model Inherit
#
# class account_invoice(models.Model):
#     _inherit = 'account.invoice'
#
#     account_id = fields.Many2one('account.account', domain="[('is_parent','=',False)]" )
#
# #________________________________________________ Model Inherit
#
# class account_invoice_line(models.Model):
#     _inherit = 'account.invoice.line'
#
#     account_id = fields.Many2one('account.account', domain="[('is_parent','=',False)]" )
#
#
# #________________________________________________ Model Inherit
#
# class account_journal(models.Model):
#     _inherit = 'account.journal'
#
#     default_debit_account_id = fields.Many2one('account.account', domain="[('is_parent','=',False)]" )
#     default_credit_account_id = fields.Many2one('account.account', domain="[('is_parent','=',False)]" )
