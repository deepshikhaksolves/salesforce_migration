from odoo import models, fields, api

class GlobalParameter(models.Model):
    _name = 'global_parameter'
    _description = "Salesforce Global Parameter"
    _rec_name = 'Key'

    Key = fields.Char('Key', size=255)
    Value = fields.Char('Value', size=255)