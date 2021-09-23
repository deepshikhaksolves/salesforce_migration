from odoo import models, fields, api


class GeographicScope(models.Model):
    _name = 'model_geographic_scope'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Coverage"
    _rec_name = 'Abbreviation__c'

    Abbreviation__c = fields.Char('Abbreviation', size=50)
    Name = fields.Char('ANS scope', size=80)
    Geographic_Scope_ID__c = fields.Integer('Scope ID')
    # CreatedById already in odoo
    Geographic_Scope_tnk__c = fields.Char('Geographic Scope tnk', size=80)
    # LastModifiedById already in odoo
    OwnerId = fields.Many2one('res.users', string='Owner')
    RecordTypeId = fields.Char('Record Type')

    product_ids = fields.One2many('product.template', 'geo_scope_id', string='Product IDS')
    address_ids = fields.One2many('model_address', 'geo_scope_id', string='Address Ids')
    city_ids = fields.One2many('model_city_c', 'Geographic_Scope_id', string='City Ids')
    state_ids = fields.One2many('res.country.state', 'Geographic_Scope_id', string='State Ids')
