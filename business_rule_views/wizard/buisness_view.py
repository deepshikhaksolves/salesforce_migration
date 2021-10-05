from odoo import api, models,fields



class BuisnessViewWizard(models.TransientModel):
    _name = 'buisness.rule.view'
    _description = 'BuisnessViewWizard'


    def get_all_views(self):
        get_models = self.env['config.open.view'].search([('ir_model', '=', self._context.get('active_model'))], limit=1)
        ls = []
        for model in get_models.configuration_ids:
            ls.append((model.ir_view.xml_id, model.ir_view.name))
        return ls

    buisness_rule_view_get = fields.Selection(get_all_views,string='Buisness rule view get')

    def get_buisness_action(self,model_name):
        action = self.env['ir.actions.act_window']._for_xml_id('business_rule_views''.action_buisness_rule_view')
        ctx = dict(self.env.context)
        ctx.update({
            'active_model': model_name,

        })
        action['context'] = ctx
        return action

    def open_business_view(self):
        get_models = self.env['config.open.view'].search([('ir_model', '=', self._context.get('active_model'))],limit=1)
        action={
            'res_model':self.env.context.get('active_model'),
            'type': "ir.actions.act_window",
            'views': [[self.env.ref(self.buisness_rule_view_get).id, 'form']],
            'target': "current",
        }
        return action

    def check_all_models(self):
        get_models = self.env['config.open.view'].search([('ir_model', '=', self._context.get('active_model'))],limit=1)
        product_id = self.env['ir.config_parameter'].sudo().get_param('business_rule_views.buisness_rules_views')