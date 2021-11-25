from odoo import models, fields, api

class ProductPrice(models.Model):
    _name = 'product_price'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Product Price"
    _rec_name = 'Name'

    # CreatedById  already in odoo
    age_range_c = fields.Selection([('FROM_0_TO_18','0 - 18'),('FROM_19_TO_23','19 - 23'),('FROM_24_TO_28','24 - 28'),('FROM_29_TO_33','29 - 33'),('FROM_34_TO_38','34 - 38'),('FROM_39_TO_43','39 - 43'),('FROM_44_TO_48','44 - 48'),('FROM_49_TO_53','49 - 53'),('FROM_54_TO_58','54 - 58'),('FROM_59_PLUS','59 +')],'age group',track_visibility='onchange')
    Name = fields.Char('Identification',track_visibility='onchange')
    # LastModifiedById  already in odoo
    contract_product_c = fields.Many2one('model_contract_plan',string='Contract Plan',track_visibility='onchange')
    pricing_c = fields.Char('Pricing',track_visibility='onchange')
    Product_c = fields.Many2one('product.template',string='Product',track_visibility='onchange')
    RecordTypeId = fields.Char('Record Type',track_visibility='onchange')
    Price_Table_c = fields.Many2one('model_price_list',string='Price list',track_visibility='onchange')
    others_value_c = fields.Float('Value For or Added', digits=(12, 2),track_visibility='onchange')
    others_value_copay_c = fields.Float('Aggregate Value (copay)', digits=(10, 2),track_visibility='onchange')
    holder_value_c = fields.Float('Value for or Holder', digits=(12, 2),track_visibility='onchange')
    holder_value_copay_c = fields.Float('Value for the Holder (Copay)', digits=(10, 2),track_visibility='onchange')

    price_list_id = fields.Many2one('model_price_list', string="Price List ID",track_visibility='onchange')

    price_x_region_ids = fields.One2many('model_price_x_region', 'model_product_price_id', string='Price x region IDS')
