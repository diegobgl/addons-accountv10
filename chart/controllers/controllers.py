# -*- coding: utf-8 -*-
from odoo import http

# class Chart(http.Controller):
#     @http.route('/chart/chart/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/chart/chart/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('chart.listing', {
#             'root': '/chart/chart',
#             'objects': http.request.env['chart.chart'].search([]),
#         })

#     @http.route('/chart/chart/objects/<model("chart.chart"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('chart.object', {
#             'object': obj
#         })