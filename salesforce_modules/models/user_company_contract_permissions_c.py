from odoo import models, fields, api


class FinancialGroup(models.Model):
    _name = 'financial_group'
    _description = "Salesforce Corporate User Agreement Jurisdiction"
    _rec_name = 'name'

    name = fields.Char('Name')


class UserAgreement(models.Model):
    _name = 'user_company_contract_permissions__c'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Corporate User Agreement Jurisdiction"
    _rec_name = 'id__c'

    contract__c = fields.Many2one('hr.contract', string='Contract',track_visibility='onchange')
    # CreatedById  already in odoo
    financial_group__c = fields.Many2one('financial_group', string='Financial Group',track_visibility='onchange')
    id__c = fields.Char(string='ID',track_visibility='onchange')
    # LastModifiedById already in odoo
    OwnerId = fields.Many2one('res.users', string='Owner',track_visibility='onchange')
    RecordTypeId = fields.Char('Record Type',track_visibility='onchange')
    status__c = fields.Selection([('Active', 'Active'), ('Inactive', 'Inactive')], 'Status',track_visibility='onchange')
    Name = fields.Char('User Permission ID',track_visibility='onchange')
