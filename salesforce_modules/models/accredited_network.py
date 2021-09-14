from odoo import models, fields, api


class AccreditedNetwork(models.Model):
    _name = 'accredited_network'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Accredited network"
    _rec_name = 'Name'

    Name        = fields.Char(string='Accredited Network', size=80)
    active__c   = fields.Boolean('Active')

    # CreatedById  already in odoo
    # LastModifiedById already in odoo
    region__c     = fields.Many2one('model_region',string='Region')
    account_id = fields.Many2one('account.account', string='Account Id')
    network_provider_ids = fields.One2many('model_network_provider', 'accredited_network__c', string='Network Provider IDS')
    quote_line_item_ids = fields.One2many('quote_line_item', 'accredited_network__c', string='Network Provider IDS')