from odoo import models, fields, api


class RevenueCompensation(models.Model):
    _name = 'model_revenue_compensation'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Salesforce Revenue Compensation'
    _rec_name = 'Name'

    # CreatedById already in odoo
    Endorsement_Code = fields.Char(string="Endorsement Code", size=100,track_visibility='onchange')
    # LastModifiedById already in odoo
    Lot = fields.Float(string="Batch",track_visibility='onchange')
    OwnerId = fields.Many2one('res.users', string="Owner",track_visibility='onchange')
    Percentage_of_Revenue_Paid = fields.Float(string="Percentage of Paid Revenue",track_visibility='onchange')
    Percentage_of_Provisioned_Revenue = fields.Float(string="Percentage of Provisioned Revenue",track_visibility='onchange')
    Revenue_Provisioning = fields.Many2one('model_revenue_provisioning', string="Revenue Provisioning",track_visibility='onchange')
    Received = fields.Date(string="Receivement",track_visibility='onchange')
    Name = fields.Char(string="Revenue remuneration",track_visibility='onchange')
    Comission_Hold = fields.Boolean(string="retain commission",track_visibility='onchange')
    Status = fields.Selection([
        ('provisioned', 'provisioned'),
        ('downloaded', 'downloaded'),
        ('Called off', 'Called off')
    ], string="Status",track_visibility='onchange')
    Amount_of_Revenue_Paid = fields.Float(string="Amount of Paid Revenue",track_visibility='onchange')
    Provisioned_Revenue_Amount = fields.Float(string="Amount of Provisioned Revenue",track_visibility='onchange')
    Premium_Amount_Paid = fields.Float(string="Premium Value Paid",track_visibility='onchange')
    Provisioned_Premium_Amount = fields.Float(string="Provisioned Premium Value",track_visibility='onchange')
