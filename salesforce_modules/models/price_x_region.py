from odoo import models, fields, api


class PriceXRegion(models.Model):
    _name = 'model_price_x_region'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Salesforce Price X Region'
    _rec_name = 'Name'

    # CreatedById already in odoo
    Name = fields.Char(string="Identification",track_visibility='onchange')
    # LastModifiedById already in odoo
    product_price_id = fields.Many2one('product.product', string="Product Price",track_visibility='onchange')
    region_id = fields.Many2one('model_region', string="Region",track_visibility='onchange')
    model_product_price_id = fields.Many2one('product_price', string='Product Price Id',track_visibility='onchange')