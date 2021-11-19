from odoo import models, fields, api


class Address(models.Model):
    _name = 'model_address'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Salesforce Address'
    _rec_name = 'Name'

    District = fields.Char(string="Neighborhood", size=100, track_visibility='onchange')
    Zip_Code = fields.Char(string="POCKET", size=9, track_visibility='onchange')
    City = fields.Many2one('model_city_c', string="City", track_visibility='onchange')
    Complement = fields.Char(string="Complement", size=255, track_visibility='onchange')
    Contract_id = fields.Many2one('hr.contract', string="Contract", track_visibility='onchange')
    # CreatedById already in odoo
    # LastModifiedById already in odoo
    Name = fields.Char(string="Address", size=80, track_visibility='onchange')
    Address = fields.Char(string="Address ID", track_visibility='onchange')
    State_id = fields.Many2one('res.country.state', string="State", track_visibility='onchange')
    Coordinates = fields.Float(string="Geolocation", track_visibility='onchange')
    Number = fields.Char(string="Number", size=100, track_visibility='onchange')
    Account_id = fields.Many2one('account.account', string="Legal person", track_visibility='onchange')
    Landmark = fields.Char(string="Reference point", size=255, track_visibility='onchange')
    Address_Type = fields.Selection([
        ('card', 'Card'),
        ('letter', 'Letters'),
        ('Charge', 'Charge'),
        ('Commercial', 'Commercial'),
        ('Correspondence', 'Correspondence'),
        ('Revenues', 'Revenues'),
        ('Fiscal', 'Fiscal'),
        ('Legal', 'Legal'),
        ('Residential', 'Residential'),
        ('Everybody', 'Everybody')
    ], string="Type of address", track_visibility='onchange')
    OwnerId = fields.Many2one('res.users', string="Owner", track_visibility='onchange')

    geo_scope_id = fields.Many2one('model_geographic_scope', string='Geographic Scope ID', track_visibility='onchange')
