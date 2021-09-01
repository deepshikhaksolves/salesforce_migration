from odoo import models, fields, api


class GeographicScope(models.Model):
    _name = 'model_geographic_scope'
    _description = "Salesforce Coverage"
    _rec_name = 'Abbreviation__c'


    Abbreviation__c = fields.Text('Abbreviation',size=50)
    Name            = fields.Text('ANS scope',size=80)
    Geographic_Scope_ID__c = fields.Integer('Scope ID')
    # CreatedById already in odoo
    Geographic_Scope_tnk__c = fields.Text('Geographic Scope tnk',size=80)
    # LastModifiedById already in odoo
    OwnerId = fields.Many2one('res.users',string='Owner')
    RecordTypeId = fields.Char('Record Type')