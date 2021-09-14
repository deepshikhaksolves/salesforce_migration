from odoo import models, fields, api

class City_C(models.Model):
    _name = 'model_city_c'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce City C"
    _rec_name = 'Name'

    # CreatedById  already in odoo
    # LastModifiedById already in odoo

    Geographic_Scope_id = fields.Many2one('model_geographic_scope',string='Coverage')
    Name = fields.Char(string='City',size=80)
    City_Code = fields.Char(string='City code',size=7)
    State_id = fields.Many2one('state',string='State')