from odoo import models, fields, api


class NetworkProvider(models.Model):
    _name = 'model_network_provider'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Network Provider"
    _rec_name = 'Name'

    accredited_network_c = fields.Many2one('accredited_network', string='Accredited Network',track_visibility='onchange')
    How_c = fields.Char('Comment', size=255,track_visibility='onchange')
    # CreatedById already in odoo
    Name = fields.Char('Identification',track_visibility='onchange')
    # LastModifiedById already in odoo
    hide_provider_c = fields.Boolean('Hide Provider',track_visibility='onchange')
    ordering_c = fields.Float(string="ordering", digits=(18, 0),track_visibility='onchange')
    OwnerId = fields.Many2one('res.users', string='Owner',track_visibility='onchange')
    product2_c = fields.Many2one('product.template', string='Plano',track_visibility='onchange')
    account_c = fields.Many2one('account.account', string='Provider',track_visibility='onchange')
    RecordTypeId = fields.Integer('Record Type',track_visibility='onchange')

