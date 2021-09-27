from odoo import models, fields, api


class SalesforceProductNetwork(models.Model):

    _name = 'product.network'
    _description = 'Salesforce Product Network'

    # user_id = fields.Many2one('res.users', string="Created By") already in odoo
    # last_modified_by_id = fields.Many2one('res.users', string="Last Modified By") already in odoo
    name = fields.Char('Identification')
    product_id = fields.Many2one('product.template', string="Product")
    region = fields.Char('Region')

    accredited_network_id = fields.Many2one('accredited_network', string='Accredited Network')