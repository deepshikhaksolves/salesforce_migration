from odoo import models, fields, api


class Region(models.Model):
    _name = 'model_region'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Region"
    _rec_name = 'Name'

    active__c = fields.Boolean(string='Active',default=True)
    # CreatedById  already in odoo
    # LastModifiedById already in odoo
    OwnerId = fields.Many2one('res.users',string='Owner')
    Name = fields.Char('Region',size=80)

    region_state_ids = fields.One2many('model_region_state', 'region', string='Region State Ids')
    region_city_ids = fields.One2many('model_region_city', 'region', string='Region City Ids')
    product_region_ids = fields.One2many('product.region', 'region_id', string='Product Region Ids')
    price_x_region_ids = fields.One2many('model_price_x_region', 'region_id', string='Price X Region Ids')
    accredited_network_ids = fields.One2many('accredited_network', 'region__c', string='Accredited Network Ids')
