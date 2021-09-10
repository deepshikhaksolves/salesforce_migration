from odoo import models, fields, api


class Country(models.Model):
    _inherit = 'res.country'
    _description = "Salesforce Country"


    # CreatedById already in odoo
    # Country_Code             already in odoo i.e. (code)
    # LastModifiedById already in odoo
    OwnerId                 = fields.Many2one('res.users',string='Owner')
    # name                    already in odoo i.e. (name)
    
    state_ids       = fields.One2many('res.country.state', 'country_id', string='State IDS')
    