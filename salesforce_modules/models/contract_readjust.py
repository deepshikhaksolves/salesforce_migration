from odoo import models, fields, api

class ContractReadjust(models.Model):
    _name = 'contract.readjust'
    _inherit = 'mail.thread'
    

    Calculated_Claim_Readjustment_Index = fields.Float(string='Calculated Claim Readjustment Index', digits=(4, 2))
    Comment = fields.Text(string='Comment')
    Contracts = fields.Many2one('hr.contract', string='Contracts')
    # CreatedById created default
    readjustment_base_date = fields.Date(string='Base Date Readjustment')
    Negotiated_Date = fields.Date(string='Date negotiated')
    Calculation_End = fields.Date(string='End Calculation')
    Caculation_Start = fields.Date(string='Start of Calculation')
    # LastModifiedById created default
    Applied_Month = fields.Date(string='Application Month')
    OwnerId = fields.Date(string='Owner')
    Readjustment_Applied = fields.Selection([
        ('readjusted', 'readjusted'), ('Contribution', 'Contribution'), ('Discount', 'Discount'), ('Free', 'Free'), ('Postponed', 'Postponed')
    ], string='Applied readjustment')
    Name = fields.Char(string='Readjustment of Contract ID')
    Status = fields.Selection([
        ('readjusted', 'readjusted'), ('Contribution', 'Contribution'), ('Discount', 'Discount'), ('Postponed', 'Postponed')
    ], string='Status')
    Applied_Financial_Support_Value = fields.Float(string='Applied Financial Support', digits=(9, 2))
    Calculated_Financial_Support = fields.Float(string='Calculated Financial Support', digits=(9, 2))
    Calculated_Composite_Readjustment_Index = fields.Float(string='Composite Adjustment Calculated Index', digits=(4, 2))
    Applied_Readjustment_Index = fields.Float(string='Applied Adjustment Index', digits=(4, 2))
    Calculated_Financial_Readjustment_Index = fields.Float(string='Calculated Financial Readjustment Ratio', digits=(4, 2))

