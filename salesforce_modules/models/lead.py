from odoo import models, fields, api


class SalesforceLead(models.Model):
    _inherit = 'crm.lead'
    _description = "Salesforce Lead"

    actual_birth_policy__c  = fields.Selection([('January','January'),('February','February'),('March','March'),('April','April'),('May','May'),('June','June'),('July','July'),('August','August'),('September','September'),('October','October'),('November','November'),('December','December')],'Actual Birth Policy')

    actual_carrier__c       = fields.Many2one('account.account', string='Actual Carrier')
    actual_invoice__c       = fields.Many2one('res.currency', string='Actual Invoice', default=lambda self: self.env.user.company_id.currency_id.id)
    actual_lifes__c         = fields.Integer('Actual Lifes')

    street                  = fields.Char()
    street2                 = fields.Char()
    zip                     = fields.Char(change_default=True)
    city                    = fields.Char()
    state_id                = fields.Many2one("res.country.state", string='State', ondelete='restrict', domain="[('country_id', '=?', country_id)]")
    country_id              = fields.Many2one('res.country', string='Country', ondelete='restrict')

    actual_birth_policy_order__c    = fields.Text('Current Order Policy Anniversary')
    AnnualRevenue           = fields.Many2one('res.currency', string='Annual Revenue', default=lambda self: self.env.user.company_id.currency_id.id)

    Business_Name__c        = fields.Text('Business Name',size=255)
    CNAE__c                 = fields.Many2one('model_cnae',string='NINE')
    CNPJ__c                 = fields.Text('CNPJ',size=18)
    Company                 = fields.Text('Company',size=255)

    Company_Segmentation__c  = fields.Selection([('Small','Recipe <40k'),('Small_Large','Revenue between 40k and 100k'),('Middle','Revenue between 100k and 250k'),('Middle_Large','Revenue between 250k and 400k'),('Corporate','Revenue between 400k and 1MM'),('Corporate_Large','Revenue >1MM')],'Company Segmentation')

    unqualified_account_source__c   = fields.Many2one('account.account', string='Disqualification Account')
    converted__c             = fields.Char('Converted')
    Broker__c                = fields.Many2one('res.partner',string='Broker')
    cpf__c                   = fields.Text('CPF',size=14)
    # CreatedById already in odoo

    CurrentGenerators__c    = fields.Text('Current Generator(s)',size=100)
    Date_of_Birth__c        = fields.Date('Birth date')
    Jigsaw                  = fields.Text('Data.com Key',size=20)
    Description             = fields.Text('Description',size=32000)
    DoNotCall               = fields.Boolean('Do Not Call')
    Email                   = fields.Char('Email')
    HasOptedOutOfEmail      = fields.Boolean('HasOptedOutOfEmail')
    extension_number__c     = fields.Integer('Extension Number')
    Fax                     = fields.Char('Fax')
    HasOptedOutOfFax        = fields.Boolean('Fax Opt Out')
    Financial_Group__c      = fields.Text('Financial Group',size=255)
    Mailing_Origin__c       = fields.Text('Mailing Source',size=255)
    Nominative__c           = fields.Boolean('Indicated')
    IndividualId            = fields.Many2one('res.users',string='Individual')
    Industry                = fields.Selection([('Agriculture','Agriculture'),('Banking','Banking'),('Biotechnology','Biotechnology'),('Food & Beverage','Food & Beverage'),('Communications','Communications'),('Construction','Construction'),('Consulting','Consulting'),('Education','Education'),('Electronics','Electronics'),('Energy','Energy'),('Engineering','Engineering'),('Entertainment','Entertainment'),('Manufacturing','Manufacturing'),('Chemicals','Chemicals'),('Finance','Finance'),('Government','Government'),('Hospitality','Hospitality'),('Machinery','Machinery'),('Environmental','Environmental'),('Media','Media'),('Oil and gas','Oil and gas'),('Recreation','Recreation'),('Shipping','Shipping'),('Healthcare','Healthcare'),('Insurance','Insurance'),('Not For Profit','Not For Profit'),('Technology','Technology'),('Telecommunications','Telecommunications'),('Transportation','Transportation'),('Utilities','Utilities'),('Retail','Retail'),('Apparel','Apparel'),('Other','Other')],'Industry')
    # LastModifiedById already in odoo
    LastTransferDate        = fields.Date('Last Transfer Date')
    Lead__c                 = fields.Char('Lead')
    OwnerId                 = fields.Many2one('res.users',string='Lead Owner')
    # RecordTypeId already in odoo i.e(type)

    LeadSource              = fields.Selection([('Quotator', 'Quotator'),('Customer Event', 'Customer Event'),('Exposure', 'Exposure'),('Google AdWords', 'Google AdWords'),('Employee Indication', 'Employee Indication'),('Mailing', 'Mailing'),('Partner', 'Partner'),('Advertising', 'Advertising'),('Site', 'Site'),('Webinar', 'Webinar'),('Others', 'Others')],'Lead Source')

    LeadSource              = fields.Selection([('Quotator', 'Quotator'),('Customer Event', 'Customer Event'),('Exposure', 'Exposure'),('Google AdWords', 'Google AdWords'),('Employee Indication', 'Employee Indication'),('Mailing', 'Mailing'),('Partner', 'Partner'),('Advertising', 'Advertising'),('Site', 'Site'),('Webinar', 'Webinar'),('Others', 'Others')],'Lead Source')

    # Status =  already in odoo i.e(stage_id)
    Locations__c            = fields.Text('Locations',size=255)
    loss_comment__c         = fields.Text('Loss Comment',size=255)
    # loss_reason__c         already in odoo i.e (lost_reason)
    mailing_file_name__c    = fields.Text('Mailing File Name',size=255)
    # MobilePhone already in odoo i.e. (mobile)
    # Name already in odoo i.e. (name)
    NumberOfEmployees       = fields.Integer('No. of Employees')
    NumberofLocations__c    = fields.Integer('Number of Locations')
    Company_Origin__c       = fields.Selection([('New', 'New'),('Cross Sell', 'Cross Sell'),('Up Sell', 'Up Sell'),('Drama', 'Drama'),('redeployment', 'redeployment')],'Company Origin')
    # Contact_Origin__c           = already in odoo i.e. source_id

    Owner_Division__c       = fields.Text('Owner Division',size=255)
    PartnerAccountId        = fields.Many2one('account.account',string='Partner Account')
    # Phone already in odoo i.e. (phone)
    Primary__c              = fields.Selection([('No', 'No'),('Yes', 'Yes')],'Primary')
    ProductInterest__c      = fields.Selection([('Personal_Accidents', 'Personal Accident'),('food', 'food'),('GC3000 series', 'Car'),('Fleet', 'Fleet'),('medicine', 'medicine'),('GC5000 series', 'Dental'),('Snack', 'Snack'),('GC1000 series', 'Health'),('Mobile Support', 'Cell Phone Support'),('Travel', 'Travel'),('Life', 'Life')],'Products of Interest')

    Rating                   = fields.Selection([('Hot', 'Hot'),('Cold', 'Cold'),('Blocked', 'Blocked'),('Global_Contract', 'Global_Contract'),('No interest', 'No interest'),('No Profile', 'No Profile'),('Non-existent phone', 'Non-existent phone')],'Rating')

    rescue_date__c          = fields.Date('Rescue Date')
    secondary_mobile_phone__c = fields.Char('Secondary Mobile Phone')
    # Sales_Channel__c          = fields.
    secondary_phone__c      = fields.Char('Secondary phone')

    telemarketing__c        = fields.Selection([('Active', 'Active'),('Receptive', 'Receptive'),('Not applicable', 'Not applicable')],'Telemarketing')

    Title                   = fields.Text('Title',size=128)
    Website                 = fields.Char('Website')
    # Workflow_Configuration__c = 
    
   
    