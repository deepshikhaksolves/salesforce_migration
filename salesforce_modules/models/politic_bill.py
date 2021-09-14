from odoo import models, fields, api


class SalesforcePoliticBill(models.Model):

    _name = 'politic.bill'
    _inherit = 'mail.thread'
    _description = 'Salesforce Politic Bill'

    user_id = fields.Many2one('res.users', string="Created By")
    last_modified_by_id = fields.Many2one('res.users', string="Last Modified By")
    life = fields.Integer('Número de Vidas',digits=(18, 0))
    reimbursement_value = fields.Float('Reimbursement Value',digits=(3,2))
    consultation_reimbursement = fields.Float('Consultation Reimbursement',digits=(16,2))
    unitary_value = fields.Float('Unitary value',digits=(16,2))
    owner_id = fields.Many2one('account.account', string='Owner')
    plan_id = fields.Many2one('product.product', 'Plano')
    reimbursement_value_type = fields.Selection([
        ('Fixed', 'Fixed'),
        ('Percentage', 'Percentage'),
    ], string="Reimbursement Value Type")
    rule_note = fields.Char('Rule note',size=200)