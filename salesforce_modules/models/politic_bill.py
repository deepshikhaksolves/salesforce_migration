from odoo import models, fields, api


class SalesforcePoliticBill(models.Model):

    _name = 'politic.bill'
    _inherit = 'mail.thread'
    _description = 'Salesforce Politic Bill'

    user_id = fields.Many2one('res.users', string="Created By",track_visibility='onchange')
    last_modified_by_id = fields.Many2one('res.users', string="Last Modified By",track_visibility='onchange')
    life = fields.Integer('Número de Vidas',digits=(18, 0),track_visibility='onchange')
    reimbursement_value = fields.Float('Reimbursement Value',digits=(3,2),track_visibility='onchange')
    consultation_reimbursement = fields.Float('Consultation Reimbursement',digits=(16,2),track_visibility='onchange')
    unitary_value = fields.Float('Unitary value',digits=(16,2),track_visibility='onchange')
    owner_id = fields.Many2one('account.account', string='Owner',track_visibility='onchange')
    plan_id = fields.Many2one('product.product', 'Plano',track_visibility='onchange')
    reimbursement_value_type = fields.Selection([
        ('Fixed', 'Fixed'),
        ('Percentage', 'Percentage'),
    ], string="Reimbursement Value Type",track_visibility='onchange')
    rule_note = fields.Char('Rule note',size=200,track_visibility='onchange')