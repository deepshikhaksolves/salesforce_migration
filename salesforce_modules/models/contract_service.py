from odoo import models, fields, api

class ContractService(models.Model):
    _name = 'contract.service'

    accountable = fields.Char(string='Accountable', size=255, )
    client_profile = fields.Char(string='Client Profile')
    Contracts = fields.Many2one('hr.contract', string='Contracts')
    # CreatedById created by default
    detailing = fields.Char(string='Detailing', size=255)
    Service_End = fields.Date(string='End of Service')
    in_scope = fields.Boolean(string='in Scope?')
    Service_Start = fields.Date(string='Start of Service')
    # LastModifiedById created by default
    OwnerId = fields.Many2one('res.users', string='Owner')
    # Periodicity not clear
    # Service not clear
    Name = fields.Char(string='Contract ID Service') 