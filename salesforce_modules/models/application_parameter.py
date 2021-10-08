from odoo import models, fields, api


class ApplicationParameter(models.Model):
    _name = 'model_application_parameter'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Salesforce Application Parameter'
    _rec_name = 'Name'

    appCode = fields.Char(string="appCode", size=50, track_visibility='onchange')
    Name = fields.Char(string="Application Parameters", size=80, track_visibility='onchange')
    # CreatedById already in odoo
    # LastModifiedById already in odoo
    OwnerId = fields.Many2one('res.users', string="Owner", track_visibility='onchange')
    Value = fields.Char(string="Value", size=255, track_visibility='onchange')