from odoo import models, fields, api


class BeneficiaryCarrier(models.Model):
    _name = 'model_beneficiary_carrier'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Salesforce Beneficiary Carrier'

    Benefits =  fields.Selection([
        ('health','Health'),
        ('Dental','Dental'),
        ('life','Life'),
        ('medicine','Medicine'),
        ('Personal_Accidents','Personal Accident'),
        ('In_Company','Consultancy'),
        ('Medical_Consulting','Medical Consulting'),
        ('Meal','Snack'),
        ('Food','Food'),
        ('transportation','Transport'),
        ('pension','Pension'),
        ('Travel','Travel'),
        ('Car_Fleet','Fleet'),
        ('Car','Car'),
        ('Fuel','Fuel'),
        ('Occupational_Health','Occupational Health'),
        ('Checkup','Checkup'),
        ('Vaccine','Vaccine'),
        ('I_protected','I Protected'),
        ('Fee','Fee')
    ],string="Benefit")
    Name =  fields.Char(string="Operator Benefit", size=80)
    # CreatedById already in odoo
    # LastModifiedById already in odoo
    carrier_id = fields.Many2one('account.account', string="Operator")
    OwnerId = fields.Many2one('res.users', string='Owner')