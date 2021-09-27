from odoo import models, fields, api


class BankAccount(models.TransientModel):
    _name = 'account.setup.bank.manual.config'
    _inherit = ['account.setup.bank.manual.config', 'mail.thread', 'mail.activity.mixin']
    _description = 'Salesforce Bank account'

    Bank_Branch = fields.Float(string="Agency", track_visibility='onchange')
    # Account_Bank__c already in odoo as acc_number
    Name = fields.Char(string="Bank Account", size=80, track_visibility='onchange')
    # CreatedById already in odoo
    Bank_Digit = fields.Char(string="DV Agency", size=2, track_visibility='onchange')
    Account_Digit = fields.Char(string="DV Counts", size=2, track_visibility='onchange')
    # LastModifiedById already in odoo
    Account_id = fields.Many2one('account.account', string="People", track_visibility='onchange')
    Account_Type = fields.Selection([
        ('Current', 'Current'),
        ('Savings', 'Savings')
    ], string="Account Type", track_visibility='onchange')
    OwnerId = fields.Many2one('res.users', string='Owner', track_visibility='onchange')
