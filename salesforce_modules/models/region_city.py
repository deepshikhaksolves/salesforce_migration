from odoo import models, fields, api


class RegionCity(models.Model):
    _name = 'model_region_city'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Region City"
    _rec_name = 'state__c'

    city__c   = fields.Many2one('model_city_c',string='City',track_visibility='onchange')
    # CreatedById  already in odoo
    Name = fields.Char('Identification',track_visibility='onchange')
    # LastModifiedById already in odoo
    priority = fields.Float('Priority', digits=(1, 0),track_visibility='onchange')
    region = fields.Many2one('model_region', string='Region',track_visibility='onchange')
    state__c = fields.Many2one('res.country.state', string='State', track_visibility='onchange')
