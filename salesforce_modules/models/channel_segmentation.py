from odoo import models, fields, api

class ChannelSegmentation(models.Model):
    _name = 'channel_segmentation'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Channel Segmentation"
    _rec_name = 'name'


    Add_Approvers__c = fields.Many2one('res.users', string='Additional Approvers',track_visibility='onchange')
    Internal_Channel__c = fields.Boolean('Internal Channel',track_visibility='onchange')
    Parent_Channel__c = fields.Many2one('channel_segmentation',string='Parent Channel',track_visibility='onchange')
    Cost_Center__c = fields.Many2one('model_cost_center',string='Cost Center',track_visibility='onchange')
    code__c = fields.Char('Code', size=20,track_visibility='onchange')
    # CreatedById         already in odoo
    Manager__c = fields.Many2one('res.users', string='Manager',track_visibility='onchange')
    # LastModifiedById         already in odoo
    OwnerId = fields.Many2one('res.users',string='Owner',track_visibility='onchange')
    Allows_Multiple_Reservations__c = fields.Boolean('Allows Multiple Bookings',track_visibility='onchange')
    Paid__c = fields.Boolean('paid',track_visibility='onchange')
    name = fields.Char('Channel Segmentation',size=80,track_visibility='onchange')
    Status__c = fields.Selection([('Active','Active'),('Inactive','Inactive')],'Status',track_visibility='onchange')

    contracts_ids = fields.One2many('hr.contract','channel_segmentation', string="Contracts_ids" )
    opportunity_ids = fields.One2many('crm.lead','account_id', string='Opportunity IDS')
