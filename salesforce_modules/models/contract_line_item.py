from odoo import models, fields, api


class ContractLineItem(models.Model):
    _name = 'contract.line.item'

    # asset_id = fields.Many2one('comodel_name', string='')
    # CreatedById created by default
    # CreatedDate created by default
    description = fields.Text(string='Description')
    discount = fields.Float(string='Discount')
    end_date = fields.Date(string='')
    last_modified_by_id = fields.Many2one('res.user', string='Last Modified By')
    last_modified_date = fields.Date(string='Last Modified Date')
    # LineItemNumber it would be id
    list_price = fields.Float(string='List Price')
    # LocationId not clear
    ParentContractLineItemId = fields.Many2one('contract.line.item', string='Parent Contract Line Item')
    Product2Id = fields.Many2one('product.product', string='Product')
    Quantity = fields.Float(string='Quantity', digits=(10, 2))
    RootContractLineItemId = fields.Many2one('contract.line.item', string='Root Contract Line Item')
    UnitPrice = fields.Float(string='Sales Price', digits=(16, 2))
    ServiceContractId = fields.Many2one('contract.service', string='Service Contract')
    StartDate = fields.Date(string='Start Date')
    # Status	 = fields.Selection([
    #     ('key', 'value')
    # ], string='Status')
    Subtotal = fields.Float(string='Subtotal', digits=(16, 2))
    TotalPrice = fields.Float(string='Total Price', digits=(16, 2))
