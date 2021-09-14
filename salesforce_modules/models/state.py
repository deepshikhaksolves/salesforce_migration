from odoo import models, fields, api


class State(models.Model):
    _name = 'res.country.state'
    # _inherit = 'res.country.state'
    _inherit = ['res.country.state','mail.thread', 'mail.activity.mixin']
    _description = "Salesforce State"

    Geographic_Scope_id = fields.Many2one('model_geographic_scope', string="Coverage")
    # CreatedById already in odoo
    # State_Code already in odoo as code
    # Name = already in odoo
    # LastModifiedById already in odoo
    # Country__c alreay in odoo
    State_Initials =  fields.Char(string="State acronym", size=2)
    