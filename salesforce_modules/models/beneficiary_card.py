from odoo import models, fields, api


class BeneficiaryCard(models.Model):
    _name = 'model_beneficiary_card'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Salesforce Beneficiary Card'
    _rec_name = 'Name'

    beneficiary = fields.Many2one('model_beneficiary', string="Recipient", track_visibility='onchange')
    blocked = fields.Boolean(string="locked", track_visibility='onchange')
    # CreatedById already in odoo
    card_code = fields.Char(string="Card Code", size=100, track_visibility='onchange')
    Name = fields.Char(string="Card Code", size=80, track_visibility='onchange')
    cancellation_date = fields.Date(string="Cancellation Date", track_visibility='onchange')
    end_term = fields.Date(string="End of Term", track_visibility='onchange')
    home_term = fields.Date(string="Beginning of Term", track_visibility='onchange')
    # LastModifiedById already in odoo
    OwnerId = fields.Many2one('res.users', string='Owner', track_visibility='onchange')
    Status = fields.Selection([
        ('Active', 'Active'),
        ('Called off', 'Called off')
    ], string="Status", track_visibility='onchange')
    type_special_beneficiary = fields.Selection([
        ('Holder', 'Holder'),
        ('Dependent', 'Dependent')
    ], string="Special Beneficiary Type", track_visibility='onchange')
    cost_center_ids = fields.One2many('model_cost_center', 'beneficiary_card_id', string='Cost Center IDS')
