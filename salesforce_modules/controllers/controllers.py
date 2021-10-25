# -*- coding: utf-8 -*-
from odoo import http, api
from odoo.http import request
import json


class SalesforceAPI(http.Controller):

    @http.route('/acommodation', type="http", auth='public')
    def acomodation_search(self):
        main_dict = {}
        data_dict = {}
        model_rec = request.env['ir.model'].sudo().search([])
        geo_recs = request.env['model_geographic_scope'].sudo().search([])
        field_ids = model_rec.field_id.filtered(lambda r: r.model == 'model_geographic_scope')
        # fields_list = model_rec.field_id.filtered(lambda r: r.model == 'model_geographic_scope').mapped('name')
        # print("Fields list======>>>>>", fields_list)
        count = 0
        for rec in geo_recs:
            main_dict[str(rec.id)] = {}
            for fields_rec in field_ids:
                field_value = ''
                if fields_rec.ttype in ['char', 'integer', 'date', 'datetime', 'selection', 'boolean']:
                    field_value = str(rec[str(fields_rec.name)])
                elif fields_rec.ttype == 'many2one':
                    field_value = str(rec[str(fields_rec.name)].id)
                elif fields_rec.ttype == 'one2many':
                    field_value = rec[str(fields_rec.name)].ids
                elif fields_rec.ttype == 'many2many':
                    field_value = rec[str(fields_rec.name)].ids
                if count <= len(field_ids):
                    data_dict[str(fields_rec.name)] = field_value
                    count + 1
            main_dict[str(rec.id)].update(data_dict)
        final_data = json.dumps(main_dict)
        print('Final data========', final_data)
        return final_data
