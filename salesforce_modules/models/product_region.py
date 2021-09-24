from odoo import models, fields, api


class SalesforceProductRegion(models.Model):

    _name = 'product.region'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Salesforce Product Region'

    user_id = fields.Many2one('res.users', string="Created By",track_visibility='onchange')
    last_modified_by_id = fields.Many2one('res.users', string="Last Modified By",track_visibility='onchange')
    name = fields.Char('Identification',track_visibility='onchange')
    product_id = fields.Many2one('product.template', string="Product",track_visibility='onchange')
    region = fields.Char('Region',track_visibility='onchange')
    region_id = fields.Many2one('model_region', string="Region Id",track_visibility='onchange')