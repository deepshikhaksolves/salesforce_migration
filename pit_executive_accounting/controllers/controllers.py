# -*- coding: utf-8 -*-
# from odoo import http


# class PitExecutiveAccounting(http.Controller):
#     @http.route('/pit_executive_accounting/pit_executive_accounting/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pit_executive_accounting/pit_executive_accounting/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pit_executive_accounting.listing', {
#             'root': '/pit_executive_accounting/pit_executive_accounting',
#             'objects': http.request.env['pit_executive_accounting.pit_executive_accounting'].search([]),
#         })

#     @http.route('/pit_executive_accounting/pit_executive_accounting/objects/<model("pit_executive_accounting.pit_executive_accounting"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pit_executive_accounting.object', {
#             'object': obj
#         })
