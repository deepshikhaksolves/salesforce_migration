from odoo import models, fields, api

class Service_C(models.Model):
    _name = 'model_service_c'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Service C"
    _rec_name = 'Name'

    # CreatedById  already in odoo
    # LastModifiedById already in odoo

    accountable = fields.Char(string='Accountable',size=255)
    Client_Profile = fields.Selection([('A','Corporate'),('B','Middle'),('B with Approval','Middle with Approval'),('C','Small')],string='Client Profile')
    client_profile_text = fields.Text(string='Client Profile Text')
    Required = fields.Boolean(string='Mandatory')
    OwnerId = fields.Many2one('res.users',string='Owner')

    periodicity_id = fields.Many2one('model.periodicity',string='Periodicity')


    Name = fields.Char(string='Service',size=80)
    type = fields.Selection([('Request','Request'),('Assignment','Assignment')],string='Type')