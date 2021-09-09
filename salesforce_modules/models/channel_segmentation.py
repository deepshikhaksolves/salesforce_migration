from odoo import models, fields, api

class ChannelSegmentation(models.Model):
    _name = 'channel_segmentation'
    _description = "Salesforce Channel Segmentation"
    _rec_name = 'name'


    Add_Approvers__c    = fields.Many2one('res.users', string='Additional Approvers')
    Internal_Channel__c = fields.Boolean('Internal Channel')
    Parent_Channel__c   = fields.Many2one('channel_segmentation',string='Parent Channel')
    # Cost_Center__c   = fields.Many2one('',string='Cost center')
    code__c             = fields.Char('Code', size=20)
    # CreatedById         already in odoo
    Manager__c          = fields.Many2one('res.users', string='Manager')
    # LastModifiedById         already in odoo
    OwnerId             = fields.Many2one('res.users',string='Owner')
    Allows_Multiple_Reservations__c = fields.Boolean('Allows Multiple Bookings')
    Paid__c              = fields.Boolean('paid')
    name                 = fields.Char('Channel Segmentation',size=80)
    Status__c            = fields.Selection([('Active','Active'),('Inactive','Inactive')],'Status')

    # opportunity_ids      = fields.One2many('')