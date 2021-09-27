from odoo import models, fields, api


class ServiceReasonConfig(models.Model):
    _name = 'service_reason_config'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Service Reason Config"
    _rec_name = 'Name'

    # CreatedById  already in odoo
    Name = fields.Char('Code',track_visibility='onchange')
    Default = fields.Boolean('Default',track_visibility='onchange')
    # LastModifiedById already in odoo
    Case_Reason = fields.Selection([('Information', 'Information'), ('Request', 'Request'), ('Complaint', 'Complaint')],
                                   'Reason for Service',track_visibility='onchange')
    OwnerId = fields.Many2one('res.users', string='Owner',track_visibility='onchange')

    solicitation_id = fields.Many2one('model_request', string='Solicitation',track_visibility='onchange')
