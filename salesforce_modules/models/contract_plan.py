from odoo import models, fields, api


class ContractPlan(models.Model):
    _name = 'model_contract_plan'
    _description = "Salesforce Coverage"
    _rec_name = 'Abbreviation__c'


    Abbreviation__c = fields.Char('Abbreviation',size=50)
    Name            = fields.Char('ANS scope',size=80)
    Geographic_Scope_ID__c = fields.Integer('Scope ID')
    # CreatedById already in odoo
    Geographic_Scope_tnk__c = fields.Char('Geographic Scope tnk',size=80)
    # LastModifiedById already in odoo
    OwnerId = fields.Many2one('res.users',string='Owner')
    RecordTypeId = fields.Char('Record Type')