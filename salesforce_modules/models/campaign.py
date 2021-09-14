from odoo import models, fields, api


class Campaign(models.Model):
    _name = 'model_campaign'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Campaign"
    _rec_name = 'Name'


    IsActive                    = fields.Boolean('Active')
    ActualCost                  = fields.Float('Actual Cost in Campaign', digits=(18, 0))
    HierarchyActualCost         = fields.Float('Actual Cost in Hierarchy', digits=(18, 0))
    BudgetedCost                = fields.Float('Budgeted Cost in Campaign', digits=(18, 0))
    HierarchyBudgetedCost       = fields.Float('Budgeted Cost in Hierarchy', digits=(18, 0))
    CampaignImageId             = fields.One2many('ir.attachment','campaign_id', string='Campaign Image')
    CampaignMemberRecordTypeId  = fields.Many2one('record_type', string='Campaign Member Type')
    Name                        = fields.Char('Campaign Name', size=80)
    OwnerId                     = fields.Many2one('res.users',string='Campaign Owner')
    NumberOfContacts            = fields.Integer('Contacts in Campaign')
    HierarchyNumberOfContacts   = fields.Integer('Contacts in Hierarchy')
    NumberOfConvertedLeads      = fields.Integer('Converted Leads in Campaign')
    HierarchyNumberOfConvertedLeads  = fields.Integer('Converted Leads in Hierarchy')
    # CreatedById already in odoo
    Description                 = fields.Char('Description', size=32000)
    EndDate                     = fields.Date('End Date')
    ExpectedResponse            = fields.Float('Expected Response (%)', digits=(8, 2))
    ExpectedRevenue             = fields.Float('Expected Revenue in Campaign', digits=(18, 0))
    HierarchyExpectedRevenue    = fields.Float('Expected Revenue in Hierarchy', digits=(18, 0))
    # LastModifiedById already in odoo
    NumberOfLeads               = fields.Integer('Leads in Campaign')
    HierarchyNumberOfLeads      = fields.Integer('Leads in Hierarchy')
    NumberSent                  = fields.Integer('Num Sent in Campaign')
    HierarchyNumberSent         = fields.Integer('Num Sent in Hierarchy')
    NumberOfOpportunities       = fields.Integer('Opportunities in Campaign')
    HierarchyNumberOfOpportunities       = fields.Integer('Opportunities in Hierarchy')
    ParentId                    = fields.Many2one('model_campaign',string='Parent Campaign')
    Released_to_Work__c         = fields.Boolean('Released to Work')
    Report_Used__c              = fields.Char('Report Used (API)', size=100)
    NumberOfResponses           = fields.Integer('Responses in Campaign')
    HierarchyNumberOfResponses  = fields.Integer('Responses in Hierarchy')
    StartDate                   = fields.Date('Start Date')
    Status                      = fields.Selection([('In Progress', 'In Progress'),('Completed', 'Finished'),('Aborted', 'Called off'),('Planned', 'Planned')],'Status')
    Type                        = fields.Selection([('Email', 'Email'),('Event', 'Event'),('Social Media', 'Social Media'),('Other', 'Other'),('Search', 'Search'),('Referral Program', 'Advertising'),('Website Direct', 'site'),('Demo Signup / Trial', 'Test'),('Mailing', 'Mailing')],'Type')

    AmountAllOpportunities      = fields.Float('Value Opportunities in Campaign', digits=(18, 0))
    HierarchyAmountAllOpportunities = fields.Float('Value Opportunities in Hierarchy', digits=(18, 0))
    AmountWonOpportunities      = fields.Float('Value Won Opportunities in Campaign', digits=(18, 0))
    HierarchyAmountWonOpportunities      = fields.Float('Value Won Opportunities in Hierarchy', digits=(18, 0))
    current__c                  = fields.Char('in force')
    NumberOfWonOpportunities    = fields.Integer('Won Opportunities in Campaign')
    HierarchyNumberOfWonOpportunities = fields.Integer('Won Opportunities in Hierarchy')

    attachment_ids  = fields.One2many('ir.attachment','campaign_id', string='Attachment IDS')


