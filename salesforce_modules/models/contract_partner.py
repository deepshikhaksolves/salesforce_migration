from odoo import models, fields, api


class SalesforceContractPartner(models.Model):

    _name = 'contract.partner'
    _inherit = 'mail.thread'
    _description = 'Salesforce Contract Partner'

    contract_id = fields.Many2one('hr.contract', 'Contract',track_visibility='onchange')
    user_id = fields.Many2one('res.users', string="Created By",track_visibility='onchange')
    start_date = fields.Date('Start date',track_visibility='onchange')
    end_date = fields.Date('Data Final',track_visibility='onchange')
    role = fields.Selection([
        ('Corretor Estratégico', 'Corretor Estratégico'),
        ('Parceiro Estratégico', 'Parceiro Estratégico'),
    ], string="Occupation",track_visibility='onchange')
    last_modified_by_id = fields.Many2one('res.users', string="Last Modified By",track_visibility='onchange')
    partner_id = fields.Many2one('account.account', string='Partner',track_visibility='onchange')
    owner_id = fields.Many2one('account.account', string='Owner',track_visibility='onchange')
    name = fields.Char('Parceiro do Contrato',track_visibility='onchange')
    opportunity_id = fields.Many2one('crm.lead', string="Opportunity",track_visibility='onchange')
