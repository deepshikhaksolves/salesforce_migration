from odoo import models, fields, api


class SalesforcePayingCompany(models.Model):

    _name = 'paying.company'
    _description = 'Salesforce Paying Company'

    user_id = fields.Many2one('res.users', string="Created By")
    last_modified_by_id = fields.Many2one('res.users', string="Last Modified By")
    owner_id = fields.Many2one('account.account', string='Owner')
    carrier_id = fields.Many2one('account.account', string='Carrier')
    account_id = fields.Many2one('account.account', string='Account')
    name = fields.Char('Code', size=80)