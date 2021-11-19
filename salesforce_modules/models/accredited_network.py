from odoo import models, fields, api


class AccreditedNetwork(models.Model):
    _name = 'accredited_network'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Accredited network"
    _rec_name = 'Name'

    Name = fields.Char(string='Accredited Network', size=80, track_visibility='onchange')
    active_c = fields.Boolean('Active', track_visibility='onchange')

    # CreatedById  already in odoo
    # LastModifiedById already in odoo
    region_c = fields.Many2one('model_region', string='Region', track_visibility='onchange')
    account_id = fields.Many2one('account.account', string='Account Id', track_visibility='onchange')
    network_provider_ids = fields.One2many('model_network_provider', 'accredited_network_c', string='Network Providers')
    quote_line_item_ids = fields.One2many('quote_line_item', 'accredited_network_c', string='Quote Line Items')

    product_network_ids = fields.One2many('product.network', 'accredited_network_id', string='Product Networks')
