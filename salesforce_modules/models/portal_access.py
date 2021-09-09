from odoo import models, fields, api

class PortalAccess(models.Model):
    _name = 'portal.access'

    access_code__c = fields.Char(string='Access Code', size=255)
    access_type__c = fields.Selection([
        ('file', 'Files'), ('service', 'Service'), ('quotation', 'Quotation'), ('billing', 'Billing'), ('financial', 'Financial'), ('implantation', 'Implantation'), ('movement', 'Movement'), ('reembolso', 'Reembolso')
    ], string='Access Type')
    access_users__c = fields.Selection([
        ('financial', 'Financial'), ('risk_management', 'Risk Management'), ('deployment', 'Deployment'), ('operational', 'Operational'), ('placement', 'Placement'), ('relationship', 'Relationship')
    ], string='Access Users')

    administrator__c = fields.Many2one('comodel_name', string='Administrator')
    carrier__c = fields.Many2one('comodel_name', string='Carrier')
    contract__c = fields.Many2one('comodel_name', string='Contract')
    contract_summary__c = fields.Char(string='Contract Summary')
    # Created By created default
    financial_group__c = fields.Many2one('comodel_name', string='Financial Group')
    # LastModifiedById created default
    login__c = fields.Char(string='Login', size=255)
    OwnerId = fields.Many2one('res.partner', string='owner')
    password__c = fields.Char(string='password', size=255)
    registered_email__c = fields.Char(string='Registered email')
    site__c = fields.Char(string='Site', size=255)
    
     


    