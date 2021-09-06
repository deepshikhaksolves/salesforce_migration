from odoo import models, fields, api


class QuoteLineItem(models.Model):
    _name = 'quote_line_item'
    _description = "Salesforce Quote Line Item"
    _rec_name = 'LineNumber'


    accredited_network__c   = fields.Many2one('accredited_network', string="Accredited Network")
    copay__c                = fields.Selection([('WITH_COPAY','With co-participation'),('WITHOUT_COPAY','No Co-participation')],'Co-participation')
    # CreatedById  already in odoo
    ServiceDate             = fields.Date('Date')
    Discount                = fields.Float('Discount', digits=(3, 2))
    External_Id__c          = fields.Char('External Id', size=255)
    # LastModifiedById already in odoo
    Description             = fields.Char('Line Item Description', size=255)
    LineNumber              = fields.Integer('Line Item Number')
    ListPrice               = fields.Float('List Price', digits=(16, 2))
    Product2Id              = fields.Many2one('product.template', string='Product')
    requested_proposal__c   = fields.Boolean('Requested proposal')
    Quantity                = fields.Float('Quantity', digits=(10, 2))
    # QuoteId                 = fields.Many2one('model_quote', string='Quote Name')
    UnitPrice               = fields.Float('Sales Price', digits=(16, 2))
    Subtotal                = fields.Float('Subtotal', digits=(16, 2))
    TotalPrice              = fields.Float('Total Price', digits=(16, 2))
