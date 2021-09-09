from odoo import models, fields, api


class ContractEligibility(models.Model):
    _name = 'contract_eligibility'
    _description = "Salesforce Contract Eligibility"
    _rec_name = 'name'


    contract_id     = fields.Many2one('hr.contract', string='Contract')
    # CreatedById already in odoo
    Start_Date      = fields.Date('Start date')
    End_Date        = fields.Date('date Final')
    Elegibility_id  = fields.Many2one('model_eligibility', string='Eligibility')
    name            = fields.Char('Elegibility', size=80)
    # LastModifiedById already in odoo
    OwnerId          = fields.Many2one('res.users',string='Owner')
    Contract_Plan_id = fields.Many2one('model_contract_plan', string='Contract Plan')
    