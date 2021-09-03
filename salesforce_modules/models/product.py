from odoo import models, fields, api


class Product(models.Model):
    _name = 'model_product'
    _description = "Salesforce Product"
    _rec_name = 'Name'

    # CreatedById  already in odoo
    Name        = fields.Char(string='Description', size=80)
    # LastModifiedById already in odoo
    OwnerId     = fields.Many2one('res.users',string='Owner')
