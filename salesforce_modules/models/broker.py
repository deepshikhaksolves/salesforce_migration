from odoo import models, fields, api

class Broker(models.Model):
    _name = 'broker'

    Name = fields.Char(string='Broker', size=80)
    # CreatedById created bu default
    SUSEp_Code = fields.Char(string='SUSEP code')
    # LastModifiedById created by default
    Logo = fields.Text(string='Logo')
    OwnerId = fields.Many2one('res.users', string='Owner')
    # Payment_Period not clear
    Account = fields.Many2one('account.account', string='people')
    Portfolio_Segmentation = fields.Selection([
        ('Individual', 'Individual'), ('legal_person',  'Legal person')
    ], string='Portfolio Segmentation')
    Broker_Type = fields.Selection([
        ('concessionaire', 'concessionaire'), ('Competitor', 'Competitor'), ('Brokerage_Concept', 'Brokerage Concept'), ('Strategic_Partner', 'Strategic Partner'), ('Brokerage_Partner', 'Brokerage Partner')
    ], string='Broker Type')
    Minimum_Payment = fields.Float(string='Minimum Payment Amount', digits=(16, 2))