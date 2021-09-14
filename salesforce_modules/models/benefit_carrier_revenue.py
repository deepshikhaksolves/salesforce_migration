from odoo import models, fields, api


class BenefitCarrierRevenue(models.Model):
    _name = 'model_beneficiary_carrier_revenue'
    _description = 'Salesforce Beneficiary Carrier Revenue'
    _rec_name = 'Name'

    Name = fields.Char(string="Benefit Carrier Revenue Name", size=80)
    carrier_id = fields.Many2one('account.account', string="Carrier")
    # CreatedById already in odoo
    # LastModifiedById already in odoo
    OwnerId = fields.Many2one('res.users', string='Owner')
    Paid_by = fields.Selection([
        ('percentage','Percentage'),
        ('value','Value')
    ],string="Paid by")
    # Revenue_id = fields.Many2one('Receita',string="Revenue") #Model not found
    Revenue_Value = fields.Float(string="Revenue Value", digits=(16, 2))

