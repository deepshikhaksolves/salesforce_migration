from odoo import models, fields, api


class AccreditedNetwork(models.Model):
    _name = 'accredited_network'
    _description = "Salesforce Accredited network"
    _rec_name = 'Name'

    Name        = fields.Text(string='Accredited Network', size=80)
    active__c   = fields.Boolean('Active')

    # CreatedById  already in odoo
    # LastModifiedById already in odoo
    region__c     = fields.Many2one('model_region',string='Region')
