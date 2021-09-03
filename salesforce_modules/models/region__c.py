from odoo import models, fields, api


class Region(models.Model):
    _name = 'model_region'
    _description = "Salesforce Region"
    _rec_name = 'Name'

    active__c   = fields.Boolean(string='Active',default=True)
    # CreatedById  already in odoo
    # LastModifiedById already in odoo
    OwnerId     = fields.Many2one('res.users',string='Owner')
    Name        = fields.Char('Region',size=80)