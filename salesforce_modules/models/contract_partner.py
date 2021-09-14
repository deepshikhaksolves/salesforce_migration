from odoo import models, fields, api


class SalesforceContractPartner(models.Model):

    _name = 'contract.partner'
    _description = 'Salesforce Contract Partner'

    contract_id = fields.Many2one('hr.contract', 'Contract')
    user_id = fields.Many2one('res.users', string="Created By")
    start_date = fields.Date('Start date')
    end_date = fields.Date('Data Final')
    role = fields.Selection([
        ('Corretor Estratégico', 'Corretor Estratégico'),
        ('Parceiro Estratégico', 'Parceiro Estratégico'),
    ], string="Role")
    last_modified_by_id = fields.Many2one('res.users', string="Last Modified By")
    partner_id = fields.Many2one('account.account', string='Partner Account')
    owner_id = fields.Many2one('account.account', string='Owner')
    name = fields.Char('Parceiro do Contrato')
    opportunity_id = fields.Many2one('crm.lead', string="Opportunity")
