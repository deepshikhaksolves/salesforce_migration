# -*- coding: utf-8 -*-
# from odoo import http


# class PitMedicalManagement(http.Controller):
#     @http.route('/pit_medical_management/pit_medical_management/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pit_medical_management/pit_medical_management/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pit_medical_management.listing', {
#             'root': '/pit_medical_management/pit_medical_management',
#             'objects': http.request.env['pit_medical_management.pit_medical_management'].search([]),
#         })

#     @http.route('/pit_medical_management/pit_medical_management/objects/<model("pit_medical_management.pit_medical_management"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pit_medical_management.object', {
#             'object': obj
#         })
