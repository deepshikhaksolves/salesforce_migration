from odoo import models, fields, api


class Eligibility(models.Model):
    _name = 'model_eligibility'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Eligibility"
    _rec_name = 'name'

    # CreatedById already in odoo
    name = fields.Char('Eligibility', size=80)
    # LastModifiedById already in odoo
    OwnerId = fields.Many2one('res.users', string='Owner')
