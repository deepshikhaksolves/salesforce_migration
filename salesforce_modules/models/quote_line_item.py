from odoo import models, fields, api


class QuoteLineItem(models.Model):
    _name = 'quote_line_item'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Quote Line Item"
    _rec_name = 'LineNumber'


    accredited_network_c = fields.Many2one('accredited_network', string="Accredited Network",track_visibility='onchange')
    copay_c = fields.Selection([('WITH_COPAY','With co-participation'),('WITHOUT_COPAY','No Co-participation')],'Co-participation',track_visibility='onchange')
    # CreatedById  already in odoo
    ServiceDate = fields.Date('Date',track_visibility='onchange')
    Discount = fields.Float('Discount', digits=(3, 2),track_visibility='onchange')
    External_Id_c = fields.Char('External Id', size=255,track_visibility='onchange')
    # LastModifiedById already in odoo
    Description = fields.Char('Line Item Description', size=255,track_visibility='onchange')
    LineNumber = fields.Integer('Line Item Number',track_visibility='onchange')
    ListPrice = fields.Float('List Price', digits=(16, 2),track_visibility='onchange')
    Product2Id = fields.Many2one('product.template', string='Product',track_visibility='onchange')
    requested_proposal_c = fields.Boolean('Requested proposal',track_visibility='onchange')
    Quantity = fields.Float('Quantity', digits=(10, 2),track_visibility='onchange',required=True)
    QuoteId = fields.Many2one('model_quote', string='Quote Name',track_visibility='onchange')
    UnitPrice = fields.Float('Sales Price', digits=(16, 2),track_visibility='onchange',required=True)
    Subtotal = fields.Float('Subtotal', digits=(16, 2),track_visibility='onchange')
    TotalPrice = fields.Float('Total Price', digits=(16, 2),track_visibility='onchange')
