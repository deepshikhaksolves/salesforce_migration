from odoo import models, fields, api

class Broker(models.Model):
    _name = 'broker'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    Name = fields.Char(string='Broker', size=80, track_visibility='onchange')
    # CreatedById created bu default
    SUSEp_Code = fields.Char(string='SUSEP code', track_visibility='onchange')
    # LastModifiedById created by default
    Logo = fields.Text(string='Logo', track_visibility='onchange')
    OwnerId = fields.Many2one('res.users', string='Owner', track_visibility='onchange')
    Payment_Period = fields.Many2one('model.periodicity', string='Payment Frequency', track_visibility='onchange')
    Account = fields.Many2one('account.account', string='People', track_visibility='onchange')
    Portfolio_Segmentation = fields.Selection([
        ('Individual', 'Individual'), ('legal_person',  'Legal person')
    ], string='Portfolio Segmentation', track_visibility='onchange')
    Broker_Type = fields.Selection([
        ('concessionaire', 'concessionaire'), ('Competitor', 'Competitor'), ('Brokerage_Concept', 'Brokerage Concept'), ('Strategic_Partner', 'Strategic Partner'), ('Brokerage_Partner', 'Brokerage Partner')
    ], string='Broker Type', track_visibility='onchange')
    Minimum_Payment = fields.Float(string='Minimum Payment Amount', digits=(16, 2), track_visibility='onchange')

    benifit_politic_ids = fields.One2many('model_benfit_politic', 'Competitor', string='Benefit Politic')
    broker_rating_ids = fields.One2many('broker.rating', 'Broker', string='Broker Ratings')
    account_ids = fields.One2many('account.account', 'broker_id', string='Account')
    lead_ids = fields.One2many('crm.lead', 'broker_id', string='Leads')