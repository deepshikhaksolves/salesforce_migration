from odoo import fields, models, api


class SaleInherit(models.Model):
    _inherit = 'sale.order'


    name = fields.Char('name')
