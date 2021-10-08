from odoo import models, fields, api


class PortalAccess(models.Model):
    _name = 'portal.access'
    _inherit = 'mail.thread'

    access_code__c = fields.Char(string='Access Code', size=255,track_visibility='onchange')
    access_type__c = fields.Selection([
        ('file', 'Files'), ('service', 'Service'), ('quotation', 'Quotation'), ('billing', 'Billing'), ('financial', 'Financial'), ('implantation', 'Implantation'), ('movement', 'Movement'), ('reembolso', 'Reembolso')
    ], string='Access Type',track_visibility='onchange')
    access_users__c = fields.Selection([
        ('financial', 'Financial'), ('risk_management', 'Risk Management'), ('deployment', 'Deployment'), ('operational', 'Operational'), ('placement', 'Placement'), ('relationship', 'Relationship')
    ], string='Access Users',track_visibility='onchange')

    administrator__c = fields.Many2one('account.account', string='Administrator',track_visibility='onchange')
    carrier_id = fields.Many2one('account.account', string='Carrier',track_visibility='onchange')
    contract__c = fields.Many2one('account.account', string='Contract',track_visibility='onchange')
    contract_summary__c = fields.Char(string='Contract Summary',track_visibility='onchange')
    user_id = fields.Many2one('res.users', string="Created By",track_visibility='onchange')
    last_modified_by_id = fields.Many2one('res.users', string="Last Modified By",track_visibility='onchange')
    financial_group_id = fields.Many2one('model_financial_group', string='Financial Group',track_visibility='onchange')
    login__c = fields.Char(string='Login', size=255,track_visibility='onchange')
    OwnerId = fields.Many2one('res.partner', string='Owner',track_visibility='onchange')
    password__c = fields.Char(string='Password', size=255,track_visibility='onchange')
    registered_email__c = fields.Char(string='Registered email',track_visibility='onchange')
    site__c = fields.Char(string='Site', size=255,track_visibility='onchange')
    attachment_lines = fields.One2many('ir.attachment','portal_access_id',string="Attachment Lines")

    account_id = fields.Many2one('account.account', string='Account Id',track_visibility='onchange')