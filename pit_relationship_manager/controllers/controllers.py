# -*- coding: utf-8 -*-
# from odoo import http


# class PitRelationshipManager(http.Controller):
#     @http.route('/pit_relationship_manager/pit_relationship_manager/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pit_relationship_manager/pit_relationship_manager/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pit_relationship_manager.listing', {
#             'root': '/pit_relationship_manager/pit_relationship_manager',
#             'objects': http.request.env['pit_relationship_manager.pit_relationship_manager'].search([]),
#         })

#     @http.route('/pit_relationship_manager/pit_relationship_manager/objects/<model("pit_relationship_manager.pit_relationship_manager"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pit_relationship_manager.object', {
#             'object': obj
#         })
