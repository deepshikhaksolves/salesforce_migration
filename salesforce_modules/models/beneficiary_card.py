from odoo import models, fields, api


class BeneficiaryCard(models.Model):
    _name = 'model_beneficiary_card'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Salesforce Beneficiary Card'

    beneficiary = fields.Many2one('model_beneficiary', string="Recipient")
    blocked = fields.Boolean(string="locked")
    # CreatedById already in odoo
    card_code = fields.Char(string="Card Code", size=100)
    Name = fields.Char(string="Card Code", size=80)
    cancellation_date = fields.Date(string="Cancellation Date")
    end_term = fields.Date(string="End of Term")
    home_term = fields.Date(string="Beginning of Term")
    # LastModifiedById already in odoo
    OwnerId = fields.Many2one('res.users', string='Owner')
    Status = fields.Selection([
        ('Active', 'Active'),
        ('Called off', 'Called off')
    ], string="Status")
    type_special_beneficiary = fields.Selection([
        ('Holder', 'Holder'),
        ('Dependent', 'Dependent')
    ], string="Special Beneficiary Type")
