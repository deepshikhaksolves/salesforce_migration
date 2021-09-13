from odoo import models, fields, api


class Accomomodation(models.Model):
    _name = 'model_accommodation'
    _description = 'Salesforce Accommodation'
    _rec_name = 'Name'

    Abbreviation = fields.Char(string="Abbreviation", size=5)
    # CreatedById already in odoo
    Accommodation_ID = fields.Char(string="Accommodation ID")
    # LastModifiedById already in odoo
    Name = fields.Char(string="Accommodation Name", size=80)
    OwnerId = fields.Many2one('res.users', string="Owner")