from odoo import models, fields, api


class Beneficiary(models.Model):
    _name = 'model_beneficiary'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Salesforce Beneficiary'
    _rec_name = 'Name'

    Name = fields.Char(string="Recipient", track_visibility='onchange')
    contact = fields.Boolean(string="Ticket", track_visibility='onchange')
    cost_center_id = fields.Many2one('model_cost_center', string="Cost center", track_visibility='onchange')
    client_id = fields.Many2one('account.account', string="Customer", track_visibility='onchange')
    contract_id = fields.Many2one('hr.contract', string="Contract", track_visibility='onchange')
    temporary_contract_id = fields.Many2one('hr.contract', string="Temporary contract", track_visibility='onchange')
    # CreatedById already in odoo
    admission_date = fields.Date(string="Admission date", track_visibility='onchange')
    date_of_departure = fields.Date(string="Leave Date", track_visibility='onchange')
    resignation_date = fields.Date(string="Dismissal Date", track_visibility='onchange')
    return_date = fields.Date(string="Return Date", track_visibility='onchange')
    description = fields.Char(string="Description", size=1500, track_visibility='onchange')
    code_eligibility = fields.Char(string="Eligibility code", size=100, track_visibility='onchange')
    end_suspension = fields.Date(string="End Suspension", track_visibility='onchange')
    degree_of_kinship = fields.Selection([
        ('Spouse', 'Spouse'),
        ('Companion', 'Companion'),
        ('Son (a)', 'Son (a)'),
        ('stepson', 'Stepson'),
        ('Aggregate', 'Aggregate')
    ], string="Degree of kinship", track_visibility='onchange')
    suspension_start = fields.Date(string="Start of suspension", track_visibility='onchange')
    # LastModifiedById already in odoo
    Limit = fields.Float(string="Limit", track_visibility='onchange')
    registration = fields.Char(string="Enrollment", size=100, track_visibility='onchange')
    currency = fields.Float(string="Currency", track_visibility='onchange')
    OwnerId = fields.Many2one('res.users', string='Owner', track_visibility='onchange')
    has_liminal = fields.Boolean(string="Has Preliminary", track_visibility='onchange')
    RecordTypeId = fields.Char(string='Record Type', track_visibility='onchange')
    retain_billing = fields.Boolean(string="Retain Billing", track_visibility='onchange')
    balance = fields.Float(string="Balance", track_visibility='onchange')
    additional_salary = fields.Float(string="Additional Salary", track_visibility='onchange')
    status = fields.Selection([('Active','Active'),('Called off','Called off')], string="Status", track_visibility='onchange')
    holder = fields.Many2one('model_beneficiary', string="Headline", track_visibility='onchange')
