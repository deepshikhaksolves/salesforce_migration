from odoo import models, fields, api


class ExpenceProvisioning(models.Model):
    _name = 'expence_provisioning'
    _description = "Salesforce Expence Provisioning"
    _rec_name = 'name'

    contract_id = fields.Many2one('hr.contract',string='Contract')
    # CreatedById already in odoo
    # LastModifiedById already in odoo
    OwnerId                 = fields.Many2one('res.users',string='Owner')
    Paid_About              = fields.Selection([('Award','Award'),('Revenue','Revenue')],'Payment About')
    user_id                 = fields.Many2one('res.users',string='Internal Participant')
    Participation           = fields.Selection([('Consultant','Consultant'),('Consultant','Consultant'),('Indicator','Indicator'),('Pre-consultant','Pre-consultant'),('Association','Association'),('Business partner','Business partner'),('Manager','Manager'),('Relationship','Relationship')],'Participation')
    Periodicity_id          = fields.Many2one('model.periodicity',string='Frequency')
    Person_id               = fields.Many2one('account.account',string='People')
    First_Month             = fields.Date('First month')
    name                    = fields.Char('Expense Provisioning')
    Revenue_Provisioning_id = fields.Many2one('model_revenue_provisioning',string='Revenue Provisioning')
    Number_Of_Days_After_Billing = fields.Float(string='Number of Days After Billing',digits=(3,0))
    Number_Of_Installments = fields.Float(string='Number of installments',digits=(3,0))
    Income_id = fields.Many2one('account.account',string='Revenue')

    Status                 = fields.Selection([('Pending','Pending'),('Accrued expense','Accrued expense'),('Approved','Approved')],'Status')
    Compensation_Type      = fields.Selection([('Value','Value'),('percentage','percentage')],'Type of Remuneration')

    Commission_Amount = fields.Float(string='Commissioned Value',digits=(16,2))
    Compensation_Value = fields.Float(string='Remunerated Value',digits=(16,2))
    First_Month_Due    = fields.Date('First Month Expiration')
    Last_Month         = fields.Date('Last month')

