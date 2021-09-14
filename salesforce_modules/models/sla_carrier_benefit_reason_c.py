from odoo import models, fields, api

class SLA_Carrier_Benefit_Reason_C(models.Model):
    _name = 'model_sla_carrier_benefit_reason_c'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce SLA Carrier Benefit Reason C"
    _rec_name = 'Name'

    # CreatedById  already in odoo
    # LastModifiedById already in odoo

    Name = fields.Char(string='Code')
    carrier_id = fields.Many2one('account.account',string='Operator')
    OwnerId = fields.Many2one('res.users', string='Owner')
    #Case_Request_SLA_id = fields.Many2one('request_deadline',string='Request Deadline')
    #Field is related to request_deadline object which is not define
