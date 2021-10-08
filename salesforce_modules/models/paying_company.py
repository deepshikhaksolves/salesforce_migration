from odoo import models, fields, api


class SalesforcePayingCompany(models.Model):
    _name = 'paying.company'
    _inherit = 'mail.thread'
    _description = 'Salesforce Paying Company'

    user_id = fields.Many2one('res.users', string="Created By",track_visibility='onchange')
    last_modified_by_id = fields.Many2one('res.users', string="Last Modified By",track_visibility='onchange')
    owner_id = fields.Many2one('account.account', string='Owner',track_visibility='onchange')
    carrier_id = fields.Many2one('account.account', string='Carrier',track_visibility='onchange')
    account_id = fields.Many2one('account.account', string='Account',track_visibility='onchange')
    name = fields.Char('Code', size=80,track_visibility='onchange')
