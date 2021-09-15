from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class RevenueProvisioning(models.Model):
    _name = 'model_revenue_provisioning'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Salesforce Revenue Provisioning'
    _rec_name = 'Name'

    Contract_id = fields.Many2one('hr.contract', string="Contract")
    # CreatedById already in odoo
    # LastModifiedById already in odoo
    Description = fields.Char(string="Description", size=155)
    OwnerId = fields.Many2one('res.users', string="Owner")
    Periodicity_id = fields.Many2one('model.periodicity',string="Frequency")
    First_Month = fields.Date(string="First month")
    Name = fields.Char(string="Revenue Provisioning")
    Number_Of_Installments = fields.Float(string="Number of installments", digits=(3, 0))
    Revenue_id = fields.Many2one('model_revenue_compensation', string="Revenue")
    Status = fields.Selection([
        ('Pendant','Pendant'),
        ('accrued revenue','accrued revenue'),
        ('Approved','Approved')
    ], string="Status")
    Compensation_Type = fields.Selection([
        ('percentage','Percentage'),
        ('Value','Value')
    ], string="Type of Remuneration")
    Compensation_Value = fields.Float(string="Remunerated Value", digits=(16,2))
    First_Month_Due = fields.Date(string="First Month Expiration")
    Last_Month  = fields.Date(string="Last month")

