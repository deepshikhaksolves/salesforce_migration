from odoo import models, fields, api


class Request(models.Model):
    _name = 'model_request'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Request"
    _rec_name = 'Name'

    # CreatedById  already in odoo
    # Entitlement_id     = fields.Many2one('model_entitlement', string='Entitlement')
    # LastModifiedById already in odoo
    Name = fields.Char('Name', size=80,track_visibility='onchange')
    OwnerId = fields.Many2one('res.users', string='Owner',track_visibility='onchange')

    Case_Priority = fields.Selection([('Low', 'Low'), ('Average', 'Average'), ('High', 'High')], 'Priority of Service',track_visibility='onchange')
    Status = fields.Selection([('Active', 'Active'), ('Called off', 'Called off')], 'Status',track_visibility='onchange')
