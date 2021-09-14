from odoo import models, fields, api

class EventControl(models.Model):
    _name = 'event_control'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Event Control"
    _rec_name = 'name'

    Assign_ID = fields.Many2one('res.users',string='Assign ID')
    cancelled = fields.Boolean('Cancelled')
    # CreatedById  already in odoo
    name = fields.Char('Event', size=80)
    Event_ID = fields.Char('Event ID', size=50)
    # LastModifiedById  already in odoo
    Opportunity_ID = fields.Many2one('crm.lead', string='Opportunity ID')
    OwnerId = fields.Many2one('res.users',string='Owner')
    pre_consultant = fields.Many2one('res.users',string='Pre Consultant')
    pre_consultant_current_user = fields.Char('Pre Consultant Current User')
    Rescheduled = fields.Boolean('Rescheduled')
    Start_Date = fields.Datetime('Start Date')
    Visit = fields.Char('Visit')