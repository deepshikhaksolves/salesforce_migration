from odoo import models, fields, api


class QuotationItemPrice(models.Model):
    _name = 'quotation_item_price'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Quotation Item Price"
    _rec_name = 'Name'

    # CreatedById  already in odoo
    quote_line_item__c = fields.Many2one('quote_line_item', string='Quote Line Item',track_visibility='onchange')
    # LastModifiedById already in odoo
    Name = fields.Char(string='Name',track_visibility='onchange')
    line_price__c = fields.Float('Line Price', digits=(10, 2),track_visibility='onchange')
    product_price__c = fields.Many2one('product_price', string='Price of the product',track_visibility='onchange')
    others_quantity__c = fields.Float('Aggregate Quantity', digits=(10, 0),track_visibility='onchange')
    dependent_quantity__c = fields.Float('Dependent Quantity', digits=(10, 0),track_visibility='onchange')
    holder_quantity__c = fields.Float('Holder Quantity', digits=(10, 0),track_visibility='onchange')
