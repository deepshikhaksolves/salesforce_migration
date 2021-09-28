# -*- coding: utf-8 -*-
# from odoo import http


# class PitFinancial(http.Controller):
#     @http.route('/pit_financial/pit_financial/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pit_financial/pit_financial/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pit_financial.listing', {
#             'root': '/pit_financial/pit_financial',
#             'objects': http.request.env['pit_financial.pit_financial'].search([]),
#         })

#     @http.route('/pit_financial/pit_financial/objects/<model("pit_financial.pit_financial"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pit_financial.object', {
#             'object': obj
#         })
