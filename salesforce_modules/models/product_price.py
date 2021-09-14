from odoo import models, fields, api

class ProductPrice(models.Model):
    _name = 'product_price'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Product Price"
    _rec_name = 'Name'

    # CreatedById  already in odoo
    age_range__c    = fields.Selection([('FROM_0_TO_18','0 - 18'),('FROM_19_TO_23','19 - 23'),('FROM_24_TO_28','24 - 28'),('FROM_29_TO_33','29 - 33'),('FROM_34_TO_38','34 - 38'),('FROM_39_TO_43','39 - 43'),('FROM_44_TO_48','44 - 48'),('FROM_49_TO_53','49 - 53'),('FROM_54_TO_58','54 - 58'),('FROM_59_PLUS','59 +')],'age group')
    Name                    = fields.Char('Identification')
    # LastModifiedById  already in odoo
    contract_product__c     = fields.Many2one('model_contract_plan',string='Contract Plan')
    pricing__c              = fields.Char('Pricing')
    Product__c              = fields.Many2one('product.template',string='Product')
    RecordTypeId            = fields.Char('Record Type')
    Price_Table__c          = fields.Many2one('model_price_list',string='Price list')
    others_value__c         = fields.Float('Value For or Added', digits=(12, 2))
    others_value_copay__c   = fields.Float('Aggregate Value (copay)', digits=(10, 2))
    holder_value__c         = fields.Float('Value for or Holder', digits=(12, 2))
    holder_value_copay__c   = fields.Float('Value for the Holder (Copay)', digits=(10, 2))

    price_list_id        = fields.Many2one('model_price_list', string="Price List ID")