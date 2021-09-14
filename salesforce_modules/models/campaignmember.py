from odoo import models, fields, api

class CampaignMember(models.Model):
    _name = 'model_campaignmember'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Campaign Member"
    _rec_name = 'FirstName'

    # CreatedById  already in odoo
    # LastModifiedById already in odoo
    # CreatedDate already in odoo
    # LastModifiedDate already in odoo

    CampaignId = fields.Many2one('model_campaign',string='Campaign')
    City = fields.Char(string='City',size=40)
    CompanyOrAccount = fields.Char(string='Company (Account)', size=255)
    ContactId = fields.Many2one('res.partner',string='Contact')
    Country = fields.Char(string='Country',size=80)
    Description = fields.Char(string='Description',size=32000)
    DoNotCall = fields.Boolean(string='Do Not Call')
    Email = fields.Char(string='Email')
    HasOptedOutOfEmail = fields.Boolean(string='Email Opt Out')
    Fax = fields.Char(string='Fax')
    HasOptedOutOfFax = fields.Boolean(string='Fax Opt Out')
    FirstName = fields.Char(string='First Name')
    FirstRespondedDate = fields.Date(string='First Responded Date')
    LastName = fields.Char(string='Last Name',size=80)
    LeadId = fields.Many2one('crm.lead',string='Lead')
    LeadSource = fields.Selection([('Quotator','Quotator'),('Customer Event','Customer Event'),('Exposure','Exposure'),
                                   ('Google AdWords','Google AdWords'),('Employee Indication','Employee Indication'),
                                   ('Mailing','Mailing'),('Partner','Partner'),('Advertising','Advertising'),
                                   ('Site','Site'),('Webinar','Webinar'),('Others','Others')],string='Lead Source')
    MobilePhone = fields.Char(string='Mobile')
    Phone = fields.Char(string='Phone')
    HasResponded = fields.Boolean(string='Responded')
    Salutation = fields.Selection([('Mr.','Mr.'),('Ms.','Ms.')],string='Salutation')
    State = fields.Char(string='State/Province',size=80)
    Status = fields.Selection([('Answered','Answered'),('Sent','Sent')],string='Status')
    Street = fields.Char(string='Street',size=255)
    Title = fields.Char(string='Title',size=128)
    PostalCode = fields.Char(string='Zip/Postal Code',size=20)

