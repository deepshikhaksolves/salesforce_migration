# -*- coding: utf-8 -*-
# from odoo import http


# class SalesforceModules(http.Controller):
#     @http.route('/salesforce_modules/salesforce_modules/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/salesforce_modules/salesforce_modules/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('salesforce_modules.listing', {
#             'root': '/salesforce_modules/salesforce_modules',
#             'objects': http.request.env['salesforce_modules.salesforce_modules'].search([]),
#         })

#     @http.route('/salesforce_modules/salesforce_modules/objects/<model("salesforce_modules.salesforce_modules"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('salesforce_modules.object', {
#             'object': obj
#         })
