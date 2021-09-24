from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class RevenueProvisioning(models.Model):
    _name = 'model_revenue_provisioning'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Salesforce Revenue Provisioning'
    _rec_name = 'Name'

    Contract_id = fields.Many2one('hr.contract', string="Contract",track_visibility='onchange')
    # CreatedById already in odoo
    # LastModifiedById already in odoo
    Description = fields.Char(string="Description", size=155,track_visibility='onchange')
    OwnerId = fields.Many2one('res.users', string="Owner",track_visibility='onchange')
    Periodicity_id = fields.Many2one('model.periodicity',string="Frequency",track_visibility='onchange')
    First_Month = fields.Date(string="First month",track_visibility='onchange')
    Name = fields.Char(string="Revenue Provisioning",track_visibility='onchange')
    Number_Of_Installments = fields.Float(string="Number of installments",track_visibility='onchange')
    Revenue_id = fields.Many2one('model_revenue_compensation', string="Revenue",track_visibility='onchange')
    Status = fields.Selection([
        ('Pendant','Pendant'),
        ('accrued revenue','accrued revenue'),
        ('Approved','Approved')
    ], string="Status",track_visibility='onchange')
    Compensation_Type = fields.Selection([
        ('percentage','Percentage'),
        ('Value','Value')
    ], string="Type of Remuneration",track_visibility='onchange')
    Compensation_Value = fields.Float(string="Remunerated Value",track_visibility='onchange')
    First_Month_Due = fields.Date(string="First Month Expiration",track_visibility='onchange')
    Last_Month  = fields.Date(string="Last month",track_visibility='onchange')

