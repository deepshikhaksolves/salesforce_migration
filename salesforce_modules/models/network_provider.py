from odoo import models, fields, api


class NetworkProvider(models.Model):
    _name = 'model_network_provider'
    _description = "Salesforce Network Provider"
    _rec_name = 'Name'

    accredited_network__c   = fields.Many2one('accredited_network',string='Accredited Network')
    How_c	                = fields.Char('Comment',size=255)
    # CreatedById already in odoo
    Name                    = fields.Char('Identification')
    # LastModifiedById already in odoo
    hide_provider__c        = fields.Boolean('Hide Provider')
    ordering__c             = fields.Float(string="ordering", digits=(18, 0) )
    OwnerId                 = fields.Many2one('res.users',string='Owner')
    product2__c             = fields.Many2one('product.template', string='Plano')
    account__c              = fields.Many2one('account.account', string='provider')
    RecordTypeId            = fields.Integer('Record Type')
