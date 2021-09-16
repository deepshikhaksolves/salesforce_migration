from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class StudyConfiguration(models.Model):
    _name = 'study_configuration'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Study Configuration C"
    _rec_name = 'Name'

    active = fields.Boolean(string="Active")
    # CreatedById already in odoo
    default_owner_id = fields.Many2one('res.users', string="Default Owner")
    Show_Aggregate = fields.Boolean(string="Show Aggregate")
    show_dependent = fields.Boolean(string="Display Dependent")
    maximum_age = fields.Float(string="Maximum Age")
    # LastModifiedById already in odoo
    logo = fields.Text(string="Logo")
    logo_b64 = fields.Text(string="B64 logo")
    maximum_lives = fields.Float(string="Maximum Lives")
    minimum_lives = fields.Float(string="Minimum of Lives")
    Name = fields.Char(string="Study Configuration Name")
    OwnerId = fields.Many2one('res.users', string="Owner")
    partnership_id = fields.Many2one('account.account', string="Partnership")
    priority = fields.Float(string="Priority")
    report_key = fields.Char(string="Report Key", size=100)
    staging = fields.Boolean(string="staging")
    person_type = fields.Selection([
        ('PF', 'Physical person'), ('PJ', 'Legal person')
    ], string="Kind of person")
    validity_of_the_proposal = fields.Float(string="Validity of the Proposal")

