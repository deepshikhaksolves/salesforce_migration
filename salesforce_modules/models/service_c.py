from odoo import models, fields, api

class Service_C(models.Model):
    _name = 'model_service_c'
    _description = "Salesforce Service C"
    _rec_name = 'Name'

    # CreatedById  already in odoo
    # LastModifiedById already in odoo

    accountable = fields.Text(string='Accountable')
    Client_Profile = fields.Selection([('A','Corporate'),('B','Middle'),('B with Approval','Middle with Approval'),('C','Small')],string='Client Profile')
    client_profile_text = fields.Text(string='Client Profile Text')
    Required = fields.Boolean(string='Mandotary')
    OwnerId = fields.Many2one('res.users',string='Owner')

    #periodicity_id = fields.Many2one('periodicity',string='Periodicity')
    #Field is related to periodicity object which is not define

    Name = fields.Text(string='Service')
    type = fields.Selection([('Request','Request'),('Assignment','Assignment')],string='Type')