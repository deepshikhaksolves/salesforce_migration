from odoo import models, fields, api



class Case(models.Model):
    _name = 'model_case'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Case"
    _rec_name = 'attendee_name'

    # CreatedById  already in odoo
    # LastModifiedById already in odoo

    AccountId = fields.Many2one('account.account',string='Account Name')
    #AssetId = fields.Many2one('asset',string='Asset')
    #AssetId is related to asset object which is not define
    #Subject_Request_id = fields.Many2one('model_subject_request',string='Subject_Request')
    #Subject_Request_id is related to subject request object which is not define

    attendee_name = fields.Char(string='Attended',size=200)
    attendee_by_id = fields.Many2one('res.partner',string='attendee by')
    Form_Attendee = fields.Text(string='Attendee Formula')
    Attendee_id = fields.Many2one('model_publico',string='Attendee Public')
    beneficiary_id = fields.Float(string='Beneficiary Id',digits=(15,0))
    benefit = fields.Text(string='Benefit')
    #BusinessHoursId = fields.Many2one('model_business_hours',string='Business Hours')
    #BusinessHoursId is related to model_business_hours object which is not define
    Cancelation_Reason = fields.Selection([('Duplicity','Duplicity'),
                                           ('Incorrect','Incorrect'),
                                           ('Test','Test')],string='Cancelation Reason')
    CaseNumber = fields.Char(string='Case Number')
    Origin =  fields.Selection([('Email','Email'),('I_Protected','I_Protected'),('Folks','Folks'),
                                ('Rh_Protected','Rh_Protected'),('System','System'),('Web','Web'),
                                ('Phone','Phone'),('Whats App','Whats App'),('Dr_Protected','Dr_Protected')],
                               string='Case Origin')
    OwnerId = fields.Many2one('res.users',string='Case Owner')
    Reason =  fields.Selection([('Change Access','Change Access'),('Block','Block'),('Settings','Settings'),
                                ('Existing Problem','Existing Problem'),('Installation','Installation'),
                                ('New Access','New Access'),('Problems In General','Problems In General'),
                                ('Instructions Not Clear','Instructions Not Clear'),('Technical Surplus','Technical Surplus'),
                                ('Result','Result')],string='Case Reason')
    RecordTypeId = fields.Char(string='Case Record Type')
    SourceId = fields.Char(string='Case Source')

    checklist = fields.Boolean(string='Checklist')
    Classification = fields.Selection([('Information','Information'),('Request','Request'),
                                       ('Complaint','Complaint')],string='Classification')
    Classified = fields.Boolean(string='Classified')
    client_view_permission = fields.Selection([('Dr_Protected','Dr_Protected'),('Rh_Protected','Rh_Protected'),
                                               ('I_Protected','I_Protected')],string='Client View Permission')
    IsClosedOnCreate = fields.Boolean(string='Closed When Created')
    contact_current_user = fields.Boolean(string='Contact Current User')
    Contact = fields.Char(string='Contact Email')
    ContactFax = fields.Char(string='Contact Fax')
    ContactMobile = fields.Char(string='Contact Mobile')
    ContactId = fields.Many2one('res.partner',string='Contact Name')
    ContactPhone = fields.Char(string='Contact Phone')
    Contract_New = fields.Char(string='Contract New',size=255)
    #Contract_Readjustment_id = fields.Many2one('model_adjustment_of_the_contract',string='Contract Readjustment')
    # Contract_Readjustment_id is related to model_adjustment_of_the_contract object which is not define
    Contract_id = fields.Many2one('hr.contract',string='Contract')


    created_current_user = fields.Boolean(string='Created Current User')
    regularization_date = fields.Date(string='Regularization Date')
    ClosedDate = fields.Datetime(string='Date/Time Closed')
    CreatedDate = fields.Datetime(string='Date/Time Opened')
    Description = fields.Text(string='Description')
    Emails = fields.Text(string='E-mails')
    EngineeringReqNumber = fields.Char(string='Engineering Req Number',size=12)
    #EntitlementId = fields.Many2one('model_Entitlement',string='Entitlement Name')
    # EntitlementId is related to model_Entitlement object which is not define
    SlaExitDate = fields.Datetime(string='Entitlement Process End Time')
    SlaStartDate = fields.Datetime(string='Entitlement Process Start Time')
    IsEscalated = fields.Boolean(string='Escalated')
    executive_manager_id = fields.Many2one('res.users',string='Executive Manager')
    Final_Email_Sent = fields.Boolean(string='Final Email Sent')
    Hour_Register = fields.Float(string='Hour Register',digits=(3,2))
    Comments = fields.Text(string='Internal Comments')
    effective_date = fields.Date(string='Beginning of term')
    Language = fields.Selection([('A','A'),('B','B'),('C','C')],string='Language')
    Last_Comment = fields.Text(string='Last Comment')
    document_list = fields.Text(string='Documents list')
    MilestoneStatus = fields.Char(string='Milestone Status',size=30)
    Service_Model_id = fields.Many2one('model_service_c',string='Service Model')
    Carrier = fields.Text(string='Operator')
    opportunity_id = fields.Many2one('crm.lead',string='Opportunity')
    ParentId = fields.Many2one('model_case',string='Parent Case')
    PotentialLiability = fields.Selection([('No','No'),('Yes','Yes')],string='Potential Liability')
    Priority = fields.Selection([('High','High'),('Medium','Medium'),('Low','Low')],string='Priority')
    ProductId = fields.Many2one('product.template',string='Product')
    Nested_Case_Number = fields.Text(string='Protocol')
    Public_id = fields.Many2one('model_publico',string='Public')
    Public_Description = fields.Text(string='Publico Description')
    quote_id = fields.Many2one('model_quote',string='Quote')
    Readjustment_Placement_End = fields.Boolean(string='Readjustment Placement End')
    relationship_director_id = fields.Many2one('res.users',string='Relationship Director')
    relationship_manager_id = fields.Many2one('res.users',string='Relationship Manager')
    Reopening = fields.Boolean(string='Reopening')
    Request = fields.Selection([('Opening of Plan','Opening of Plan'),('Sub Opening','Sub Opening'),
                                ('Deployment Agreement','Deployment Agreement'),('Customer Actions','Customer Actions'),
                                ('Health Actions','Health Actions'),('Additions','Additions'),
                                ('Scheduling','Scheduling'),('Change','Change'),('Invoice Anticipation','Invoice Anticipation'),
                                ('Accounting File','Accounting File'),('Apportionment File','Apportionment File'),
                                ('Claim Notice to the Customer','Claim Notice to the Customer'),('Basis for Billing','Basis for Billing'),
                                ('Registration Certificate','Registration Certificate'),('Block','Block'),('Ticket','Ticket'),
                                ('Adhesion Campaign','Adhesion Campaign'),('Cancellation','Cancellation'),('Stipulator Cancellation','Stipulator Cancellation'),
                                ('Substipulator Cancellation','Substipulator Cancellation'),('Surgeries','Surgeries'),
                                ('Health Committee','Health Committee'),('Equipment Purchases','Equipment Purchases'),
                                ('Communication of the Claim to the Insurer','Communication of the Claim to the Insurer'),
                                ('Settings','Settings'),('Query','Query'),('Contact Customer','Contact Customer'),
                                ('Contact Internal Team','Contact Internal Team'),('Contact Operator','Contact Operator'),
                                ('Contract','Contract'),('File Conversion','File Conversion'),('Co-participation','Co-participation'),
                                ('Disaccreditation','Disaccreditation'),('Hospital expenses','Hospital expenses'),
                                ('Refund Return','Refund Return'),('Documentation','Documentation'),
                                ('Coverage Doubt','Coverage Doubt'),('Questions / Changes','Questions / Changes'),
                                ('Issuance of Declaration of Permanence','Issuance of Declaration of Permanence'),
                                ('Voucher Issuance','Voucher Issuance'),('Card delivery','Card delivery'),
                                ('Report submission','Report submission'),('Market research','Market research'),
                                ('Exams','Exams'),('Technical surplus','Technical surplus'),('Extension','Extension'),
                                ('Co-participation Statement','Co-participation Statement'),('Technical Invoice','Technical Invoice'),
                                ('Inclusion','Inclusion'),('Inclusion of Dismissed / Retired','Inclusion of Dismissed / Retired'),
                                ('Inclusion of Redeemed','Inclusion of Redeemed'),('Out of Date Inclusion','Out of Date Inclusion'),
                                ('Accreditation Indication','Accreditation Indication'),('Information','Information'),
                                ('Refund Information','Refund Information'),('Installation','Installation'),
                                ('Waiver Waiver','Waiver Waiver'),('Release of Procedures','Release of Procedures'),
                                ('injunction','injunction'),('Medicines','Medicines'),('Not Receiving the Card','Not Receiving the Card'),
                                ('Denial of Procedures','Denial of Procedures'),('Readjustment negotiation','Readjustment negotiation'),
                                ('New','New'),('Card number','Card number'),('dental','dental'),('Release Guidelines','Release Guidelines'),
                                ('Others','Others'),('Market Panel','Market Panel'),('Implementation Lecture','Implementation Lecture'),
                                ('Request','Request'),('Pending Release','Pending Release'),('Refund Prior','Refund Prior'),
                                ('Problem','Problem'),('Membership Proposal','Membership Proposal'),('Technical Invoice Extension','Technical Invoice Extension'),
                                ('Readjustment','Readjustment'),('Reactivation','Reactivation'),('Accredited network','Accredited network'),
                                ('Late Refund','Late Refund'),('Reimbursement Review','Reimbursement Review'),('Refilling','Refilling'),
                                ('Renovation','Renovation'),('Result','Result'),('Second copy','Second copy'),('SIPAT','SIPAT'),
                                ('Request','Request'),('Therapies','Therapies'),('Documentation Screening','Documentation Screening'),
                                ('Vaccines','Vaccines'),('Passwords Released','Passwords Released'),('Denied passwords','Denied passwords')],
                               string='Request')
    #ServiceContractId = fields.Many2one('model_service_contract',string='Service Contract')
    # ServiceContractId is related to model_service_contract object which is not define

    SLAViolation = fields.Selection([('No','No'),('Yes','Yes')],string='SLA Violation')
    Requestor_id = fields.Many2one('model_publico',string='Applicant')
    Request_old_id = fields.Many2one('model_request',string='old request')
    Stage = fields.Selection([('waiting for documents','waiting for documents'),('Document Analysis','Document Analysis'),
                              ('Layout/Review/Waiting for Documentation','Layout/Review/Waiting for Documentation'),
                              ('Shipping to Operator','Shipping to Operator'),('Operator Review','Operator Review')],
                             string='Stage')
    Status = fields.Selection([('Open','Open'),('New','New'),('classified','classified'),('Alert','Alert Sent'),
                               ('On Hold','In progress'),('Awaiting Customer Return','Awaiting Customer Return'),
                               ('Negotiation','Negotiation'),('Released for Deployment','Released for Deployment'),
                               ('Checklist + Welcome','Checklist + Welcome'),('Awaiting Documentation','Awaiting Documentation'),
                               ('Document Analysis','Document Analysis'),('Review/Awaiting Documentation','Review/Awaiting Documentation'),
                               ('Shipping to Operator','Shipping to Operator'),('Operator Review','Operator Review'),
                               ('Implemented in the Operator','Implemented in the Operator'),('Contract Activation','Contract Activation'),
                               ('Released for Service','Released for Service'),('In Customer Review','In Customer Review'),
                               ('Under Operator Analysis','Under Operator Analysis'),('In Internal Analysis','In Internal Analysis'),
                               ('In Return Analysis','In Return Analysis'),('Closed','Closed'),('Called off','Called off')],
                              string='Status')
    IsStopped = fields.Boolean(string='Stopped')
    StopStartDate = fields.Datetime(string='Stopped Since')
    Subject = fields.Char(string="Subject", size=255)
    Subject_old_id = fields.Many2one('model_subject_c',string='Subject old')
    Support_Placement = fields.Boolean(string='Support Placement')
    Type = fields.Selection([('Access','Access'),('Telephony','Cellphone'),('Computer/Notebook','Computer/Notebook'),
                             ('Printer','Printer'),('Network/Internet','Network/Internet'),('Software','Software'),
                             ('Servers','Servers'),('Readjustment','Readjustment'),('Readjustment Kit','Readjustment Kit'),
                             ('advances','advances'),('Policy Calculation','Policy Calculation'),('Travel Assistance','Travel Assistance'),
                             ('Audit','Audit'),('Authorizations','Authorizations'),('Registration Certificate','Registration Certificate'),
                             ('Cards','Cards'),('Checkup','Checkup'),('Concessions','Concessions'),('Contract','Contract'),
                             ('Co-participation','Co-participation'),('Revenues','Revenues'),('health management','health management'),
                             ('Implantation','Implantation'),('Post Refund','Post Refund'),('Cadastral Movement','Cadastral Movement'),
                             ('PAT','PAT'),('Projects','Projects'),('Quality of life','Quality of life'),('Accredited network','Accredited network'),
                             ('Reimbursement','Reimbursement'),('Management report','Management report'),('Management report','Management report'),
                             ('Sinister','Sinister'),('Purchases','Purchases'),('Other Doubts','Other Doubts'),
                             ('Protected HR Technical Support','Protected HR Technical Support'),('helpdesk_me','helpdesk_me'),
                             ('Negative','Negative')], string='Type')
    Visible_to_the_Customer = fields.Boolean(string='Visible to the Customer')
    SuppliedCompany = fields.Char(string='Web Company',size=80)
    SuppliedEmail = fields.Char(string='Web Email')
    SuppliedName = fields.Char(string='Web Name',size=80)
    SuppliedPhone = fields.Char(string='Web Phone',size=40)
    attachment_ids = fields.One2many('ir.attachment','case_id',string="Attachment")
    partner_id = fields.Many2one('res.partner', string='partner Name')



class AttachmentInherit(models.Model):
    _inherit = 'ir.attachment'

    case_id = fields.Many2one('model_case',string="Case Id")




