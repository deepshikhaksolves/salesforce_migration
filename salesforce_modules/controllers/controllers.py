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

from odoo import http, api
from odoo.http import request
import json


class SalesforceAPI(http.Controller):

    @http.route('/acommodation', type="http", auth='public')
    def acomodation_search(self):
        data = {}
        # data = json.dumps({"data": "API Called Sucessfully"})
        # print('Data========', data)
        geo_rec = request.env['model_geographic_scope']
        # geo_fields = request.env['ir.model.fields'].sudo().search([('model','=','model_geographic_scope')]).mapped('name')
        print('user_data===>>>>',geo_rec.fields_get())

        # fields_list = user_data.field_id.filtered(lambda r: r.model == 'account.analytic.account').mapped('name')
        # print('fields====', fields_list)
        # for rec in user_data:
        #     print('rec========', rec)
        # print('Data====', data)
        # return json.dumps(data)
