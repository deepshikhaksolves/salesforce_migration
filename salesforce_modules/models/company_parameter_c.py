from odoo import models, fields, api
from odoo.exceptions import ValidationError


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
    attachment_ids = fields.One2many('ir.attachment', 'company_parameter_c_id', string="Attachment")

    @api.constrains('priority')
    def digit_validation(self):
        for rec in self:
            if rec.priority > 999:
                raise ValidationError("Priority should not greater than 3 digits")


class AttachmentInherit(models.Model):
    _inherit = 'ir.attachment'

    company_parameter_c_id = fields.Many2one('model_company_parameter_c', string="Company Parameter Id")

