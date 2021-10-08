# -*- coding: utf-8 -*-
# from odoo import http


# class PitExecutiveFinancial(http.Controller):
#     @http.route('/pit_executive_financial/pit_executive_financial/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pit_executive_financial/pit_executive_financial/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pit_executive_financial.listing', {
#             'root': '/pit_executive_financial/pit_executive_financial',
#             'objects': http.request.env['pit_executive_financial.pit_executive_financial'].search([]),
#         })

#     @http.route('/pit_executive_financial/pit_executive_financial/objects/<model("pit_executive_financial.pit_executive_financial"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pit_executive_financial.object', {
#             'object': obj
#         })
