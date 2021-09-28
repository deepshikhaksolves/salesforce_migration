# -*- coding: utf-8 -*-
# from odoo import http


# class PitRiskManagement(http.Controller):
#     @http.route('/pit_risk_management/pit_risk_management/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pit_risk_management/pit_risk_management/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pit_risk_management.listing', {
#             'root': '/pit_risk_management/pit_risk_management',
#             'objects': http.request.env['pit_risk_management.pit_risk_management'].search([]),
#         })

#     @http.route('/pit_risk_management/pit_risk_management/objects/<model("pit_risk_management.pit_risk_management"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pit_risk_management.object', {
#             'object': obj
#         })
