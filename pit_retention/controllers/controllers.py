# -*- coding: utf-8 -*-
# from odoo import http


# class PitRetention(http.Controller):
#     @http.route('/pit_retention/pit_retention/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pit_retention/pit_retention/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pit_retention.listing', {
#             'root': '/pit_retention/pit_retention',
#             'objects': http.request.env['pit_retention.pit_retention'].search([]),
#         })

#     @http.route('/pit_retention/pit_retention/objects/<model("pit_retention.pit_retention"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pit_retention.object', {
#             'object': obj
#         })
