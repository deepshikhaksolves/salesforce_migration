from odoo import models, fields, api


class CoastCenter(models.Model):
    _name = 'model_cost_center'
    _description = "Salesforce Cost Center"
    _rec_name = 'name'


    beneficiary_id          = fields.Many2one('comodel_name', string='Recipient')
    beneficiary_card_id     = fields.Many2one('comodel_name', string='Beneficiary Card')
    cost_center             = fields.Char('Cost center', size=255)
    name                    = fields.Char('Cost Center ID')
    contract_id             = fields.Many2one('hr.contract', string='Contract')
    # CreatedById already in odoo
    end_term                = fields.Date('End of Term')
    financial_group_id      = fields.Many2one('model_financial_group', string='Financial Group ID')
    home_term               = fields.Date('Beginning of Term')
    # LastModifiedById already in odoo
    OwnerId                 = fields.Many2one('res.users',string='Owner')
    status                  = fields.Selection([('Active','Active'),('Cancellation','Cancellation')],'Status')
