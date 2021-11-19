from odoo import models, fields, api


class WorkflowConfig(models.Model):
    _name = 'workflow_configuration'
    _description = "Salesforce Workflow configuration"
    _rec_name = 'Name'

    ObjectStatusField_c = fields.Char('Object Status field', size=255)
    # CreatedById  already in odoo
    Description_c = fields.Char('Description', size=32768)
    # LastModifiedById  already in odoo
    Name = fields.Char('Name', size=80)
    Workflow_Standard_of_Object_c = fields.Boolean('Objects Standard Workflow')
    Object_c = fields.Char('Object', size=255)
    OwnerId = fields.Many2one('res.users', string='Owner')
    RecordType_c = fields.Char('RecordType', size=255)
    RecordTypeId_c = fields.Char('RecordTypeId', size=100)
    Initial_Status_c = fields.Char('Status Inicial', size=255)
