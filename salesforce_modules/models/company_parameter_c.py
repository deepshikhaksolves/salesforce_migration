from odoo import models, fields, api

class Company_Parameter_C(models.Model):
    _name = 'model_company_parameter_c'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Company Parameter C"
    _rec_name = 'Name'

    # CreatedById  already in odoo
    # LastModifiedById already in odoo

    Name = fields.Char(string='Key',size=80)
    company_id = fields.Many2one('account.account',string='Company')
    priority = fields.Float(string='priority',digits=(3,0))
    study_configuration_id = fields.Many2one('study_configuration',string='Study Configuration')
    value = fields.Char(string='Value',size=100000)

