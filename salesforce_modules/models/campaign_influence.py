from odoo import models, fields, api


class CampaignInfluence(models.Model):
    _name = 'campaign.influence'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Campaign Influence"
    _rec_name = 'CampaignId'

    CampaignId = fields.Many2one('model_campaign', string='Campaign')
    # ModelId = fields.Many2one('campaign influence model', 'Campign Influence Model')
    ContactId = fields.Many2one('res.partner', 'Contact')
    # CreatedById already in odoo i.e. create_uid
    # CreatedDate already in odoo i.e. create_date
    Influence = fields.Float(string='Influence (%)', digits=(3, 2))
    # LastModifiedById already in odoo i.e. write_uid
    # LastModifiedDate already in odoo i.e. write_date
    OpportunityId = fields.Many2one('crm.lead', 'Opportunity')
    RevenueShare = fields.Float(string='Revenue Share', digits=(16, 2))
