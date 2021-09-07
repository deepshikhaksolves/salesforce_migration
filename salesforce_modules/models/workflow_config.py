from odoo import models, fields, api

class WorkflowConfig(models.Model):
    _name = 'workflow_configuration'
    _description = "Salesforce Workflow configuration"
    _rec_name = 'Name'

    ObjectStatusField__c    = fields.Char('Object Status field',size=255)
    # CreatedById  already in odoo
    Description__c          = fields.Char('Description',size=32768)
    # LastModifiedById  already in odoo
    Name                    = fields.Char('Name',size=80)
    Workflow_Standard_of_Object__c  = fields.Boolean('Objects Standard Workflow')
    Object__c               = fields.Char('Object',size=255)
    OwnerId                 = fields.Many2one('res.users',string='Owner')
    RecordType__c           = fields.Char('RecordType',size=255)
    RecordTypeId__c         = fields.Char('RecordTypeId',size=100)
    Initial_Status__c       = fields.Char('Status Inicial',size=255)
