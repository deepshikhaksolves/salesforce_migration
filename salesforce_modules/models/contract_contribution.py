from odoo import models, fields, api

class ContractContribution(models.Model):
    _name = 'contract.contribution'

    coments = fields.Char(string='Comments', size=255, )
    name = fields.Char(string='Contract Contributory')
    contract_id = fields.Many2one('hr.contract', string='Contract')
    # CreatedById created by default
    # LastModifiedById created by default
    owner_id = fields.Many2one('res.users', string='Owner')
    Plan = fields.Many2one('model_contract_plan', string='Plano')
    type_of_beneficiary = fields.Selection([
        ('holder', 'Holder'), ('dependente', 'Dependente')
    ], string='Type of Beneficiary')
    value_type = fields.Selection([
        ('fixed', 'Fixed'), ('percentage', 'Percentage')
    ], string='Value Type')
    Value = fields.Float(string='Value')