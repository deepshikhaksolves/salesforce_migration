from odoo import models, fields, api


class BenefitCarrierRevenue(models.Model):
    _name = 'model_beneficiary_carrier_revenue'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Salesforce Beneficiary Carrier Revenue'
    _rec_name = 'Name'

    Name = fields.Char(string="Benefit Carrier Revenue Name", size=80, track_visibility='onchange')
    carrier_id = fields.Many2one('account.account', string="Carrier", track_visibility='onchange')
    # CreatedById already in odoo
    # LastModifiedById already in odoo
    OwnerId = fields.Many2one('res.users', string='Owner', track_visibility='onchange')
    Paid_by = fields.Selection([
        ('percentage', 'Percentage'),
        ('value', 'Value')
    ], string="Paid by", track_visibility='onchange')
    Revenue_id = fields.Many2one('revenue_compensation', string="Revenue", track_visibility='onchange')
    Revenue_Value = fields.Float(string="Revenue Value", track_visibility='onchange')
