from odoo import models, fields, api


class Product(models.Model):
    _name = 'model_product'
    _description = "Salesforce Product"
    _rec_name = 'Name'


    accommodation__c    = fields.Selection([('nurse','Nursery'),('apt','Apartment')],'Accommodation')
    IsActive            = fields.Boolean('Active')
    ans_code_with_copay__c = fields.Char(string='ANS Code With Copay', size=15)
    ans_code_no_copay__c = fields.Char(string='ANS Code Without Copay', size=15)
    carrier__c           = fields.Char(string='Carrier')
    Product_Classification__c = fields.Selection([('Basic Infirmary','Basic Infirmary'),('Basic Apartment','Basic Apartment'),('Standard infirmary','Standard infirmary'),('Standard Apartment','Standard Apartment'),('Executive','Executive')],'Product Classification')
    Coverage__c    = fields.Selection([('role','role'),('Expanded List','Expanded List')],'Coverage')
    # CreatedById  already in odoo
    integration_product_code__c = fields.Char(string='Integration Code', size=50)
    Internal_Code__c = fields.Char(string='Internal code', size=50)
    DisplayUrl       = fields.Char(string='Display URL', size=1000)
    Downgrade__c     = fields.Boolean('Downgrade')
    # ExternalDataSourceId    = fields.Many2one('', string='External Data Source')
    ExternalId              = fields.Char(string='External ID', size=255)
    product_family__c       = fields.Many2one('product_family',string='Product Family')
    Geographic_Scope__c     = fields.Many2one('model_geographic_scope',string='Geographic Scope ANS')
    Geographic_Scope_tnk__c = fields.Char('Geographic Scope tnk')
    # LastModifiedById already in odoo
    Charge_Mode__c          = fields.Selection([('average cost','Average cost'),('age group','age group')],'Billing Model')
    maximum_lives__c        = fields.Float('Maximum Lives', digits=(4, 0))
    Minimum_Lives__c        = fields.Float('Minimum of Lives', digits=(4, 0))
    priority__c             = fields.Float('Priority', digits=(3, 0))
    ProductCode             = fields.Char(string='Product Code', size=255)
    Description             = fields.Char(string='Product Description', size=4000)
    # Family                  =