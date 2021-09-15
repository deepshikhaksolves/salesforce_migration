from odoo import models, fields, api


class RegionState(models.Model):
    _name = 'model_region_state'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Region State"
    _rec_name = 'region'

    # CreatedById  already in odoo
    Name = fields.Char('Identification')
    # LastModifiedById already in odoo
    region = fields.Many2one('model_region', string='Region')
    state_id = fields.Many2one('res.country.state', string="State")
