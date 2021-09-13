from odoo import models, fields, api

class FinancialGroupMasterUser(models.Model):
    _name = 'financial_group_master_user'
    _description = "Salesforce Financial Group Master User"
    _rec_name = 'name'

    active  = fields.Boolean('Active')
    # CreatedById already in odoo
    financial_group_id   = fields.Many2one('model_financial_group', string='Financial Group')
    email_id = fields.Char('ID')
    # LastModifiedById already in odoo
    name        = fields.Char('Master User')
    OwnerId     = fields.Many2one('res.users',string='Owner')
