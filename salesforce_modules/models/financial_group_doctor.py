from odoo import models, fields, api


class FinancialGroupDoctor(models.Model):
    _name = 'financial_doctor'
    _description = "Salesforce Financial doctor"
    _rec_name = 'name'


    active  = fields.Boolean('Active')
    # CreatedById already in odoo
    name        = fields.Char('Medical User Code')
    financial_group_id   = fields.Many2one('model_financial_group', string='Financial Group')
    email_id = fields.Char('ID')
    # LastModifiedById already in odoo
    OwnerId     = fields.Many2one('res.users',string='Owner')
