from odoo import models, fields, api


class State(models.Model):
    _name = 'state'
    _description = "Salesforce State"
    _rec_name = 'Name'

    Geographic_Scope_id = fields.Many2one('model_geographic_scope', string="Coverage")
    # CreatedById already in odoo
    State_Code = fields.Char(string='State code', size=2)
    Name = fields.Char(string="State", size=80)
    # LastModifiedById already in odoo
    Country_id  = fields.Many2one('res.country', string="Country")
    State_Initials =  fields.Char(string="State acronym", size=2)
