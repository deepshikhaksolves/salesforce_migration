from odoo import models, fields, api


class Address(models.Model):
    _name = 'model_address'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Salesforce Address'
    _rec_name = 'Name'

    District = fields.Char(string="Neighborhood", size=100)
    Zip_Code = fields.Char(string="POCKET", size=9)
    City = fields.Many2one('model_city_c',string="City")
    Complement =  fields.Char(string="Complement", size=255)
    Contract_id = fields.Many2one('hr.contract', string="Contract")
    # CreatedById already in odoo
    # LastModifiedById already in odoo
    Name =  fields.Char(string="Address", size=30)
    Address = fields.Char(string="Address ID", size=80)
    State__id = fields.Many2one('res.country.state',string="State")
    Coordinates = fields.Float(string="Geolocation")
    Number = fields.Char(string="Number", size=100)
    Account_id = fields.Many2one('account.account', string="Legal person")
    Landmark = fields.Char(string="Reference point", size=255)
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
    ], string="Type of address")
    OwnerId = fields.Many2one('res.users', string="Owner")

    geo_scope_id = fields.Many2one('model_geographic_scope', string='Geographic Scope ID')
