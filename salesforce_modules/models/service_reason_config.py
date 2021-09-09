from odoo import models, fields, api

class ServiceReasonConfig(models.Model):
    _name = 'service_reason_config'
    _description = "Salesforce Service Reason Config"
    _rec_name = 'Name'

    # CreatedById  already in odoo
    Name                = fields.Char('Code')
    Default             = fields.Boolean('Default')
    # LastModifiedById already in odoo
    Case_Reason         = fields.Selection([('Information','Information'),('Request','Request'),('Complaint','Complaint')],'Reason for Service')
    OwnerId             = fields.Many2one('res.users',string='Owner')

    solicitation_id     = fields.Many2one('model_request', string='Solicitation')
