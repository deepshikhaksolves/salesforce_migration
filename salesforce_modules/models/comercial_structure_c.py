from odoo import models, fields, api



class Comercial_Structure_C(models.Model):
    _name = 'model_comercial_structure_c'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Comercial Structure C"
    _rec_name = 'Name'

    # CreatedById  already in odoo
    # LastModifiedById already in odoo
    Parent_Access = fields.Boolean(string="Father's Hits")
    Name =  fields.Char(string='Commercial Structure', size=80)
    Internal_Structure = fields.Boolean(string='Internal structure')
    Multiple = fields.Boolean(string='multiples')
    OwnerId = fields.Many2one('res.users',string='Owner')
    Allows_Pair = fields.Boolean(string='Permit By')
    Quantity = fields.Float(string='The amount',digits=(3,0))


