from odoo import models, fields, api


class Quote(models.Model):
    _name = 'model_quote'
    _description = 'Salesforce Quote'
    _rec_name = 'Name'

    AccountId = fields.Many2one('account.account', string="Account Name")
    account_owner = fields.Char(string="Account Owner")
    AdditionalAddress = fields.Text(string="Additional To")
    AdditionalName = fields.Char(string="Additional To Name", size=255)
    admin_proposal = fields.Char(string="Admin Proposal", size=20)
    admin_proposal_date = fields.Datetime(string="Admin Proposal Date")
    BillingAddress = fields.Text(string="Bill To")
    BillingName = fields.Char(string="Bill To Name", size=255)
    carrier = fields.Char(string="Carrier")
    # Case =  fields.Many2one('case',string="Case") Model Not found
    cc_email = fields.Char(string="CC Email")
    CNPJ = fields.Char(string="CNPJ")
    ContactId = fields.Many2one('res.partner',string="Contact Name")
    ContractId = fields.Many2one('hr.contract', string="Contract")
    cpf = fields.Char(string="CPF", size=14)
    # CreatedById already in odoo
    # creation_date already in odoo
    status_change_date = fields.Date(string="Status Change Date")
    Description = fields.Text(string="Description")
    days_in_current_status = fields.Char(string="Days in Current Status")
    Discount = fields.Float(string="Discount", digits=(3, 2))
    Email = fields.Char(string="Email")
    email_from = fields.Char(string="email_from")
    send_email = fields.Boolean(string="Send email")
    estimated_revenue = fields.Char(string="Estimated Revenue")
    ExpirationDate = fields.Date(string="Expiration Date")
    External_Id = fields.Char(string="External Id", size=255)
    Fax = fields.Char(string="Fax")
    first_quote = fields.Boolean(string="First quote")
    GrandTotal = fields.Float(string="Grand Total", digits=(16, 2))
    # LastModifiedById already in odoo
    lead_source =  fields.Char(string="Lead Source")
    # LineItemCount #RollUP Summery
    made_by =  fields.Selection([
        ('self-service_sincare','Sincare self-service'),
        ('consultant_thinkcare','Thinkcare consultant')
    ],string="Made By")
    Mailing_Font =  fields.Char(string="Mailing Font")
    Motive_Of_Gain =  fields.Selection([
        ('Expertise','Expertise'),
        ('Claim Management','Claim Management'),
        ('Innovation','Innovation'),
        ('Price','Price'),
        ('Relationship','Relationship'),
        ('Service','Service'),
        ('Offered Solution','Offered Solution')
    ],string="Reason for gain")
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
    ],string="Reason for loss")
    contact_name = fields.Char(string="Contact's full name"),
    opportunity_current_user = fields.Boolean(string="Opportunity Current User")
    OpportunityId = fields.Many2one('crm.lead', string="Opportunity Name")
    opportunity_owner = fields.Char(string="Opportunity Owner")
    Original_Quote_Number = fields.Char(string="Original Quote Number", size=255)
    owner_current_user = fields.Boolean(string="Owner Current User")
    OwnerId = fields.Many2one('res.users', string="Owner Name")
    phone_c = fields.Char(string="Phone")
    phone =  fields.Char(string="Phone")
    proposal_number = fields.Char(string="Proposal Number", size=20)
    Quotation_Reason = fields.Selection([
        ('Network Improvement','Network Improvement'),
        ('Plan Redesign','Plan Redesign')
    ],string="Quotation Reason")
    Name = fields.Char(string="Quote Name", size=255)
    QuoteNumber = fields.Char(string="Quote Number")
    RecordTypeId =fields.Char(string="Quote Record Type")
    QuoteToAddress = fields.Text(string="Quote To")
    QuoteToName = fields.Char(string="Quote To Name", size=255)
    quote_type__c = fields.Selection([
        ('Price','Price'),('Benchmarking','Benchmarking')
    ],string="Quote Type")
    quote_won =  fields.Char(string="Quote Won", size=255)
    repique = fields.Boolean(string="Repique")
    request_date = fields.Date(string="Request Date")
    returned_reason =  fields.Char(string="Returned Reason", size=255)
    ShippingAddress = fields.Text(string="Ship To")
    ShippingName =  fields.Char(string="Ship To Name", size=255)
    ShippingHandling = fields.Float(string="Shipping and Handling", digits=(16, 2))
    Quote__c = fields.Char(string="Study request")
    # parent_quote_id = fields.Many2one('')
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
    Tax = fields.Float(string="Tax",digits=(16, 2))
    total_lives =  fields.Float(string="Total VIdas", digits=(10, 0))
    # TotalPrice
    verified_partnership = fields.Char(string="Verified Partnership", size=100)
    last_quote = fields.Boolean(string="Last quote")

    _sql_constraints = [
        ('check_external_id_uniq', 'unique (External_ID)', "External ID Should be unique!!"),
    ]



