from odoo import models, fields, api


class ModelQuote(models.Model):
    _name = 'model_quote'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Salesforce Quote'
    _rec_name = 'Name'

    AccountId = fields.Many2one('account.account', string="Account Name",track_visibility='onchange')
    account_owner = fields.Char(string="Account Owner",track_visibility='onchange')
    AdditionalAddress = fields.Text(string="Additional To",track_visibility='onchange')
    AdditionalName = fields.Char(string="Additional To Name", size=255,track_visibility='onchange')
    admin_proposal = fields.Char(string="Admin Proposal", size=20,track_visibility='onchange')
    admin_proposal_date = fields.Datetime(string="Admin Proposal Date",track_visibility='onchange')
    BillingAddress = fields.Text(string="Bill To",track_visibility='onchange')
    BillingName = fields.Char(string="Bill To Name", size=255,track_visibility='onchange')
    carrier = fields.Char(string="Carrier",track_visibility='onchange')
    Case =  fields.Many2one('model_case',string="Case",track_visibility='onchange')
    cc_email = fields.Char(string="CC Email",track_visibility='onchange')
    CNPJ = fields.Char(string="CNPJ", size=18,track_visibility='onchange')
    ContactId = fields.Many2one('res.partner',string="Contact Name",track_visibility='onchange')
    ContractId = fields.Many2one('hr.contract', string="Contract",track_visibility='onchange')
    cpf = fields.Char(string="CPF", size=14,track_visibility='onchange')
    # CreatedById already in odoo
    creation_date = fields.Date('Creation Date',track_visibility='onchange')
    status_change_date = fields.Date(string="Status Change Date",track_visibility='onchange')
    Description = fields.Text(string="Description",track_visibility='onchange')
    days_in_current_status = fields.Char(string="Days in Current Status",track_visibility='onchange')
    Discount = fields.Float(string="Discount",track_visibility='onchange')
    Email = fields.Char(string="Email",track_visibility='onchange')
    email_from = fields.Char(string="email_from",track_visibility='onchange')
    send_email = fields.Boolean(string="Send email",track_visibility='onchange')
    estimated_revenue = fields.Char(string="Estimated Revenue",track_visibility='onchange')
    ExpirationDate = fields.Date(string="Expiration Date",track_visibility='onchange')
    External_Id = fields.Char(string="External Id", size=255,track_visibility='onchange')
    Fax = fields.Char(string="Fax",track_visibility='onchange')
    first_quote = fields.Boolean(string="First quote",track_visibility='onchange')
    GrandTotal = fields.Float(string="Grand Total",track_visibility='onchange')
    # LastModifiedById already in odoo
    lead_source =  fields.Char(string="Lead Source",track_visibility='onchange')
    # LineItemCount #RollUP Summery
    made_by =  fields.Selection([
        ('self-service_sincare','Sincare self-service'),
        ('consultant_thinkcare','Thinkcare consultant')
    ],string="Made By",track_visibility='onchange')
    Mailing_Font =  fields.Char(string="Mailing Font",track_visibility='onchange')
    Motive_Of_Gain =  fields.Selection([
        ('Expertise','Expertise'),
        ('Claim Management','Claim Management'),
        ('Innovation','Innovation'),
        ('Price','Price'),
        ('Relationship','Relationship'),
        ('Service','Service'),
        ('Offered Solution','Offered Solution')
    ],string="Reason for gain",track_visibility='onchange')
    Loss_Reason = fields.Selection([
        ('High risk','High risk'),
        ('contractual mooring','contractual mooring'),
        ('Flexible benefit','Flexible benefit'),
        ('Broker mundial','Broker mundial'),
        ('Converted','Converted'),
        ('relationship broker','relationship broker'),
        ('Expertise','Expertise'),
        ('Closed by PF','Closed by PF'),
        ('Dated PJ hair','Dated PJ hair'),
        ('Claim Management','Claim Management'),
        ('Innovation','Innovation'),
        ('Lost to Competitor','Lost to Competitor'),
        ('No Budget / Lost Funding','No Budget / Lost Funding'),
        ('No Decision / Non-Responsive','No Decision / Non-Responsive'),
        ('Other','Other'),
        ('Market research','Market research'),
        ('expired term','expired term'),
        ('Price','Price'),
        ('Network','Network'),
        ('Relationship','Relationship'),
        ('Service','Service'),
        ('Solution offered','Solution offered')
    ],string="Reason for loss",track_visibility='onchange')
    contact_name = fields.Char(string="Contact's full name",track_visibility='onchange')
    opportunity_current_user = fields.Boolean(string="Opportunity Current User",track_visibility='onchange')
    OpportunityId = fields.Many2one('crm.lead', string="Opportunity Name",track_visibility='onchange')
    opportunity_owner = fields.Char(string="Opportunity Owner",track_visibility='onchange')
    Original_Quote_Number = fields.Char(string="Original Quote Number", size=255,track_visibility='onchange')
    owner_current_user = fields.Boolean(string="Owner Current User",track_visibility='onchange')
    OwnerId = fields.Many2one('res.users', string="Owner Name",track_visibility='onchange')
    phone_c = fields.Char(string="Phone",track_visibility='onchange')
    phone =  fields.Char(string="Phone",track_visibility='onchange')
    proposal_number = fields.Char(string="Proposal Number", size=20,track_visibility='onchange')
    Quotation_Reason = fields.Selection([
        ('Network Improvement','Network Improvement'),
        ('Plan Redesign','Plan Redesign')
    ],string="Quotation Reason",track_visibility='onchange')
    Name = fields.Char(string="Quote Name", size=255, track_visibility='onchange', required=True)
    QuoteNumber = fields.Char(string="Quote Number",track_visibility='onchange')
    RecordTypeId =fields.Char(string="Quote Record Type",track_visibility='onchange')
    QuoteToAddress = fields.Text(string="Quote To",track_visibility='onchange')
    QuoteToName = fields.Char(string="Quote To Name", size=255,track_visibility='onchange')
    quote_type__c = fields.Selection([
        ('Price','Price'),('Benchmarking','Benchmarking')
    ],string="Quote Type",track_visibility='onchange')
    quote_won =  fields.Char(string="Quote Won", size=255,track_visibility='onchange')
    repique = fields.Boolean(string="Repique",track_visibility='onchange')
    request_date = fields.Date(string="Request Date",track_visibility='onchange')
    returned_reason =  fields.Char(string="Returned Reason", size=255,track_visibility='onchange')
    ShippingAddress = fields.Text(string="Ship To",track_visibility='onchange')
    ShippingName =  fields.Char(string="Ship To Name", size=255)
    ShippingHandling = fields.Float(string="Shipping and Handling")
    Quote__c = fields.Char(string="Study request")
    parent_quote_id = fields.Many2one('model_quote', string="Parent Study Request" )
    Status = fields.Selection([
        ('Draft','In filling'),
        ('Needs Review','Open'),
        ('Under Proposal Analysis','Under Proposal Analysis'),
        ('Pending Information','Pending Information'),
        ('Sent to Operator','Sent to Operator'),
        ('Rejected','Declined'),
        ('In Review','In Validation'),
        ('Accepted','Accomplished'),
        ('Presented','Introduced'),
        ('tnk_quote','tnk_quote'),
        ('In negociation','In negociation'),
        ('Devolution','Devolution'),
        ('released_for_deployment','Released for Deployment'),
        ('awaiting_documentation','Awaiting Documentation'),
        ('admin_propose','Management Proposal'),
        ('admin_deploy','In Admin Deployment'),
        ('critcims','Review'),
        ('Lost','Lost'),
        ('win','win')
    ],string="Status")
    study_configuration_id = fields.Many2one('study_configuration', string="Study Configuration")
    # Subtotal =
    IsSyncing = fields.Boolean(string="Syncing")
    Tax = fields.Float(string="Tax")
    total_lives =  fields.Float(string="Total Vidas")
    # TotalPrice
    verified_partnership = fields.Char(string="Verified Partnership", size=100)
    last_quote = fields.Boolean(string="Last quote")
    attachment_ids = fields.One2many('ir.attachment', 'quote_id', string="Attachment IDS")

    opportunity_ids = fields.One2many('crm.lead','opportunity_quote_id',string='Opportunity')
    case_ids = fields.One2many('model_case','case_quote_id', string='Case')
    quote_product_ids = fields.One2many('model_quote_products', 'quote_product_id', string='Quotation Product')
    additional_parameter_ids = fields.One2many('model_additional_parameter', 'quote_id', string='Additional Parameter')
    quote_ids = fields.One2many('model_quote', 'parent_quote_id', string='Quotes')



    # @api.model
    # def create(self, vals):
    #     if vals['OpportunityId']:
    #         get_quotes_for_same_opportunity = self.env['model_quote'].sudo().search([('OpportunityId','=',vals['OpportunityId'])])
    #         if not get_quotes_for_same_opportunity:
    #             vals['first_quote'] = True
    #     record = super(ModelQuote, self).create(vals)
    #     return record










