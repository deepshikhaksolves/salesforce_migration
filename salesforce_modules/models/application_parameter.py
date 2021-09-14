from odoo import models, fields, api


class ApplicationParameter(models.Model):
    _name = 'model_application_parameter'
    _description = 'Salesforce Application Parameter'
    _rec_name = 'Name'

    appCode = fields.Char(string="appCode", size=50)
    Name = fields.Char(string="Application Parameters", size=80)
    # CreatedById already in odoo
    # LastModifiedById already in odoo
    OwnerId = fields.Many2one('res.users', string="Owner")
    Value = fields.Char(string="Value", size=255)