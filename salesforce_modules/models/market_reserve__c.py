from odoo import models, fields, api


class MarketReserve__C(models.Model):
    _name = 'model_market_reserve__c'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Market Reserve C"
    _rec_name = 'Name'

    How_c = fields.Char(string='Comment',size=255)
    Seller__c = fields.Many2one('res.users',string='Consultant')
    Account__c = fields.Many2one('account.account',string='Account')
    # ============== ===========================
    # CreatedById  already in odoo

    End__c = fields.Date(string='End Date')
    Start__c = fields.Date(string='Start Date')
    external_id__c = fields.Char(string='External Id',size=20)
    # LastModifiedById already in odoo
    Reason__c = fields.Selection([('Visit Scheduling','Visit Scheduling'),('Study Request','Study Request'),('Renewal by Negotiation','Renewal by Negotiation')],string='Reason')
    Not_update_account__c = fields.Boolean(string='Not update account')
    Opportunity__c = fields.Many2one('crm.lead',string='Opportunity')
    OwnerId = fields.Many2one('res.users',string='Owner')
    Name =  fields.Char(string='Market Reserve', size=80)
    Reserve__c = fields.Char(string='Reserve')
    Status__c = fields.Selection([('Reserved','Reserved'),('Finished','Finished'),('Canceled','Canceled')],string='Status')



