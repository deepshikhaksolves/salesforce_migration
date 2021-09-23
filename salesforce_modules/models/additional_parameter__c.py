from odoo import models, fields, api


class AdditionalParameter(models.Model):
    _name = 'model_additional_parameter'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Salesforce Additional Parameter'
    _rec_name = 'quote_id'

    # CreatedById already in odoo
    # LastModifiedById already in odoo
    Name = fields.Char(string="Identification", track_visibility='onchange')
    OwnerId = fields.Many2one('res.users', string="Owner", track_visibility='onchange')
    quote_id = fields.Many2one('model_quote', string="Quote", track_visibility='onchange')
    type = fields.Selection([
        ('sincor_partnership', 'Sincor Associate'),
        ('status_sincor_partnership', 'Sincor Member Status')
    ], string="Type", track_visibility='onchange')
    value = fields.Char(string="Value", size=32768, track_visibility='onchange')
