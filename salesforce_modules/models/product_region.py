from odoo import models, fields, api


class SalesforceProductRegion(models.Model):

    _name = 'product.region'
    _description = 'Salesforce Product Region'

    user_id = fields.Many2one('res.users', string="Created By")
    last_modified_by_id = fields.Many2one('res.users', string="Last Modified By")
    name = fields.Char('Identification')
    product_id = fields.Many2one('product.product', string="Product")
    region = fields.Char('Region')