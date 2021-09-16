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
        ('Fee', 'Fee')], string="Benefit")
    Quote_id = fields.Many2one('model_quote', string="Price")
    # CreatedById already in odoo
    OwnerId = fields.Many2one('res.users', string="Owner")
    Product_id = fields.Many2one('product.template', string="Product")
    Name = fields.Char(string="Quotation Products")
    Cost_Type = fields.Selection([
        ('Average cost', 'Average cost'),
        ('age group', 'Age group')
    ], string="Cost Type")
    Value = fields.Float(string="Value")
    # LastModifiedById already in odoo


