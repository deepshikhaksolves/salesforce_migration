from odoo import models, fields, api

class FinancialAgreement(models.Model):
    _name = 'financial_agreement'
    _description = "Salesforce Financial Agreement"
    _rec_name = 'name'

    # CreatedById  already in odoo
    name = fields.Char('Financial Agreement ID')
    # LastModifiedById  already in odoo
    OwnerId = fields.Many2one('res.users',string='Owner')
    Automatic_Rule = fields.Float(string='Automatic Rule',digits=(18,0))
    status = fields.Selection([('Under Analysis', 'Under Analysis'),('In Technical Approval', 'In Technical Approval'),('provisioned', 'provisioned'),('Manually Provisioned', 'Manually Provisioned'),('returned', 'returned')],'Status')

