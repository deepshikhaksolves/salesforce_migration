from odoo import models, fields, api


class RegionCity(models.Model):
    _name = 'model_region_city'
    _description = "Salesforce Region City"
    _rec_name = 'state__c'

    # city__c   = fields.Many2one('model_city',string='City') #model_city Not created 
    # CreatedById  already in odoo
    Name        = fields.Char('Identification')
    # LastModifiedById already in odoo
    priority    = fields.Float('Priority', digits=(1, 0))
    region      = fields.Many2one('model_region', string='Region')
    state__c    = fields.Char('State')