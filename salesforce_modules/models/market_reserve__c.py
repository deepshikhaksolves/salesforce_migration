from odoo import models, fields, api


class MarketReserve__C(models.Model):
    _name = 'model_market_reserve__c'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Market Reserve C"
    _rec_name = 'Name'

    How_c = fields.Char(string='Comment',size=255,track_visibility='onchange')
    Seller_c = fields.Many2one('res.users',string='Consultant',track_visibility='onchange')
    Account_c = fields.Many2one('account.account',string='Account',track_visibility='onchange')
    # ============== ===========================
    # CreatedById  already in odoo

    End_c = fields.Date(string='End Date',track_visibility='onchange')
    Start_c = fields.Date(string='Start Date',track_visibility='onchange')
    external_id_c = fields.Char(string='External Id',size=20,track_visibility='onchange')
    # LastModifiedById already in odoo
    Reason_c = fields.Selection([('Visit Scheduling','Visit Scheduling'),('Study Request','Study Request'),('Renewal by Negotiation','Renewal by Negotiation')],string='Reason',track_visibility='onchange')
    Not_update_account_c = fields.Boolean(string='Not update account',track_visibility='onchange')
    Opportunity_c = fields.Many2one('crm.lead',string='Opportunity',track_visibility='onchange')
    OwnerId = fields.Many2one('res.users',string='Owner',track_visibility='onchange')
    Name =  fields.Char(string='Market Reserve', size=80,track_visibility='onchange')
    Reserve_c = fields.Char(string='Reserve',track_visibility='onchange')
    Status_c = fields.Selection([('Reserved','Reserved'),('Finished','Finished'),('Canceled','Canceled')],string='Status',track_visibility='onchange')



