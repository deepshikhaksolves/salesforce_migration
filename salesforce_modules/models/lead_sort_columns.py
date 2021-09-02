from odoo import models, fields, api


class LeadSortColumns(models.Model):
    _name = 'LeadSortColumsInCapaign__c'
    _description = "Salesforce Lead Sort Columns"
    _rec_name = 'Abbreviation__c'


    Campaign__c     = fields.Many2one('Campaign',string=50)
    Name            = fields.Text('ANS scope',size=80)
    Geographic_Scope_ID__c = fields.Integer('Scope ID')
    # CreatedById already in odoo
    Geographic_Scope_tnk__c = fields.Text('Geographic Scope tnk',size=80)
    # LastModifiedById already in odoo
    OwnerId = fields.Many2one('res.users',string='Owner')
    RecordTypeId = fields.Char('Record Type')