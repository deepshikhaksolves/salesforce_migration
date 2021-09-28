# -*- coding: utf-8 -*-
# from odoo import http


# class PitExecutiveRelationship(http.Controller):
#     @http.route('/pit_executive_relationship/pit_executive_relationship/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pit_executive_relationship/pit_executive_relationship/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pit_executive_relationship.listing', {
#             'root': '/pit_executive_relationship/pit_executive_relationship',
#             'objects': http.request.env['pit_executive_relationship.pit_executive_relationship'].search([]),
#         })

#     @http.route('/pit_executive_relationship/pit_executive_relationship/objects/<model("pit_executive_relationship.pit_executive_relationship"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pit_executive_relationship.object', {
#             'object': obj
#         })
