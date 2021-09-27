from odoo import models, fields, api


class ReasonForBeneficial(models.Model):
    _name = 'model_reason_for_beneficial'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Salesforce REason For Beneficial'
    _rec_name = 'Name'

    # CreatedById already in odoo
    code = fields.Char(striing="Code", size=100,track_visibility='onchange')
    Name = fields.Char(string="Description", size=80,track_visibility='onchange')
    end_term = fields.Date(string="End of Term",track_visibility='onchange')
    home_term = fields.Date(string="Beginning of Term",track_visibility='onchange')
    # LastModifiedById already in odoo
    OwnerId = fields.Many2one('res.users', string="Owner",track_visibility='onchange')


