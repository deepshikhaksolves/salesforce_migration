from odoo import models, fields, api


class Beneficiary(models.Model):
    _name = 'model_beneficiary'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Salesforce Beneficiary'

    Name =fields.Char(string="Recipient")
    contact = fields.Boolean(string="Ticket")
    # cost_center_id = fields.Many2one('Cost Center', string="Cost center") #Model not found
    client_id = fields.Many2one('account.account', string="Customer")
    contract_id = fields.Many2one('hr.contract', string="Contract")
    temporary_contract_id = fields.Many2one('hr.contract',string="Temporary contract")
    # CreatedById already in odoo
    admission_date = fields.Date(string="Admission date")
    date_of_departure =  fields.Date(string="Leave Date")
    resignation_date = fields.Date(string="Dismissal Date")
    return_date = fields.Date(string="Return Date")
    description = fields.Char(string="Description", size=1500)
    code_eligibility = fields.Char(string="Eligibility code", size=100)
    end_suspension = fields.Date(string="End Suspension")
    degree_of_kinship = fields.Selection([
        ('Spouse','Spouse'),
        ('Companion','Companion'),
        ('Son (a)','Son (a)'),
        ('stepson','Stepson'),
        ('Aggregate','Aggregate')
    ],string="Degree of kinship")
    suspension_start = fields.Date(string="Start of suspension")
    # LastModifiedById already in odoo
    Limit = fields.Float(string="Limit", digits=(16, 2))
    registration = fields.Char(string="Enrollment", size=100)
    currency = fields.Float(string="Currency", digits=(16, 2))
    OwnerId = fields.Many2one('res.users', string='Owner')
    has_liminal = fields.Boolean(string="Has Preliminary")
    # RecordTypeId =
    retain_billing = fields.Boolean(string="Retain Billing")
    balance =  fields.Float(string="Balance", digits=(16, 2))
    additional_salary = fields.Float(string="Additional Salary", digits=(16, 2))
    status = fields.Selection([], string="Status")
    holder =  fields.Many2one('model_beneficiary',string="Headline")

