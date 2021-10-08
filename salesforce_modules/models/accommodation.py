from odoo import models, fields, api


class Accomomodation(models.Model):
    _name = 'model_accommodation'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Salesforce Accommodation'
    _rec_name = 'Name'

    Abbreviation = fields.Char(string="Abbreviation", size=5, track_visibility='onchange')
    # CreatedById already in odoo
    Accommodation_ID = fields.Char(string="Accommodation ID", track_visibility='onchange')
    # LastModifiedById already in odoo
    Name = fields.Char(string="Accommodation Name", size=80, track_visibility='onchange')
    OwnerId = fields.Many2one('res.users', string="Owner", track_visibility='onchange')