from odoo import models, fields, api


class Country(models.Model):
    _name = 'res.country'
    _inherit = ['res.country', 'mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Country"

    # CreatedById already in odoo
    # Country_Code             already in odoo i.e. (code)
    # LastModifiedById already in odoo
    OwnerId = fields.Many2one('res.users', string='Owner')
    # name                    already in odoo i.e. (name)

    state_ids = fields.One2many('res.country.state', 'country_id', string='State')
