from odoo import models, fields, api


class BrandC(models.Model):
    _name = 'model_brand_c'
    _description = 'Salesforce Brand'
    _rec_name = 'Name'

    # CreatedById already in odoo
    # LastModifiedById already in odoo
    Name = fields.Char(string="Mark", size=80)
    OwnerId = fields.Many2one('res.users', string='Owner')
