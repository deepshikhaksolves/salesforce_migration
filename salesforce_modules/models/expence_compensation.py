from odoo import models, fields, api


class ExpenceCompensation(models.Model):
    _name = 'hr.expense'
    _inherit = ['hr.expense', 'mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Expence Compensation"

    # CreatedById already in odoo
    # Payment_Day already in odoo i.e. (date)
    # LastModifiedById already in odoo
    Internal_Extract_Number = fields.Float(string='Internal Statement Number', digits=(18, 0))
    OwnerId = fields.Many2one('res.users', string='Owner')
    Percentage_of_Comission_Paid = fields.Float(string='Percentage of Commission Paid', digits=(16, 2))
    Percentage_of_Provisioned_Comission = fields.Float(string='Percentage of the Provisioned Commission',
                                                       digits=(16, 2))
    Expense_Provisioning_id = fields.Many2one('expence_provisioning', string='Expense Provisioning')
    # name(Expense Compensation)                    already in odoo i.e. (name)
    Revenue_Compensation_id = fields.Many2one('model_revenue_compensation', string='Revenue remuneration')
    Status = fields.Selection(
        [('provisioned', 'provisioned'), ('Delete', 'Delete'), ('Paid out', 'Paid out'), ('Called off', 'Called off')],
        'Status')
    Value_of_Comission_Paid = fields.Float(string='Amount of Commission Paid', digits=(16, 2))
    Value_of_Provisioned_Commission = fields.Float(string='Value of the Provisioned Commission', digits=(16, 2))
    Premium_Amount_Paid = fields.Float(string='Premium Value Paid', digits=(16, 2))
    Provisioned_Premium_Amount = fields.Float(string='Provisioned Premium Value', digits=(16, 2))
