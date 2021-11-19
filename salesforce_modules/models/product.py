from odoo import models, fields, api


class ProductTemplate(models.Model):
    _name = 'product.template'
    _inherit = ['product.template', 'mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Product"


    accommodation_c = fields.Selection([('nurse','Nursery'),('apt','Apartment')],'Accommodation',track_visibility='onchange')
    IsActive = fields.Boolean('Active',track_visibility='onchange')
    ans_code_with_copay_c = fields.Char(string='ANS Code With Copay', size=15,track_visibility='onchange')
    ans_code_no_copay_c = fields.Char(string='ANS Code Without Copay', size=15,track_visibility='onchange')
    carrier_c = fields.Char(string='Carrier',track_visibility='onchange')
    Product_Classification_c = fields.Selection([('Basic Infirmary','Basic Infirmary'),('Basic Apartment','Basic Apartment'),('Standard infirmary','Standard infirmary'),('Standard Apartment','Standard Apartment'),('Executive','Executive')],'Product Classification',track_visibility='onchange')
    Coverage_c = fields.Selection([('role','role'),('Expanded List','Expanded List')],'Coverage',track_visibility='onchange')
    # CreatedById  already in odoo
    integration_product_code_c = fields.Char(string='Integration Code', size=50,track_visibility='onchange')
    Internal_Code_c = fields.Char(string='Internal code', size=50,track_visibility='onchange')
    DisplayUrl = fields.Char(string='Display URL', size=1000,track_visibility='onchange')
    Downgrade_c = fields.Boolean('Downgrade',track_visibility='onchange')
    # ExternalDataSourceId    = fields.Many2one('', string='External Data Source')
    ExternalId = fields.Char(string='External ID', size=255,track_visibility='onchange')
    product_family_c = fields.Many2one('product_family',string='Product Family',track_visibility='onchange')
    Geographic_Scope_c = fields.Many2one('model_geographic_scope',string='Geographic Scope ANS',track_visibility='onchange')
    Geographic_Scope_tnk_c = fields.Char('Geographic Scope tnk',track_visibility='onchange')
    # LastModifiedById already in odoo
    Charge_Mode_c = fields.Selection([('average cost','Average cost'),('age group','age group')],'Billing Model',track_visibility='onchange')
    maximum_lives_c = fields.Float('Maximum Lives', digits=(4, 0),track_visibility='onchange')
    Minimum_Lives_c = fields.Float('Minimum of Lives', digits=(4, 0),track_visibility='onchange')
    priority_c = fields.Float('Priority', digits=(3, 0),track_visibility='onchange')
    ProductCode = fields.Char(string='Product Code', size=255,track_visibility='onchange')
    Description = fields.Char(string='Product Description', size=4000,track_visibility='onchange')
    Family = fields.Selection([('None','--None--'),('Basic','Basic'),('Blue','Blue'),('Dix','Dix'),('Executive','Executive'),('Flex','Flex'),('International','International'),('Top Preferred','Top Preferred'),('447','447'),('557','557')],'Product Family',track_visibility='onchange')
    # name                   already in odoo
    RecordTypeId = fields.Integer('Product Record Type',track_visibility='onchange') # DATA TYPE IS Record Type
    StockKeepingUnit = fields.Char(string='Product SKU', size=180,track_visibility='onchange')
    QuantityUnitOfMeasure = fields.Selection([('Each','Each')],'Quantity Unit Of Measure',track_visibility='onchange')
    Segmentation_c = fields.Selection([('Outpatient','Outpatient'),('Hospital without obstetrics','Hospital without obstetrics'),('Hospital with obstetrics','Hospital with obstetrics'),('Exclusively Dental','Exclusively Dental'),('Reference','Reference'),('Outpatient + Dental','Outpatient + Dental'),('Outpatient + Inpatient without obstetrics','Outpatient + Inpatient without obstetrics'),('Outpatient + Hospital with obstetrics','Outpatient + Hospital with obstetrics'),('Hospital with obstetrics + dental','Hospital with obstetrics + dental'),('Hospital without obstetrics + Dental','Hospital without obstetrics + Dental'),('Outpatient + Inpatient without obstetrics + Dental','Outpatient + Inpatient without obstetrics + Dental'),('Outpatient + Hospital with obstetrics + Dental','Outpatient + Hospital with obstetrics + Dental')],'Segmentation',track_visibility='onchange')

    upgrade_c = fields.Boolean('Upgrade',track_visibility='onchange')

    geo_scope_id = fields.Many2one('model_geographic_scope', string='Geographic Scope ID',track_visibility='onchange')
    product_region_ids = fields.One2many('product.region', 'product_id', string='Product Region IDS')
    product_network_ids = fields.One2many('product.network', 'product_id', string='Product Network IDS')
    network_provider_ids = fields.One2many('model_network_provider', 'product2_c', string='Network Provider IDS')
    product_price_ids = fields.One2many('product_price', 'Product_c', string='Product Price IDS')
    attachment_ids = fields.One2many('ir.attachment', 'product_id', string='Attachment IDS')
    product_family_id = fields.Many2one('product_family', string='Product Family Id',track_visibility='onchange')