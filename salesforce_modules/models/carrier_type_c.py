from odoo import models, fields, api

class Carrier_Type_C(models.Model):
    _name = 'model_carrier_type_c'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Carrier Type C"
    _rec_name = 'Name'

    # CreatedById  already in odoo
    # LastModifiedById already in odoo

    OwnerId = fields.Many2one('res.users', string='Owner')
    Initials = fields.Char(string='Initials', size=20)
    Name = fields.Char(string='Operator Type',size=80)
    Carrier_Type = fields.Char(string='Type of Carrier ID')
