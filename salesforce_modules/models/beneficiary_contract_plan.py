from odoo import models, fields, api


class BeneficiaryContractedPlan(models.Model):
    _name = 'beneficiary.contract.plan'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Salesforce Beneficiary Contracted Plan'
    _rec_name = 'Name'

    beneficiary_id = fields.Many2one('model_beneficiary',string="Recipient", track_visibility='onchange')
    # CreatedById already in odoo
    Name = fields.Char('Contracted Plan Code', track_visibility='onchange')
    end_date = fields.Date('End date Effective', track_visibility='onchange')
    End_date_Adm = fields.Date('End date Admin term', track_visibility='onchange')
    start_date = fields.Date('Start date', track_visibility='onchange')
    start_date_adm = fields.Date('Start Date Effectiveness Adm', track_visibility='onchange')
    # LastModifiedById already in odoo
    reason_for_cancellation = fields.Selection([
        ('Cost', 'Cost'),
        ('service team', 'service team'),
        ('Operational', 'Operational'),
        ('Accredited network', 'Accredited network'),
        ('insurance company', 'insurance company'),
        ('Service','Service')
    ], string="Reason for Cancellation", track_visibility='onchange')

    reason_for_beneficial_inclusion_id = fields.Many2one('model_reason_for_beneficial', string='Reason for Beneficiary Inclusion', track_visibility='onchange')
    OwnerId = fields.Many2one('res.users', string="Owner", track_visibility='onchange')
    contracted_plan_id = fields.Many2one('model_contract_plan', string='Contracted Plane', track_visibility='onchange')