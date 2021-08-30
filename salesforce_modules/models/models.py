# -*- coding: utf-8 -*-

from odoo import models, fields, api


class salesforce_user(models.Model):
    _inherit = 'res.user'
    _description = 'salesforce users'

    about_me = fields.Text(string = "About Me", limit=1000)
    # isactive field aready present in odoo
    street = fields.Char()
    street2 = fields.Char()
    zip = fields.Char(change_default=True)
    city = fields.Char()
    state_id = fields.Many2one("res.country.state", string='State', ondelete='restrict',
                               domain="[('country_id', '=?', country_id)]")
    country_id = fields.Many2one('res.country', string='Country', ondelete='restrict')
    partner_latitude = fields.Float(string='Geo Latitude', digits=(16, 5))
    partner_longitude = fields.Float(string='Geo Longitude', digits=(16, 5))
    ReceivesAdminInfoEmails = fields.Boolean(string="Admin Info Emails")
    alias = fields.Text(string="Alias")
    forecast_enabled = fields.Boolean(string="Allow Forecasting")
    # banner photo is already present in odoo
