# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, timedelta

# class CustomPartner(models.Model):
#     """
#     Add fields in res.partner
#
#     """
#     _inherit = "res.partner"
#
#     # Contact
#     sf_design = fields.Char('Design')
#     sf_contact_id = fields.Char(string="SalesForce Contact Id", readonly=True, index=True)
#     sf_related_account_id = fields.Many2one('res.partner', string="Account ID", readonly=True)
#     sf_asst_name = fields.Char(string="AssistantName", readonly=True)
#     sf_asst_phone = fields.Char(string='Assistant Phone', readonly=True)
#     sf_birth_date = fields.Date(string='Birth Date', readonly=True)
#     sf_department = fields.Char(string="Sf Department", readonly=True)
#     sf_email_bounce_date = fields.Datetime(string='Email Bounced Date', readonly=True)
#     sf_email_bounce_rsn = fields.Char(string="Email Bounced Reason", readonly=True)
#     sf_first_name = fields.Char(string="First Name", readonly=True)
#     sf_is_mail_bounced = fields.Boolean(string="Is Email Bounced", readonly=True)
#     sf_jigsaw_contact_id = fields.Char(string="Jigsaw Contact Id", readonly=True)
#     sf_last_name = fields.Char(string="Last Name", readonly=True)
#     sf_lst_ref_data = fields.Datetime(string='Last Reference Date', readonly=True)
#     sf_lead_source = fields.Selection([('Partner Referral', 'Partner Referral'), ('Web', 'Web'),
#                                        ('Phone Inquiry', 'Phone Inquiry'), ('Other', 'Other'),
#                                        ('Purchased List', 'Purchased List'), ('Trade Show', 'Trade Show'),
#                                        ('External Referral','External Referral'), ('Word of mouth','Word of mouth'),
#                                        ('Public Relations','Public Relations'), ('Partner','Partner'),
#                                        ('Thomas Net','ThomasNet'), ('Greg Papandrew','Greg Papandrew'),
#                                        ('Global Spec','Global Spec'), ('3D Instruments, LLC','3D Instruments, LLC'),
#                                        ('4DSP, LLC','4DSP, LLC')], string="Lead Source", readonly=True)
#     sf_mailing_city = fields.Char(string="Mailing City", readonly=True)
#     sf_mailing_country = fields.Char(string="Mailing Country", readonly=True)
#     sf_mailing_geocode_accuracy = fields.Selection([('Address', 'Address'), ('NearAddress', 'NearAddress'),
#                                                     ('Block', 'Block'), ('Street', 'Street'), ('Zip', 'Zip'),
#                                                     ('ExtendedZip', 'ExtendedZip'), ('Neighborhood', 'Neighborhood'),
#                                                     ('City', 'City'), ('Country', 'Country'), ('State', 'State'),
#                                                     ('Unknown', 'Unknown')], string="Mailing Geocode Accuracy",
#                                                    readonly=True)
#     sf_mailing_latitude = fields.Float(string="Mailing Latitude", readonly=True)
#     sf_mailing_longitude = fields.Float(string="Mailing Longitude", readonly=True)
#     sf_mailing_postalcode = fields.Char(string="Mailing PostalCode", readonly=True)
#     sf_mailing_state = fields.Char(string="Mailing State", readonly=True)
#     sf_mailing_street = fields.Char(string="Mailing Street", readonly=True)
#     sf_reports_to = fields.Many2one('res.partner', string="Reports To Id", readonly=True)
#     sf_other_city = fields.Char(string="Other City", readonly=True)
#     sf_other_country = fields.Char(string="Other Country", readonly=True)
#     sf_other_geocode_accuracy = fields.Selection([('Address', 'Address'), ('NearAddress', 'NearAddress'),
#                                                     ('Block', 'Block'), ('Street', 'Street'), ('Zip', 'Zip'),
#                                                     ('ExtendedZip', 'ExtendedZip'), ('Neighborhood', 'Neighborhood'),
#                                                     ('City', 'City'), ('Country', 'Country'), ('State', 'State'),
#                                                     ('Unknown', 'Unknown')], string="Other Geocode Accuracy",
#                                                    readonly=True)
#     sf_other_latitude = fields.Float(string="Other Latitude", readonly=True)
#     sf_other_longitude = fields.Float(string="Other Longitude", readonly=True)
#     sf_other_postalcode = fields.Char(string="Other PostalCode", readonly=True)
#     sf_other_state = fields.Char(string="Other State", readonly=True)
#     sf_other_street = fields.Char(string="Other Street", readonly=True)
#     sf_salutation = fields.Selection([('Mr.', 'Mr.'), ('Ms.', 'Ms.'), ('Mrs.', 'Mrs.'), ('Dr.', 'Dr.'),
#                                       ('Prof.', 'Prof.')], string="Salutation")
#     sf_title = fields.Char(string="Salesforce Title", readonly=True)
#
#     sf_country_name = fields.Char(string='Sf Country name')
#     sf_country_id = fields.Many2one('sf.country.map',string='Country id')
#     sf_state = fields.Char(string='Salesforce State name')
#     sf_state_id = fields.Many2one('sf.state.map',string='State id')
#     # Account
#     sf_account_id = fields.Char(string="SalesForce Account Id", readonly=True, index=True)
#     sf_company_number_of_employees = fields.Char('No of employees')
#     sf_individual_rel_id = fields.Many2one('res.partner', string="Individual Id", readonly=True)
#     sf_customer_name = fields.Char(string="Customer Name", readonly=True)
#     sf_account_source = fields.Selection([('YES', 'YES'), ('NO', 'NO'), ('MAYBE', 'MAYBE'), ('External Referral', 'External Referral'), ('Partner', 'Partner'),
#                                           ('Greg Papandrew', 'Greg Papandrew'), ('Trade Show', 'Trade Show'),
#                                           ('Web', 'Web'), ('Word of mouth', 'Word of mouth'), ('Other', 'Other'),
#                                           ('Thomas Net', 'Thomas Net'), ('Global Spec', 'Global Spec')],
#                                          string="Account Source", readonly=True)
#     sf_annualrevenue = fields.Float(string="Sf Annual Revenue", readonly=True)
#     assembly_account_status = fields.Selection(selection_add=[('COLD', 'COLD'), ('HOT', 'HOT'),
#                                                               ('WARM', 'WARM'),
#                                                               ('BC LIST', 'BC LIST'),
#                                                               ('CLOSED', 'CLOSED'), ('WRONG #', 'WRONG #')])
#     sf_assembly_first_order__c = fields.Date(string='Assembly_First_Order__c', readonly=True)
#     sf_billing_city = fields.Char(string="Billing City", readonly=True)
#     sf_billing_country = fields.Char(string="Billing Country", readonly=True)
#     sf_billing_geocode_accuracy = fields.Selection([('Address', 'Address'), ('NearAddress', 'NearAddress'),
#                                                    ('Block', 'Block'), ('Street', 'Street'), ('Zip', 'Zip'),
#                                                    ('ExtendedZip', 'ExtendedZip'), ('Neighborhood', 'Neighborhood'),
#                                                    ('City', 'City'), ('Country', 'Country'), ('State', 'State'),
#                                                    ('Unknown', 'Unknown')], string="Billing Geocode Accuracy",
#                                                    readonly=True)
#     sf_billing_latitude = fields.Float(string="Billing Latitude", readonly=True)
#     sf_billing_longitude = fields.Float(string="Billing Longitude", readonly=True)
#     sf_billing_postalcode = fields.Char(string="Billing PostalCode", readonly=True)
#     sf_billing_state = fields.Char(string="Billing State", readonly=True)
#     sf_billing_street = fields.Char(string="Billing Street", readonly=True)
#     sf_buyer_notes__c = fields.Text(string="Buyer_Notes__c", readonly=True)
#     sf_comments_2__c = fields.Text(string="Comments_2__c", readonly=True)
#     sf_comments__c = fields.Text(string="Comments__c", readonly=True)
#     # company_business_type = fields.Selection(selection_add=[("Don\'t Know", "Don\'t Know")])
#     # sf_classification__c = fields.Selection([('Guppy', 'Guppy'), ('Minnow', 'Minnow'), ('Tuna', 'Tuna'),
#     #                                          ('Whale', 'Whale')], string="Classification__c", readonly=True)
#     # sf_company_type__c = fields.Selection([('CM', 'CM'), ('OEM', 'OEM'), ('Design', 'Design'), ('Other', 'Other'),
#     #                                        ("Don't Know", "Don't Know")], string="Company_Type__c", readonly=True)
#     sf_connection_rcv_id = fields.Many2one('sf.pnc', string="Connection Received Id", readonly=True)
#     sf_connection_snt_id = fields.Many2one('sf.pnc', string="Connection Sent Id", readonly=True)
#     sf_credit_ref__c = fields.Text(string="Credit_Reference__c", readonly=True)
#     sf_description = fields.Text(string="Description", readonly=True)
#     sf_estimated_pcb_expense__c = fields.Float(string="Estimated_PCB_Expense__c", readonly=True)
#     sf_expected_annual_spend__c = fields.Float(string="Expected_Annual_Spend__c", readonly=True)
#     sf_interested_in_assembly__c = fields.Boolean(string="Interested_in_Assembly__c", readonly=True)
#     sf_is_deleted = fields.Boolean(string="Is Deleted", readonly=True)
#     sf_jigsaw_com_id = fields.Char(string="Jigsaw Company Id", readonly=True)
#     sf_lead_status__c = fields.Selection([('CUSTOMER', 'CUSTOMER'), ('COLD', 'COLD'), ('CLOSED', 'CLOSED'),
#                                           ('BC LIST', 'BC LIST'), ('HOT', 'HOT'), ('WARM', 'WARM'), ('NF', 'NF'),
#                                           ('NI', 'NI'), ('WRONG #', 'WRONG #')], string="Lead_Status__c", readonly=True)
#     sf_master_rec_id = fields.Many2one('res.partner', string="Master Record Id", readonly=True)
#     sf_partner_id = fields.Many2one('res.partner', string="Partner Id", readonly=True)
#     sf_photo_url = fields.Char('Photo Url', readonly=True)
#     sf_prospecting__c = fields.Boolean(string="Prospecting__c", readonly=True)
#     sf_rep_name__c = fields.Many2one('sf.rep__c', string="Rep_Name__c", readonly=True)
#     sf_shipping_city = fields.Char(string="Shipping City", readonly=True)
#     sf_shipping_country = fields.Char(string="Shipping Country", readonly=True)
#     sf_shipping_geocode_accuracy = fields.Selection([('Address', 'Address'), ('NearAddress', 'NearAddress'),
#                                                     ('Block', 'Block'), ('Street', 'Street'), ('Zip', 'Zip'),
#                                                     ('ExtendedZip', 'ExtendedZip'), ('Neighborhood', 'Neighborhood'),
#                                                     ('City', 'City'), ('Country', 'Country'), ('State', 'State'),
#                                                     ('Unknown', 'Unknown')], string="Shipping Geocode Accuracy",
#                                                     readonly=True)
#     sf_shipping_latitude = fields.Float(string="Shipping Latitude", readonly=True)
#     sf_shipping_longitude = fields.Float(string="Shipping Longitude", readonly=True)
#     sf_shipping_postalcode = fields.Char(string="Shipping PostalCode", readonly=True)
#     sf_shipping_state = fields.Char(string="Shipping State", readonly=True)
#     sf_shipping_street = fields.Char(string="Shipping Street", readonly=True)
#     sf_sp_acc_status__c = fields.Selection([('GET INFO', 'GET INFO'), ('CUSTOMER', 'CUSTOMER'), ('NF', 'NF'),
#                                             ('NI', 'NI'), ('QUOTED', 'QUOTED')], string="Solder Paste Account Status",
#                                            readonly=True)
#     sf_sp_notes__c = fields.Text(string='Solder Paste Notes c', readonly=True)
#     sf_stencil_notes__c = fields.Text(string='Stencil Notes', readonly=True)
#     sf_type = fields.Selection([('Customer - Direct', 'Customer - Direct'), ('Customer - Channel', 'Customer - Channel'),
#                                 ('Prospect','Prospect'),('Channel Partner / Reseller','Channel Partner / Reseller'),
#                                 ('Installation Partner','Installation Partner'),
#                                 ('Technology Partner','Technology Partner'),
#                                 ('Other','Other'),('Customer','Customer'),('Not Interested','Not Interested'),
#                                 ('Not a Fit','Not a Fit'),('Lead','Lead'),
#                                 ('Out of Business','Out of Business'),('Inactive','Inactive'),('Partner','Partner'),
#                                 ('Competitor','Competitor'),('Not Interested','Not Interested')],
#                                readonly=True)
#     sf_velegrity__c = fields.Text(string='Velegrity__c', readonly=True)
#     stencil_account_status = fields.Selection(selection_add=[('No', 'No')])
#     sf_source__c = fields.Selection([('IPC', 'IPC'), ('Referral', 'Referral'), ('Web Search', 'Web Search'),
#                                      ('Burhan', 'Burhan'), ('SMTA', 'SMTA')], string="Source", readonly=True)
#     # sf_square_footage__c = fields.Float(string="Square_Footage__c", readonly=True)
#     # sf_no_of_employees__c = fields.Float(string="Number_of_Employees__c", readonly=True)
#
#     # Individual
#     sf_individual_id = fields.Char(string="SalesForce Individual Id", readonly=True)
#     sf_can_store_pii_elsewhere = fields.Boolean(string="Can Store Pii Else where", readonly=True)
#     sf_children_count = fields.Integer(string="Children Count", readonly=True)
#     sf_consume_credit_score = fields.Integer(string="Consume Credit Score", readonly=True)
#     sf_ccs_povider_name = fields.Char(string="Consumer Credit Score Provider Name", readonly=True)
#     sf_convictions_count = fields.Integer(string="Convictions Count", readonly=True)
#     sf_death_date = fields.Date(string='Death Date', readonly=True)
#     sf_hasoptedoutgeo_track = fields.Boolean(string="HasOptedOutGeoTracking", readonly=True)
#     sf_hasoptedout_processing = fields.Boolean(string="HasOptedOutProcessing", readonly=True)
#     sf_hasoptedout_profiling = fields.Boolean(string="HasOptedOutProfiling", readonly=True)
#     sf_hasoptedout_solicit = fields.Boolean(string="HasOptedOutSolicit", readonly=True)
#     sf_hasoptedout_trac = fields.Boolean(string="HasOptedOutTracking", readonly=True)
#     sf_individual_age = fields.Selection([('13 or Older', '13 or Older'), ('16 or Older', '16 or Older')],
#                                          string="Individuals Age", readonly=True)
#     sf_influencer_rating = fields.Integer(string="InfluencerRating", readonly=True)
#     sf_is_home_own = fields.Boolean(string="IsHomeOwner", readonly=True)
#     sf_military_service = fields.Selection([('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')],
#                                          string="MilitaryService", readonly=True)
#     sf_occupation = fields.Char(string="Occupation", readonly=True)
#     sf_sendindividualdata = fields.Boolean(string="SendIndividualData", readonly=True)
#     sf_should_forget = fields.Boolean(string="ShouldForget", readonly=True)
#     sf_created_date = fields.Datetime(string="Partner Created Date")
#     sf_last_modified_date = fields.Datetime(string="Partner Last Modified Date")
#     # user fields
#     sf_salesperson_id = fields.Char('Salesforce Salesperson Id', readonly=True)
#     sf_created_by_id = fields.Char('Sf CreatedBy Id')
#     sf_last_modified_by_id = fields.Char('Sf LastModifiedBy Id')

# class CustomLead(models.Model):
#     """
#     Adds custom fields in crm.lead model
#     """
#     _inherit = "crm.lead"
#
#     sf_name = fields.Char(string="Sales Force Name")
#     sf_id = fields.Char(string="SalesForce Opportunity Id", index=True)
#     sf_amount = fields.Float(string="Amount")
#     sf_connection_rcv_id = fields.Many2one('sf.pnc', string="Connection Received Id", readonly=True)
#     sf_connection_snt_id = fields.Many2one('sf.pnc', string="Connection Sent Id", readonly=True)
#     sf_contact_id = fields.Many2one('res.partner', string="Conatct Id", readonly=True)
#     sf_fiscal = fields.Char(string="Fiscal")
#     sf_fiscal_quarter = fields.Integer(string="Fiscal Quarter")
#     sf_fiscal_year = fields.Integer(string="Fiscal Year")
#     sf_stage_name = fields.Char(string='Sf stage name')
#     sf_forecast_category = fields.Selection([('Omitted', 'Omitted'), ('Pipeline', 'Pipeline'),
#                                              ('Best Case', 'Best Case'), ('Commit', 'Commit'), ('Closed', 'Closed')],
#                                             string="ForecastCategory")
#     # sf_forecast_cat_name = fields.Selection([('Omitted', 'Omitted'), ('Pipeline', 'Pipeline'),
#     # ('Best Case', 'Best Case'), ('Commit', 'Commit'), ('Closed', 'Closed')],string="ForecastCategoryname")
#
#     sf_has_opn_activity = fields.Boolean(string="HasOpenActivity")
#     sf_has_opp_lineitem = fields.Boolean(string="HasOpportunityLineItem")
#     sf_has_overduetask = fields.Boolean(string="HasOverdueTask")
#     sf_is_closed = fields.Boolean(string="IsClosed")
#     sf_is_deleted = fields.Boolean(string="IsDeleted")
#     sf_is_won = fields.Boolean(string="IsWon")
#     sf_stencil_amount = fields.Float(string="Stencil_Amount__c")
#     sf_tariff_amount = fields.Float(string="Tariff_Amount__c")
#     sf_stencil__c = fields.Selection([('CHECKING', 'CHECKING'), ('ORDERED', 'ORDERED'), ('NOT NEEDED', 'NOT NEEDED'),
#                                       ("DOESN'T BUY", "DOESN'T BUY")], string="Stencil__c")
#     # sf_quote_type__c = fields.Selection([('Bid for Bid', 'Bid for Bid'), ('Bid for Buy', 'Bid for Buy'),
#     # ("Unknown", "Unknown")], string="Quote_Type__c")
#     sf_potential_customer = fields.Boolean(string="Potential_Customer__c")
#     sf_pcb_amount = fields.Float(string="PCB_Amount__c")
#     sf_open_date = fields.Date(string="Open Date")
#     sf_closed_date = fields.Date(string="Opportunity Closed Date")
#     sf_feed_back = fields.Text('Feedback')
#     sf_expected_order_val = fields.Float(string="Expected_Order_Value__c")
#     sf_company_type = fields.Selection([('OEM', 'OEM'), ('CM', 'CM'), ('Design', 'Design'), ('Other','Other'),
#                                         ("Don't Know", "Don't Know")], string="Company_Type__c")
#     sf_comment = fields.Text('Comments__c')
#     sf_buyer_feedback = fields.Char(string="Buyer_Feedback__c")
#     sf_blanket_order = fields.Boolean(string="Blanket_Order__c")
#     sf_assembly = fields.Boolean(string="Assembly__c")
#     sf_assembly_amount = fields.Float(string="Assembly_Amount__c")
#     sf_created_date = fields.Datetime(string="Opportunity Created Date")
#     sf_last_modified_date = fields.Datetime(string="Opportunity Last Modified Date")
#     # RVQ type for Quote_Type__c
#     RFQ_type = fields.Many2one('sf.quote.type.map', string='RFQ Type')
#
#     # Lead
#     sf_salesperson_id = fields.Char('Salesforce OwnerId', readonly=True)
#     sf_created_by_id = fields.Char('Sf CreatedById')
#     sf_last_modified_by_id = fields.Char('Sf LastModifiedById')
#     sf_comment_2__c = fields.Text('Comments_2_c')
#     sf_master_rec_id = fields.Many2one('res.partner', string="Master Record Id", readonly=True)
#     sf_individual_rel_id = fields.Many2one('res.partner', string="Individual Id", readonly=True)
#     sf_address = fields.Text('Sf Address')
#     # sf_company = fields.Char('Sf Company')
#     sf_country = fields.Char('Sf Country')
#     sf_email = fields.Char('Sf Email')
#     sf_is_converted = fields.Boolean('Sf Is Converted')
#     sf_lead_source = fields.Selection([('Partner Referral', 'Partner Referral'), ('Web', 'Web'),
#                                        ('Phone Inquiry', 'Phone Inquiry'), ('Other', 'Other'),
#                                        ('Purchased List', 'Purchased List'), ('Trade Show', 'Trade Show'),
#                                        ('External Referral','External Referral'), ('Word of mouth','Word of mouth'),
#                                        ('Public Relations','Public Relations'), ('Partner','Partner'),
#                                        ('Thomas Net','ThomasNet'), ('Greg Papandrew','Greg Papandrew'),
#                                        ('Global Spec','Global Spec'), ('3D Instruments, LLC','3D Instruments, LLC'),
#                                        ('4DSP, LLC','4DSP, LLC')], string="Lead Source", readonly=True)
#     sf_description = fields.Text(string="Description")
#     sf_lead_status = fields.Selection([('CUSTOMER', 'CUSTOMER'), ('COLD', 'COLD'), ('CLOSED', 'CLOSED'),
#                                        ('BC LIST', 'BC LIST'), ('HOT', 'HOT'), ('WARM', 'WARM'), ('NF', 'NF'),
#                                        ('NI', 'NI'), ('WRONG #', 'WRONG #'), ('OPEN','OPEN'), ('Mailing', 'Mailing'),
#                                        ("Don't Buy PCB's", "Don't Buy PCB's")]
#                                       , string="Lead_Status")
#     sf_interested_in_assembly__c = fields.Selection([('YES', 'YES'), ('NO', 'NO'), ('MAYBE', 'MAYBE'),
#                                                      ], string="Sf Interested in Assembly")
#     sf_lead_stencil__c = fields.Selection([("Don't Know", "Don't Know"), ('Yes', 'Yes'), ('No', 'No')],
#                                           string="Lead Stencil__c")
#     sf_lead_stencil_notes__c = fields.Text(string='Stencil Notes')
#     sf_EmailBouncedDate = fields.Datetime(string='Email Bounced Date')
#     sf_EmailBouncedReason = fields.Text(string='Email Bounced Reason')
#     sf_lead_expected_annual_spend__c = fields.Float(string="Expected_Annual_Spend__c", readonly=True)
#     sf_title = fields.Char(string="Salutation")
#
#     # company_business_type = fields.Selection(selection_add=[("Don\'t Know", "Don\'t Know")])
#     sf_state = fields.Char('Sf State')
#     sf_street = fields.Char('Sf Street')
#     sf_postal_code = fields.Char('Postal Code')
#     sales_import_status = fields.Selection([('imported', 'Imported'), ('not_imported', 'Not Imported Yet'),
#                                             ('failed_import', 'Import Failed'), ('re_import', 'Re Importing')],
#                                            string='Import Status', default='not_imported')
#
#     sf_buyer_notes_c = fields.Text('Buyer_Notes__c')


class SalesforceUserId(models.Model):
    _inherit = 'res.users'
    salesforce_user_id = fields.Char('Salesforce User Id')

class SalesforceTasks(models.Model):
    _name = 'salesforce.tasks'
    _description = 'Model for storing salesforce tasks fields'
    _rec_name = 'Subject'

    sf_id = fields.Char(string="SalesForce Task Id", index=True)

    active = fields.Boolean(default=True)
    sf_salesperson_id = fields.Char('Assigned To')

    user_id = fields.Many2one('res.users')
    CallDurationInSeconds = fields.Integer('Call Duration')
    CallObject = fields.Char('Call Object Identifier')
    CallDisposition = fields.Char('Call Result')
    CallType = fields.Char('Call Type')
    Description = fields.Text('Comments')
    sf_created_by_id = fields.Char('Salesforce Created By')
    sf_last_modified_by_id = fields.Char('Salesforce LastModified By')
    IsRecurrence = fields.Boolean('Create Recurring Series of Tasks')
    ActivityDate = fields.Date('Activity due date')
    CompletedDateTime = fields.Datetime('Task Complete date time')
    Email = fields.Char('Email')
    Name = fields.Char('Who (Lead or contact)')
    who_Type = fields.Selection([('Lead', 'Lead'), ('Contact', 'Contact')], string='Who Type')
    Phone = fields.Char('Phone')
    Priority = fields.Char('Priority')
    RecurrenceInterval = fields.Integer('Recurrence Interval')
    What = fields.Char('Related to ID')
    what_Type = fields.Char('Related to')
    IsReminderSet = fields.Boolean('Is reminder set')
    RecurrenceRegeneratedType = fields.Char('Repeat This Task')
    Status = fields.Char('status')
    Subject = fields.Char('Subject')
    TaskSubtype = fields.Char('task subtype')
    Type = fields.Many2one('salesforce.task.types',string='Task Type')

    sf_created_date = fields.Datetime('Task Create time')

    # task to activity status
    is_converted = fields.Boolean('Is task Converted', default=False)
    activity_message_id = fields.Many2one('mail.message', ondelete='set null')
    activity_id = fields.Many2one('mail.activity', ondelete='set null')
    conversion_status = fields.Char('Conversion Status')

    related_opportunity = fields.Many2one('crm.lead', string='Related Opportunity Record',
                                          compute='compute_related_opportunity', default=False)
    related_account = fields.Many2one('res.partner', string='Related Account Record',
                                          compute='compute_related_account', default=False)

    def compute_related_opportunity(self):
        for rec in self:
            if not rec.What:
                rec.related_opportunity = False
                continue
            related_rec = self.env['crm.lead'].search([('sf_id','=',rec.What),('type','=','opportunity')], limit=1)
            if related_rec:
                rec.related_opportunity = related_rec.id
            else:
                rec.related_opportunity = False

    def compute_related_account(self):
        for rec in self:
            if not rec.What:
                rec.related_account = False
                continue
            related_rec = self.env['res.partner'].search([('sf_account_id','=',rec.What)], limit=1)
            if related_rec:
                rec.related_account = related_rec.id
            else:
                rec.related_account = False

    def convert_tasks_on_form_action(self):
        cron_record = self.env.ref('salesforce_connector.sf_tasks_conversion_process_1')
        if cron_record and self.ids:
            next_exc_time = datetime.now() + timedelta(milliseconds=5)
            cron_record.write({'nextcall': next_exc_time})
            code_to_run = f"model.convert_salesforce_tasks_to_activities(records={[self.ids]})"
            cron_record.write({'code': code_to_run})

        # self.env['sf.sync.data'].convert_salesforce_tasks_to_activities(self.ids)

class SalesforceTaskTypes(models.Model):
    _name = 'salesforce.task.types'
    _description = 'Salesforce Task types'
    name = fields.Char('Task Type Name')

class MailActivityForSalesforce(models.Model):
    _inherit = 'mail.activity'

    salesforce_id = fields.Char('Salesforce ID')
    imported_task_id = fields.Many2one('salesforce.tasks',string='Imported Salesforce Task', ondelete='set null')
    call_direction = fields.Selection([('inbound','inbound'),('outbound','outbound'),('transfer','transfer')],
                                      string='Call Direction')
    call_result = fields.Selection([('Gatekeeper','Gatekeeper'),('Reached Buyer','Reached Buyer'),
                                    ('Reached Decision Maker','Reached Decision Maker'),
                                    ('DNC','DNC'),('Wrong Number','Wrong Number')], string='Call Result')
    call_disposition = fields.Selection([('Answered','Answered'),('No Answer','No Answer'),('Left VM','Left VM'),
                                         ('Busy','Busy'),('Inactive/Disconnected Number','Inactive/Disconnected Number')],
                                      string='Call Disposition')
    is_activity_call_type = fields.Boolean('Call Type Activity',compute='compute_if_call_type_activity',
                                           default=False, store=True)
    activity_reason = fields.Selection([('Customer Onboarding - NDA','Customer Onboarding - NDA'),
                                        ('Customer Onboarding - Terms and Conditions', 'Customer Onboarding - Terms and Conditions'),
                                        ('Customer Onboarding - New Customer Info Sheet', 'Customer Onboarding - New Customer Info Sheet'),
                                        ('Customer Loyalty Program','Customer Loyalty Program'),
                                        ('Accounting','Accounting'),('Quality','Quality'),
                                        ('Quote - Follow-up','Quote - Follow-up'),
                                        ('Quote - Delivery','Quote - Delivery'),
                                        ('RFQ','RFQ'),('PO','PO'),('Shipping / Receiving','Shipping / Receiving'),
                                        ('Account Management','Account Management'),('Growth','Growth'),
                                        ('Engineering','Manufacturing')], string='Reason')

    @api.depends('activity_type_id')
    def compute_if_call_type_activity(self):
        for rec in self:
            if rec.activity_type_id.id == self.env.ref('mail.mail_activity_data_call').id:
                rec.is_activity_call_type = True
            else:
                rec.is_activity_call_type = False

class MailMessageForSalesforce(models.Model):
    _inherit = 'mail.message'

    imported_task_id = fields.Many2one('salesforce.tasks', string='Imported Salesforce Task ID', ondelete='set null')
