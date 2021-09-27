# -*- coding: utf-8 -*-
# from odoo import http


# class PitRelationship(http.Controller):
#     @http.route('/pit_relationship/pit_relationship/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pit_relationship/pit_relationship/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pit_relationship.listing', {
#             'root': '/pit_relationship/pit_relationship',
#             'objects': http.request.env['pit_relationship.pit_relationship'].search([]),
#         })

#     @http.route('/pit_relationship/pit_relationship/objects/<model("pit_relationship.pit_relationship"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pit_relationship.object', {
#             'object': obj
#         })
