from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class QuoteProducts(models.Model):
    _name = 'model_quote_products'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Salesforce Quote Products'
    _rec_name = 'Name'

    Benefits = fields.Selection([
        ('Health', 'Health'),
        ('Dental', 'Dental'),
        ('Life', 'Life'),
        ('Medicine', 'Medicine'),
        ('Personal_Accidents', 'Personal Accident'),
        ('In_Company', 'Consultancy'),
        ('Medical_Consulting', 'Medical Consulting'),
        ('Meal', 'Snack'),
        ('Food', 'Food'),
        ('Transportation', 'Transport'),
        ('Pension', 'Pension'),
        ('Car_Fleet', 'Fleet'),
        ('Car', 'Car'),
        ('Fuel', 'Fuel'),
        ('Occupational_Health', 'Occupational_Health'),
        ('Checkup', 'Checkup'),
        ('Vaccine', 'Vaccine'),
        ('I_protected', 'I Protected'),
        ('Fee', 'Fee')], string="Benefit",track_visibility='onchange')
    Quote_id = fields.Many2one('model_quote', string="Price",track_visibility='onchange')
    # CreatedById already in odoo
    OwnerId = fields.Many2one('res.users', string="Owner",track_visibility='onchange')
    Product_id = fields.Many2one('product.template', string="Product",track_visibility='onchange')
    Name = fields.Char(string="Quotation Products",track_visibility='onchange')
    Cost_Type = fields.Selection([
        ('Average cost', 'Average cost'),
        ('age group', 'Age group')
    ], string="Cost Type",track_visibility='onchange')
    Value = fields.Float(string="Value",track_visibility='onchange')

    quote_product_id = fields.Many2one('model_quote', string='Quote Product')
    # LastModifiedById already in odoo


