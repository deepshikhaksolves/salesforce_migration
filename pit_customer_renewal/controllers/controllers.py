# -*- coding: utf-8 -*-
# from odoo import http


# class PitCustomerRenewal(http.Controller):
#     @http.route('/pit_customer_renewal/pit_customer_renewal/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pit_customer_renewal/pit_customer_renewal/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pit_customer_renewal.listing', {
#             'root': '/pit_customer_renewal/pit_customer_renewal',
#             'objects': http.request.env['pit_customer_renewal.pit_customer_renewal'].search([]),
#         })

#     @http.route('/pit_customer_renewal/pit_customer_renewal/objects/<model("pit_customer_renewal.pit_customer_renewal"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pit_customer_renewal.object', {
#             'object': obj
#         })
