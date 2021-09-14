from odoo import models, fields, api


class AdditionalParameter(models.Model):
    _name = 'model_additional_parameter'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Salesforce Additional Parameter'
    _rec_name = 'Name'

    # CreatedById already in odoo
    # LastModifiedById already in odoo
    Name =  fields.Char(string="Identification")
    OwnerId = fields.Many2one('res.users', string="Owner")
    quote_id = fields.Many2one('model_quote', string="Quote")
    type = fields.Selection([
        ('sincor_partnership','Sincor Associate'),
        ('status_sincor_partnership','Sincor Member Status')
    ], string="Type")
    value = fields.Char(string="Value", size=32768)
