from odoo import models, fields, api


class Region(models.Model):
    _name = 'model_region'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Region"
    _rec_name = 'Name'

    active_c = fields.Boolean(string='Active',default=True,track_visibility='onchange')
    # CreatedById  already in odoo
    # LastModifiedById already in odoo
    OwnerId = fields.Many2one('res.users',string='Owner',track_visibility='onchange')
    Name = fields.Char('Region',size=80,track_visibility='onchange')

    region_state_ids = fields.One2many('model_region_state', 'region', string='Region State',track_visibility='onchange')
    region_city_ids = fields.One2many('model_region_city', 'region', string='Region City',track_visibility='onchange')
    product_region_ids = fields.One2many('product.region', 'region_id', string='Product Region',track_visibility='onchange')
    price_x_region_ids = fields.One2many('model_price_x_region', 'region_id', string='Price X Region',track_visibility='onchange')
    accredited_network_ids = fields.One2many('accredited_network', 'region_c', string='Accredited Network',track_visibility='onchange')
