from odoo import models, fields, api

class Comercial_Agent_C(models.Model):
    _name = 'model_comercial_agent_c'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Comercial Agent C"
    _rec_name = 'Name'

    # CreatedById  already in odoo
    # LastModifiedById already in odoo

    Name = fields.Char(string='Commercial Agent ID')
    OwnerId = fields.Many2one('res.users',string='Owner')
    Agent_Type = fields.Selection([('Pre-Consultant','Pre-Consultant'),('Consultant','Consultant'),('Indicator','Indicator'),
                                   ('Manager','Manager'),('Relationship','Relationship')],string='Agent Type')