from odoo import models, fields, api


class Campaign(models.Model):
    _name = 'model_campaign'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Campaign"
    _rec_name = 'Name'

    IsActive = fields.Boolean('Active', track_visibility='onchange')
    ActualCost = fields.Float('Actual Cost in Campaign', digits=(18, 0), track_visibility='onchange')
    HierarchyActualCost = fields.Float('Actual Cost in Hierarchy', digits=(18, 0), track_visibility='onchange')
    BudgetedCost = fields.Float('Budgeted Cost in Campaign', digits=(18, 0), track_visibility='onchange')
    HierarchyBudgetedCost = fields.Float('Budgeted Cost in Hierarchy', digits=(18, 0), track_visibility='onchange')
    CampaignImageId = fields.One2many('ir.attachment', 'campaign_id', string='Campaign Image')
    CampaignMemberRecordTypeId = fields.Many2one('record_type', string='Campaign Member Type',
                                                 track_visibility='onchange')
    Name = fields.Char('Campaign Name', size=80, track_visibility='onchange')
    OwnerId = fields.Many2one('res.users', string='Campaign Owner', track_visibility='onchange')
    NumberOfContacts = fields.Integer('Contacts in Campaign', track_visibility='onchange')
    HierarchyNumberOfContacts = fields.Integer('Contacts in Hierarchy', track_visibility='onchange')
    NumberOfConvertedLeads = fields.Integer('Converted Leads in Campaign', track_visibility='onchange')
    HierarchyNumberOfConvertedLeads = fields.Integer('Converted Leads in Hierarchy', track_visibility='onchange')
    # CreatedById already in odoo
    Description = fields.Char('Description', size=32000, track_visibility='onchange')
    EndDate = fields.Date('End Date', track_visibility='onchange')
    ExpectedResponse = fields.Float('Expected Response (%)', digits=(8, 2), track_visibility='onchange')
    ExpectedRevenue = fields.Float('Expected Revenue in Campaign', digits=(18, 0), track_visibility='onchange')
    HierarchyExpectedRevenue = fields.Float('Expected Revenue in Hierarchy', digits=(18, 0),
                                            track_visibility='onchange')
    # LastModifiedById already in odoo
    NumberOfLeads = fields.Integer('Leads in Campaign', track_visibility='onchange')
    HierarchyNumberOfLeads = fields.Integer('Leads in Hierarchy', track_visibility='onchange')
    NumberSent = fields.Integer('Num Sent in Campaign', track_visibility='onchange')
    HierarchyNumberSent = fields.Integer('Num Sent in Hierarchy', track_visibility='onchange')
    NumberOfOpportunities = fields.Integer('Opportunities in Campaign', track_visibility='onchange')
    HierarchyNumberOfOpportunities = fields.Integer('Opportunities in Hierarchy', track_visibility='onchange')
    ParentId = fields.Many2one('model_campaign', string='Parent Campaign', track_visibility='onchange')
    Released_to_Work__c = fields.Boolean('Released to Work', track_visibility='onchange')
    Report_Used__c = fields.Char('Report Used (API)', size=100, track_visibility='onchange')
    NumberOfResponses = fields.Integer('Responses in Campaign', track_visibility='onchange')
    HierarchyNumberOfResponses = fields.Integer('Responses in Hierarchy', track_visibility='onchange')
    StartDate = fields.Date('Start Date', track_visibility='onchange')
    Status = fields.Selection(
        [('In Progress', 'In Progress'), ('Completed', 'Finished'), ('Aborted', 'Called off'), ('Planned', 'Planned')],
        'Status', track_visibility='onchange')
    Type = fields.Selection(
        [('Email', 'Email'), ('Event', 'Event'), ('Social Media', 'Social Media'), ('Other', 'Other'),
         ('Search', 'Search'), ('Referral Program', 'Advertising'), ('Website Direct', 'site'),
         ('Demo Signup / Trial', 'Test'), ('Mailing', 'Mailing')], 'Type', track_visibility='onchange')

    AmountAllOpportunities = fields.Float('Value Opportunities in Campaign', digits=(18, 0),
                                          track_visibility='onchange')
    HierarchyAmountAllOpportunities = fields.Float('Value Opportunities in Hierarchy', digits=(18, 0),
                                                   track_visibility='onchange')
    AmountWonOpportunities = fields.Float('Value Won Opportunities in Campaign', digits=(18, 0),
                                          track_visibility='onchange')
    HierarchyAmountWonOpportunities = fields.Float('Value Won Opportunities in Hierarchy', digits=(18, 0),
                                                   track_visibility='onchange')
    current__c = fields.Char('in force', track_visibility='onchange')
    NumberOfWonOpportunities = fields.Integer('Won Opportunities in Campaign', track_visibility='onchange')
    HierarchyNumberOfWonOpportunities = fields.Integer('Won Opportunities in Hierarchy', track_visibility='onchange')

    attachment_ids = fields.One2many('ir.attachment', 'campaign_id', string='Attachment IDS')
    opportunity_ids = fields.One2many('crm.lead', 'campaigns_id', string='Campaign IDS')
    campaign_member_ids = fields.One2many('model_campaignmember', 'CampaignId', string='Campaign Member IDS')
