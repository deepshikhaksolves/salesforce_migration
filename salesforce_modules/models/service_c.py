from odoo import models, fields, api


class Service_C(models.Model):
    _name = 'model_service_c'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Service C"
    _rec_name = 'Name'

    # CreatedById  already in odoo
    # LastModifiedById already in odoo

    accountable = fields.Char(string='Accountable', size=255,track_visibility='onchange')
    Client_Profile = fields.Selection(
        [('A', 'Corporate'), ('B', 'Middle'), ('B with Approval', 'Middle with Approval'), ('C', 'Small')],
        string='Client Profile',track_visibility='onchange')
    client_profile_text = fields.Text(string='Client Profile Text',track_visibility='onchange')
    Required = fields.Boolean(string='Mandatory',track_visibility='onchange')
    OwnerId = fields.Many2one('res.users', string='Owner',track_visibility='onchange')

    periodicity_id = fields.Many2one('model.periodicity',string='Periodicity',track_visibility='onchange')


    Name = fields.Char(string='Service', size=80,track_visibility='onchange')
    type = fields.Selection([('Request', 'Request'), ('Assignment', 'Assignment')], string='Type',track_visibility='onchange')
    contract_service_ids = fields.One2many('contract.service','Service', string='Contract Service')
    contract_id = fields.Many2one('hr.contract',string='Contract',track_visibility='onchange')
