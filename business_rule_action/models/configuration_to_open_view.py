# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.tools.safe_eval import safe_eval


class salesforce_open_view(models.Model):
    _name = 'config.open.view'
    _description = 'Configurations to open view'
    _rec_name = 'rule_name'

    rule_name = fields.Char("Business Rule Name")
    ir_model = fields.Many2one('ir.model', string='Model', required=True, ondelete='cascade')
    model_name = fields.Char(related='ir_model.model', string='Model Name')
    configuration_ids = fields.One2many('config.open.view.configurations', 'config_parent_id', 'Business Model '
                                                                                               'Configuration')

    def get_record_according_to_domain(self, model_name,res_ids):
        rec_set = self.env['config.open.view'].search([('ir_model.model', '=', model_name)])

        data = []
        for rec in rec_set.configuration_ids:
            data_dict = {
                'model': rec_set.ir_model.model,
                'view_id': rec.ir_view.id,
                'domain': safe_eval(rec.domain),
                'context': safe_eval(rec.context),
                'res_ids': []
            }
            if rec.domain:
                domain_data = rec.env[model_name].search(safe_eval(rec.domain)+[['id','in',res_ids]])
                if domain_data:
                    data_dict['res_ids'] = domain_data.ids
            data.append(data_dict)
        return data


class salesforce_open_view_configs(models.Model):

    _name = 'config.open.view.configurations'

    ir_view = fields.Many2one('ir.ui.view', string="View", required=True)
    context = fields.Char(string='Context Value', default={},
                          help="Context dictionary as Python expression, empty by default (Default: {})")
    domain = fields.Char('Domain')
    config_parent_id = fields.Many2one('config.open.view')
    model_name = fields.Char(related='config_parent_id.ir_model.model', string='Model Name')