from odoo import models, fields, api


class PortalAccess(models.Model):
    _name = 'portal.access'
    _inherit = 'mail.thread'

    access_code__c = fields.Char(string='Access Code', size=255)
    access_type__c = fields.Selection([
        ('file', 'Files'), ('service', 'Service'), ('quotation', 'Quotation'), ('billing', 'Billing'), ('financial', 'Financial'), ('implantation', 'Implantation'), ('movement', 'Movement'), ('reembolso', 'Reembolso')
    ], string='Access Type')
    access_users__c = fields.Selection([
        ('financial', 'Financial'), ('risk_management', 'Risk Management'), ('deployment', 'Deployment'), ('operational', 'Operational'), ('placement', 'Placement'), ('relationship', 'Relationship')
    ], string='Access Users')

    administrator__c = fields.Many2one('account.account', string='Administrator')
    carrier_id = fields.Many2one('account.account', string='Carrier')
    contract__c = fields.Many2one('account.account', string='Contract')
    contract_summary__c = fields.Char(string='Contract Summary')
    user_id = fields.Many2one('res.users', string="Created By")
    last_modified_by_id = fields.Many2one('res.users', string="Last Modified By")
    financial_group_id = fields.Many2one('model_financial_group', string='Financial Group')
    login__c = fields.Char(string='Login', size=255)
    OwnerId = fields.Many2one('res.partner', string='Owner')
    password__c = fields.Char(string='Password', size=255)
    registered_email__c = fields.Char(string='Registered email')
    site__c = fields.Char(string='Site', size=255)
    attachment_lines = fields.One2many('ir.attachment','portal_access_id',string="Attachment Lines")

    account_id = fields.Many2one('account.account', string='Account Id')