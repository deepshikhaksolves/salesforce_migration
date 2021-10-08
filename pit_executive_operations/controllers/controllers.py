# -*- coding: utf-8 -*-
# from odoo import http


# class PitExecutiveOperations(http.Controller):
#     @http.route('/pit_executive_operations/pit_executive_operations/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pit_executive_operations/pit_executive_operations/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pit_executive_operations.listing', {
#             'root': '/pit_executive_operations/pit_executive_operations',
#             'objects': http.request.env['pit_executive_operations.pit_executive_operations'].search([]),
#         })

#     @http.route('/pit_executive_operations/pit_executive_operations/objects/<model("pit_executive_operations.pit_executive_operations"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pit_executive_operations.object', {
#             'object': obj
#         })
