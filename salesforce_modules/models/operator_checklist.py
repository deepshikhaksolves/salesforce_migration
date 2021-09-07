from odoo import models, fields, api


class OperatorChecklist(models.Model):
    _name = 'model_operator_checklist'
    _description = "Salesforce Operator Checklist"
    _rec_name = 'Name'

    # CreatedById already in odoo
    # LastModifiedById already in odoo
    Name                    = fields.Char('Name Operator Checklist',size=80)
    operator__c             = fields.Many2one('account.account',string='Operator')
