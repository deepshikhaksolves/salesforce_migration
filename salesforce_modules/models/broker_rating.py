from odoo import models, fields, api

class BrokerRating(models.Model):
    _name = 'broker.rating'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'Name'
    
    Rating = fields.Selection([
        ('Bronze', 'Bronze'), ('Silver', 'Silver'), ('Gold', 'Gold'), ('Diamond', 'Diamond')
    ], string='Classification', track_visibility='onchange')
    Name = fields.Char(string='Broker ID Classification', track_visibility='onchange')
    # CreatedById	created by default
    End = fields.Date(string='The End', track_visibility='onchange')
    Start = fields.Date(string='Start', track_visibility='onchange')
    # LastModifiedById created by default
    OwnerId = fields.Many2one('res.users', string='Owner', track_visibility='onchange')
    Segmentation = fields.Selection([
        ('Physical_person', 'Physical person'), ('Legal_person', 'Legal person')
    ], string='Segmentation', track_visibility='onchange')
    Broker = fields.Many2one('broker', string="Broker")