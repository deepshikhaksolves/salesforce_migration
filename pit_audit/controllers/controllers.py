# -*- coding: utf-8 -*-
# from odoo import http


# class PitAudit(http.Controller):
#     @http.route('/pit_audit/pit_audit/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pit_audit/pit_audit/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pit_audit.listing', {
#             'root': '/pit_audit/pit_audit',
#             'objects': http.request.env['pit_audit.pit_audit'].search([]),
#         })

#     @http.route('/pit_audit/pit_audit/objects/<model("pit_audit.pit_audit"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pit_audit.object', {
#             'object': obj
#         })
