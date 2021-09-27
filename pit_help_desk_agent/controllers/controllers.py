# -*- coding: utf-8 -*-
# from odoo import http


# class PitHelpDeskAgent(http.Controller):
#     @http.route('/pit_help_desk_agent/pit_help_desk_agent/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pit_help_desk_agent/pit_help_desk_agent/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pit_help_desk_agent.listing', {
#             'root': '/pit_help_desk_agent/pit_help_desk_agent',
#             'objects': http.request.env['pit_help_desk_agent.pit_help_desk_agent'].search([]),
#         })

#     @http.route('/pit_help_desk_agent/pit_help_desk_agent/objects/<model("pit_help_desk_agent.pit_help_desk_agent"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pit_help_desk_agent.object', {
#             'object': obj
#         })
