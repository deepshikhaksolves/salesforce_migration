from odoo import models, fields, api
from odoo.exceptions import ValidationError


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

    @api.constrains('Quantity')
    def digit_validation(self):
        for rec in self:
            if rec.Quantity > 999:
                raise ValidationError("The amount should not greater than 3 digits")

