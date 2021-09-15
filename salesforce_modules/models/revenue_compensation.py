from odoo import models, fields, api


class RevenueCompensation(models.Model):
    _name = 'model_revenue_compensation'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Salesforce Revenue Compensation'
    _rec_name = 'Name'

    # CreatedById already in odoo
    Endorsement_Code = fields.Char(string="Endorsement Code", size=100)
    # LastModifiedById already in odoo
    Lot = fields.Float(string="Batch")
    OwnerId = fields.Many2one('res.users', string="Owner")
    Percentage_of_Revenue_Paid = fields.Float(string="Percentage of Paid Revenue")
    Percentage_of_Provisioned_Revenue = fields.Float(string="Percentage of Provisioned Revenue")
    Revenue_Provisioning = fields.Many2one('model_revenue_provisioning', string="Revenue Provisioning")
    Received = fields.Date(string="Receivement")
    Name = fields.Char(string="Revenue remuneration")
    Comission_Hold = fields.Boolean(string="retain commission")
    Status = fields.Selection([
        ('provisioned', 'provisioned'),
        ('downloaded', 'downloaded'),
        ('Called off', 'Called off')
    ], string="Status")
    Amount_of_Revenue_Paid = fields.Float(string="Amount of Paid Revenue")
    Provisioned_Revenue_Amount = fields.Float(string="Amount of Provisioned Revenue")
    Premium_Amount_Paid = fields.Float(string="Premium Value Paid")
    Provisioned_Premium_Amount = fields.Float(string="Provisioned Premium Value")
