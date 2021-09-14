from odoo import models, fields, api


class PriceList(models.Model):
    _name = 'model_price_list'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Price List"
    _rec_name = 'Name'

    contract_c = fields.Many2one('hr.contract', string='Contract')
    # CreatedById  already in odoo
    readjustment_date_c = fields.Date('Readjustment Date')
    end_validity_c = fields.Date('End Effective')
    start_validity_c = fields.Date('Beginning of Term')
    # LastModifiedById  already in odoo
    maximum_lives_c = fields.Float('Maximum Lives', digits=(4, 0))
    maximum_holder_lives_c = fields.Float('Maximum Holder Lives', digits=(4, 0))
    minimum_lives_c = fields.Float('Minimum Lives', digits=(4, 0))
    minimum_holder_lives_c = fields.Float('Minimum Holder Lives', digits=(4, 0))
    Name = fields.Char('Price List Name', size=80)
    carrier_c = fields.Many2one('account.account', string='Operator')
    OwnerId = fields.Many2one('res.users', string='Owner')
    percentage_adjustment_c = fields.Float('Percentage readjustment', digits=(2, 2))
    origin_table_c = fields.Many2one('model_price_list', string='source table')
    account_id = fields.Many2one('account.account', string='Account Id')
    product_price_ids = fields.One2many('product_price', 'price_list_id', 'Product Price IDS')
