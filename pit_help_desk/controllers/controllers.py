# -*- coding: utf-8 -*-
# from odoo import http


# class PitHelpDesk(http.Controller):
#     @http.route('/pit_help_desk/pit_help_desk/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pit_help_desk/pit_help_desk/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pit_help_desk.listing', {
#             'root': '/pit_help_desk/pit_help_desk',
#             'objects': http.request.env['pit_help_desk.pit_help_desk'].search([]),
#         })

#     @http.route('/pit_help_desk/pit_help_desk/objects/<model("pit_help_desk.pit_help_desk"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pit_help_desk.object', {
#             'object': obj
#         })
