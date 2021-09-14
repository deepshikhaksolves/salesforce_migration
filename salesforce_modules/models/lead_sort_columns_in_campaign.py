from odoo import models, fields, api


class LeadSortColumns(models.Model):
    _name = 'lead_sort_colums_in_capaign'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Lead Sort Columns"
    _rec_name = 'Name'

    Campaign__c = fields.Many2one('model_campaign', string='Campaign')
    # CreatedById already in odoo
    Name = fields.Char('Code')
    Field__c = fields.Selection(
        [('AnnualRevenue', 'Annual Revenue'), ('Broker__c', 'Broker'), ('Business_Name__c', 'Business Name'),
         ('CNAE__c', 'CNAE'), ('CNPJ__c', 'CNPJ'), ('Company', 'Company'),
         ('Company_Origin__c', 'Company Segmentation'), ('Contact_Origin__c', 'Contact Origin'),
         ('CurrentGenerators__c', 'Current Generators'), ('Date_of_Birth__c', 'Date of Birth'),
         ('Description', 'Description'), ('DoNotCall', 'Do Not Call'), ('Email', 'Email'), ('Industry', 'Industry'),
         ('LastTransferDate', 'Last Transfer Date'), ('LeadSource', 'Lead Source'),
         ('Mailing_Origin__c', 'Mailing Origin'), ('MobilePhone', 'Mobile Phone'), ('Name', 'Name'),
         ('NumberOfEmployees', 'Number Of Employees'), ('NumberofLocations__c', 'Number of Locations'),
         ('Phone', 'Phone'), ('Primary__c', 'Primary'), ('ProductInterest__c', 'Product Interest'),
         ('Rating', 'Rating'), ('Sales_Channel__c', 'Sales Channel'), ('SICCode__c', 'SIC Code'), ('Status', 'Status'),
         ('Title', 'Title'), ('Address', 'Address')], 'Field')

    Field_of_Lead__c = fields.Char('Field of Lead')
    # LastModifiedById already in odoo
    OwnerId = fields.Many2one('res.users', string='Owner')
    SortOrder__c = fields.Selection([('ASC', 'ASC'), ('DESC', 'DESC')], 'SortOrder')
