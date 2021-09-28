# -*- coding: utf-8 -*-
# from odoo import http


# class PitTechnicalAreaRegistration(http.Controller):
#     @http.route('/pit_technical_area_registration/pit_technical_area_registration/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pit_technical_area_registration/pit_technical_area_registration/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pit_technical_area_registration.listing', {
#             'root': '/pit_technical_area_registration/pit_technical_area_registration',
#             'objects': http.request.env['pit_technical_area_registration.pit_technical_area_registration'].search([]),
#         })

#     @http.route('/pit_technical_area_registration/pit_technical_area_registration/objects/<model("pit_technical_area_registration.pit_technical_area_registration"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pit_technical_area_registration.object', {
#             'object': obj
#         })
