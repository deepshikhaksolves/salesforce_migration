from odoo import models, fields, api

class BrokerRating(models.Model):
    _name = 'broker.rating'
    
    Rating = fields.Selection([
        ('Bronze', 'Bronze'), ('Silver', 'Silver'), ('Gold', 'Gold'), ('Diamond', 'Diamond')
    ], string='Classification')
    Name = fields.Char(string='Broker ID Classification')
    # CreatedById	created by default
    End = fields.Date(string='The End')
    Start = fields.Date(string='Start')
    # LastModifiedById created by default
    OwnerId = fields.Many2one('res.users', string='Owner')
    Segmentation = fields.Selection([
        ('Physical_person', 'Physical person'), ('Legal_person', 'Legal person')
    ], string='Segmentation')