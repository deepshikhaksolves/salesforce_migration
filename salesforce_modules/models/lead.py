from odoo import models, fields, api


class SalesforceLead(models.Model):
    _name = 'crm.lead'
    _inherit = ['crm.lead', 'mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Lead"

    actual_birth_policy__c = fields.Selection(
        [('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'),
         ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'),
         ('November', 'November'), ('December', 'December')], 'Actual Birth Policy',track_visibility='onchange')

    actual_carrier__c = fields.Many2one('account.account', string='Actual Carrier',track_visibility='onchange')

    actual_invoice__c = fields.Float('Actual Invoice', digits=(16, 2),track_visibility='onchange')
    actual_lifes__c = fields.Float('Actual Lifes', digits=(18, 0),track_visibility='onchange')

    street = fields.Char(track_visibility='onchange')
    street2 = fields.Char(track_visibility='onchange')
    zip = fields.Char(change_default=True,track_visibility='onchange')
    city = fields.Char(track_visibility='onchange')
    state_id = fields.Many2one("res.country.state", string='State', ondelete='restrict',
                               domain="[('country_id', '=?', country_id)]",track_visibility='onchange')
    country_id = fields.Many2one('res.country', string='Country', ondelete='restrict',track_visibility='onchange')

    actual_birth_policy_order__c = fields.Text('Current Order Policy Anniversary',track_visibility='onchange')
    AnnualRevenue = fields.Float('Annual Revenue', digits=(18, 0),track_visibility='onchange')

    Business_Name__c = fields.Char('Business Name', size=255,track_visibility='onchange')
    CNAE__c = fields.Many2one('model_cnae', string='NINE',track_visibility='onchange')
    CNPJ__c = fields.Char('CNPJ', size=18,track_visibility='onchange')
    Company = fields.Char('Company', size=255, track_visibility='onchange')

    Company_Segmentation__c = fields.Selection(
        [('Small', 'Recipe <40k'), ('Small_Large', 'Revenue between 40k and 100k'),
         ('Middle', 'Revenue between 100k and 250k'), ('Middle_Large', 'Revenue between 250k and 400k'),
         ('Corporate', 'Revenue between 400k and 1MM'), ('Corporate_Large', 'Revenue >1MM')], 'Company Segmentation',track_visibility='onchange')

    unqualified_account_source__c = fields.Many2one('account.account', string='Disqualification Account',track_visibility='onchange')
    converted__c = fields.Char('Converted',track_visibility='onchange')
    Broker__c = fields.Many2one('res.partner', string='Broker',track_visibility='onchange')
    cpf__c = fields.Char('CPF', size=14,track_visibility='onchange')
    # CreatedById already in odoo

    CurrentGenerators__c = fields.Char('Current Generator(s)', size=100,track_visibility='onchange')
    Date_of_Birth__c = fields.Date('Birth date',track_visibility='onchange')
    Jigsaw = fields.Char('Data.com Key', size=20,track_visibility='onchange')
    Description = fields.Char('Description', size=32000,track_visibility='onchange')
    DoNotCall = fields.Boolean('Do Not Call',track_visibility='onchange')
    # Email                   already in odoo i.e. (email_from)
    HasOptedOutOfEmail = fields.Boolean('HasOptedOutOfEmail',track_visibility='onchange')
    extension_number__c = fields.Float('Extension Number', digits=(10, 0),track_visibility='onchange')
    Fax = fields.Char('Fax',track_visibility='onchange')
    HasOptedOutOfFax = fields.Boolean('Fax Opt Out',track_visibility='onchange')
    Financial_Group__c = fields.Char('Financial Group', size=255,track_visibility='onchange')
    Mailing_Origin__c = fields.Char('Mailing Source', size=255,track_visibility='onchange')
    Nominative__c = fields.Boolean('Indicated',track_visibility='onchange')
    IndividualId = fields.Many2one('res.users', string='Individual',track_visibility='onchange')
    Industry = fields.Selection(
        [('Agriculture', 'Agriculture'), ('Banking', 'Banking'), ('Biotechnology', 'Biotechnology'),
         ('Food & Beverage', 'Food & Beverage'), ('Communications', 'Communications'), ('Construction', 'Construction'),
         ('Consulting', 'Consulting'), ('Education', 'Education'), ('Electronics', 'Electronics'), ('Energy', 'Energy'),
         ('Engineering', 'Engineering'), ('Entertainment', 'Entertainment'), ('Manufacturing', 'Manufacturing'),
         ('Chemicals', 'Chemicals'), ('Finance', 'Finance'), ('Government', 'Government'),
         ('Hospitality', 'Hospitality'), ('Machinery', 'Machinery'), ('Environmental', 'Environmental'),
         ('Media', 'Media'), ('Oil and gas', 'Oil and gas'), ('Recreation', 'Recreation'), ('Shipping', 'Shipping'),
         ('Healthcare', 'Healthcare'), ('Insurance', 'Insurance'), ('Not For Profit', 'Not For Profit'),
         ('Technology', 'Technology'), ('Telecommunications', 'Telecommunications'),
         ('Transportation', 'Transportation'), ('Utilities', 'Utilities'), ('Retail', 'Retail'), ('Apparel', 'Apparel'),
         ('Other', 'Other')], 'Industry',track_visibility='onchange')
    # LastModifiedById already in odoo
    LastTransferDate = fields.Date('Last Transfer Date',track_visibility='onchange')
    Lead__c = fields.Char('Lead',track_visibility='onchange')
    OwnerId = fields.Many2one('res.users', string='Lead Owner',track_visibility='onchange')
    # RecordTypeId already in odoo i.e(type)
    RecordTypeId = fields.Char(string='Record Type', track_visibility='onchange')

    LeadSource = fields.Selection(
        [('Quotator', 'Quotator'), ('Customer Event', 'Customer Event'), ('Exposure', 'Exposure'),
         ('Google AdWords', 'Google AdWords'), ('Employee Indication', 'Employee Indication'), ('Mailing', 'Mailing'),
         ('Partner', 'Partner'), ('Advertising', 'Advertising'), ('Site', 'Site'), ('Webinar', 'Webinar'),
         ('Others', 'Others')], 'Lead Source',track_visibility='onchange')

    # Status =  already in odoo i.e(stage_id)
    Locations__c = fields.Char('Locations', size=255,track_visibility='onchange')
    loss_comment__c = fields.Char('Loss Comment', size=255,track_visibility='onchange')
    # loss_reason__c         already in odoo i.e (lost_reason)
    mailing_file_name__c = fields.Char('Mailing File Name', size=255,track_visibility='onchange')
    # MobilePhone already in odoo i.e. (mobile)
    # Name already in odoo i.e. (name)
    NumberOfEmployees = fields.Float('No. of Employees', digits=(8, 0),track_visibility='onchange')
    NumberofLocations__c = fields.Float('Number of Locations', digits=(3, 0),track_visibility='onchange')
    Company_Origin__c = fields.Selection(
        [('New', 'New'), ('Cross Sell', 'Cross Sell'), ('Up Sell', 'Up Sell'), ('Drama', 'Drama'),
         ('redeployment', 'redeployment')], 'Company Origin',track_visibility='onchange')
    # Contact_Origin__c           = already in odoo i.e. source_id

    Owner_Division__c = fields.Char('Owner Division', size=255,track_visibility='onchange')
    PartnerAccountId = fields.Many2one('account.account', string='Partner Account',track_visibility='onchange')
    # Phone already in odoo i.e. (phone)
    Primary__c = fields.Selection([('No', 'No'), ('Yes', 'Yes')], 'Primary',track_visibility='onchange')
    ProductInterest__c = fields.Selection(
        [('Personal_Accidents', 'Personal Accident'), ('food', 'food'), ('GC3000 series', 'Car'), ('Fleet', 'Fleet'),
         ('medicine', 'medicine'), ('GC5000 series', 'Dental'), ('Snack', 'Snack'), ('GC1000 series', 'Health'),
         ('Mobile Support', 'Cell Phone Support'), ('Travel', 'Travel'), ('Life', 'Life')], 'Products of Interest',track_visibility='onchange')

    Rating = fields.Selection(
        [('Hot', 'Hot'), ('Cold', 'Cold'), ('Blocked', 'Blocked'), ('Global_Contract', 'Global_Contract'),
         ('No interest', 'No interest'), ('No Profile', 'No Profile'), ('Non-existent phone', 'Non-existent phone')],
        'Rating',track_visibility='onchange')

    rescue_date__c = fields.Date('Rescue Date',track_visibility='onchange')
    secondary_mobile_phone__c = fields.Char('Secondary Mobile Phone',track_visibility='onchange')
    Sales_Channel__c = fields.Many2one('channel_segmentation', string='Channel Segmentation',track_visibility='onchange')
    secondary_phone__c = fields.Char('Secondary phone',track_visibility='onchange')

    telemarketing__c = fields.Selection(
        [('Active', 'Active'), ('Receptive', 'Receptive'), ('Not applicable', 'Not applicable')], 'Telemarketing',track_visibility='onchange')

    Title = fields.Char('Title', size=128,track_visibility='onchange')
    Website = fields.Char('Website',track_visibility='onchange')
    Workflow_Configuration__c = fields.Many2one('workflow_configuration', string='Workflow Configuration',track_visibility='onchange')

    attachment_ids = fields.One2many('ir.attachment', 'lead_id', string='Attachment IDS')

    benifit_ids = fields.One2many('model_benfit_politic', 'lead_id', string='Benefit Politic')
    event_control_ids = fields.One2many('event_control', 'Opportunity_ID', string='Event Control Id')
