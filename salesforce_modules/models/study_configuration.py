from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class StudyConfiguration(models.Model):
    _name = 'study_configuration'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Study Configuration C"
    _rec_name = 'Name'

    active = fields.Boolean(string="Active",track_visibility='onchange')
    # CreatedById already in odoo
    default_owner_id = fields.Many2one('res.users', string="Default Owner",track_visibility='onchange')
    Show_Aggregate = fields.Boolean(string="Show Aggregate",track_visibility='onchange')
    show_dependent = fields.Boolean(string="Display Dependent",track_visibility='onchange')
    maximum_age = fields.Float(string="Maximum Age",track_visibility='onchange')
    # LastModifiedById already in odoo
    logo = fields.Text(string="Logo",track_visibility='onchange')
    logo_b64 = fields.Text(string="B64 logo",track_visibility='onchange')
    maximum_lives = fields.Float(string="Maximum Lives",track_visibility='onchange')
    minimum_lives = fields.Float(string="Minimum of Lives",track_visibility='onchange')
    Name = fields.Char(string="Study Configuration Name",track_visibility='onchange')
    OwnerId = fields.Many2one('res.users', string="Owner",track_visibility='onchange')
    partnership_id = fields.Many2one('account.account', string="Partnership",track_visibility='onchange')
    priority = fields.Float(string="Priority",track_visibility='onchange')
    report_key = fields.Char(string="Report Key", size=100,track_visibility='onchange')
    staging = fields.Boolean(string="staging",track_visibility='onchange')
    person_type = fields.Selection([
        ('PF', 'Physical person'), ('PJ', 'Legal person')
    ], string="Kind of person",track_visibility='onchange')
    validity_of_the_proposal = fields.Float(string="Validity of the Proposal",track_visibility='onchange')

