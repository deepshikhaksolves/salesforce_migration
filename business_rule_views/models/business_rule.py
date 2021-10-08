from odoo import models, fields, api
from odoo.tools.safe_eval import safe_eval


class BusinessRuleActionInherit(models.Model):
    _inherit = 'config.open.view'
    _description = 'BusinessRuleActionInherit'

    show_popup = fields.Boolean(string='Show popup on create')



    def get_record_according_to_domain(self, model_name,res_ids):
        rec_set = self.env['config.open.view'].search([('ir_model.model', '=', model_name)])

        data = []
        if rec_set:
            data.append({
                'model': rec_set.ir_model.model,
                'show_popup': rec_set.show_popup,
                'res_ids':[]
            })
        sorted_data = rec_set.configuration_ids.sorted(key=lambda conf: conf.sequence)
        for rec in sorted_data:
            data_dict = {
                'model': rec_set.ir_model.model,
                'view_id': rec.ir_view.id,
                'domain': safe_eval(rec.domain) if rec.domain else safe_eval('False'),
                'context': safe_eval(rec.context),
                'res_ids': []
            }
            if rec.domain:
                domain_data = rec.env[model_name].search(safe_eval(rec.domain)+[['id','in',res_ids]])
                if domain_data:
                    data_dict['res_ids'] = domain_data.ids
            data.append(data_dict)
        return data