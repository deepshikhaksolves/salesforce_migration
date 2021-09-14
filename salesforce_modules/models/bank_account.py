from odoo import models, fields, api


class BankAccount(models.TransientModel):
    _inherit = 'account.setup.bank.manual.config'
    _description = 'Salesforce Bank account'

    Bank_Branch = fields.Float(string="Agency", digits=(5, 0))
    # Account_Bank__c already in odoo
    Name = fields.Char(string="Bank Account", size=80)
    # CreatedById already in odoo
    Bank_Digit =  fields.Char(string="DV Agency", size=2)
    Account_Digit =  fields.Char(string="DV Counts", size=2)
    # LastModifiedById already in odoo
    Account_id = fields.Many2one('account.account',string="People")
    Account_Type = fields.Selection([
        ('Current','Current'),
        ('Savings','Savings')
    ],string="Account Type")
    OwnerId = fields.Many2one('res.users', string='Owner')