from odoo import models, fields, api


class RecordType(models.Model):
    _name = 'record_type'
    _description = "Salesforce Record Type"
    _rec_name = 'name'

    name  = fields.Char('Name')


class TypeOfOperator(models.Model):
    _name = 'type_of_operator'
    _description = "Salesforce Operator"
    _rec_name = 'name'

    name  = fields.Char('Name')


class Account(models.Model):
    _name = 'account.account'
    _inherit = ['account.account', 'mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Account"

    ABC_Analysis__pc    = fields.Selection([('B', 'B'),('B', 'B'),('C', 'C')],'ABC Analysis')
    Account__c          = fields.Many2one('account.account',string='Account')
    # Name                = fields.Char('Account Name')
    AccountNumber       = fields.Char('Account Number',size=40)
    OwnerId             = fields.Many2one('res.users',string='Account Owner')
    RecordTypeId        = fields.Many2one('record_type',string='Record Type')
    Site                = fields.Char('Account Site',size=80)
    AccountSource       = fields.Selection([('Quotator', 'Quotator'),('Customer Event', 'Customer Event'),('Exposure', 'Exposure'),('Google AdWords', 'Google AdWords'),('Employee Indication', 'Employee Indication'),('Mailing', 'Mailing'),('Partner', 'Partner'),('Advertising', 'Advertising'),('Site', 'Site'),('Webinar', 'Webinar'),('Others', 'Others')],'Account Source')
    Active__c           = fields.Selection([('No', 'Not'),('Yes', 'Yes')],'Active')

    allow_create_accredited_net_case__c = fields.Boolean(string="Allow Create Accredited Net Case")
    allow_create_reimbursement_case__c = fields.Boolean(string="Allow Create Reimbursement Case")
    allow_direct_mail__pc = fields.Boolean(string="Allow Direct Mail")
    # AnnualRevenue         = fields.Many2one('res.currency', string='Annual Revenue', default=lambda self: self.env.user.company_id.currency_id.id)
    AnnualRevenue       = fields.Float('Annual Revenue', digits=(18, 0))

    ans_start__c        = fields.Date('YEARS Start')
    ans_code__c         = fields.Float('ANS / SUSEP Code', digits=(10, 0))
    app_address__c      = fields.Char('App Address',size=255)
    PersonAssistantName = fields.Char('Assistant',size=40)
    assistant_email__pc = fields.Char('Assistant E-mail')
    assistant_extension_number__pc  = fields.Float('Assistant Extension Number', digits=(10, 0))
    assistant_mobile_phone__pc  = fields.Char('Assistant Mobile Phone')
    PersonAssistantPhon = fields.Char('Asst. Phone')
    Active__pc          = fields.Boolean('Active')
    benefits__c         = fields.Selection([('Health', 'Health'),('Dental', 'Dental'),('Life', 'Life'),('Medicine', 'medicine'),('Personal_Accidents', 'Personal Accident'),('In_Company', 'Consultancy'),('Medical_Consulting', 'Medical Consulting'),('Meal', 'Snack'),('Food', 'food'),('Transportation', 'Transport'),('Pension', 'pension'),('Travel', 'Travel'),('Car_Fleet', 'Frota'),('Car', 'Car'),('Fuel', 'Fuel'),('Occupational_Health', 'occupational health'),('Checkup', 'Check-up'),('Vaccine', 'Vaccine'),('I_protected', 'I Protected'),('Fee', 'Fee')],'Benefits')

    BillingAddress      = fields.Text('Billing Address')
    PersonBirthdate     = fields.Date('Birthdate')
    Broker__c           = fields.Many2one('res.partner',string='Broker')
    broker_call_center__c = fields.Char('Broker Call Center')
    Social_Reason__c	= fields.Char('Business Name',size=255)
    card_image__c       = fields.Char('Card Image',size=32768)
    card_template__c    = fields.Char('Card Template',size=32768)
    carrier_type__c     = fields.Many2one('type_of_operator',string='Carrier Type')
    nationalh_health_card__pc = fields.Char('National Health Card',size=50)
    ChannelProgramLevelName   = fields.Char('Channel Program Level Name',size=255)
    ChannelProgramName  = fields.Char('Channel Program Name',size=255)
    cid__pc             = fields.Char('CID',size=100)
    CNAE__c             = fields.Many2one('model_cnae',string='NINE')
    CNPJ__c             = fields.Char('CNPJ',size=18)
    CNS__c              = fields.Integer('CNS')
    comercial_name__c   = fields.Char('Comercial Name',size=255)
    Company_Segmentation__c = fields.Selection([('Small', 'Revenue'),('Small_Large', 'Revenue between 40k and 100k'),('Middle', 'Revenue between 100k and 250k'),('Middle_Large', 'Revenue between 250k and 400k'),('Corporate', 'Revenue between 400k and 1MM'),('Corporate_Large', 'Revenue >1MM')],'Company Segmentation')

    Company_Classification__c = fields.Selection([('Small', 'Recipe <40k'),('Small_Large', 'Revenue between 40k and 100k'),('Middle', 'Revenue between 100k and 250k'),('Middle_Large', 'Revenue between 250k and 400k'),('Corporate', 'Revenue between 400k and 1MM'),('Corporate_Large', 'Revenue >1MM')],'Company_Classification')

    council_state__c     = fields.Selection([('AC', 'AC'),('AL', 'AL'),('AM', 'AM'),('AP', 'AP'),('BA', 'BA'),('CE', 'CE'),('DF', 'DF'),('ES', 'ES'),('GO', 'GO'),('MA', 'MA'),('MG', 'MG'),('MS', 'MS'),('MT', 'MT'),('PA', 'PA'),('PB', 'PB'),('PE', 'PE'),('PI', 'PI'),('PR', 'PR'),('RJ', 'RJ'),('RN', 'RN'),('RO', 'RO'),('RR', 'RR'),('RR', 'RR'),('RS', 'RS'),('SC', 'SC'),('SE', 'SE'),('SP', 'SP'),('TO', 'TO')],'Council State')

    CPF__c      = fields.Char('CPF',size=14)
    cpf__pc     = fields.Char('CPF',size=14)
    # CreatedById already in odoo
    IsCustomerPortal            = fields.Selection([('1','1'),('2','2')],'Customer Portal Account')
    CustomerPriority__c         = fields.Selection([('High', 'High'),('Low', 'Low'),('Medium', 'Medium')],'Customer Priority')
    customer_service_center__c  = fields.Char('Customer Service Center')
    integration_carrier_code__c = fields.Char('Internal code',size=50)
    Foundation_Date__c          = fields.Date('Foundation date')
    issuance_date__pc           = fields.Date('Issuance date')
    Jigsaw                      = fields.Char('Data.com Key',size=20)
    department__pc              = fields.Selection([('Commercial', 'Commercial'),('Purchases', 'Purchases'),('Revenues', 'Revenues'),('Financial', 'Financial'),('Medical Management', 'Medical Management'),('Legal', 'Legal'),('Marketing', 'Marketing'),('Operational', 'Operational'),('After sales', 'After sales'),('HR', 'HR')],'Department')
    PersonDepartment            = fields.Char('Department',size=80)
    department_description__pc  = fields.Char('Department Description',size=255)
    Description                 = fields.Char('Description',size=32000)
    description__pc             = fields.Char('Description',size=1000)
    benefits_text__c            = fields.Char('Description Benefits',size=255)
    DNV__c                      = fields.Float('DNV', digits=(11, 0))
    PersonDoNotCall             = fields.Boolean('Do Not Call')
    drink__pc                   = fields.Selection([('Tequila', 'Tequila'),('Wine', 'Wine'),('Saque', 'Saque'),('Beer', 'Beer'),('Vodka', 'Vodka'),('Gin', 'Gin'),('Sparkling wine', 'Sparkling wine'),('Champagne', 'Champagne'),('Whisky', 'Whisky'),('Liquor', 'Liquor')],'Drink')
    Email__c                    = fields.Char('E-mail')
    Tier                        = fields.Text('Einstein Account Tier')
    PersonEmail                 = fields.Char('Email')
    PersonHasOptedOutOfEmail    = fields.Boolean('Email Opt Out')
    NumberOfEmployees           = fields.Float('Employees', digits=(8, 0))
    Marital_Status__c           = fields.Selection([('Single', 'Single'),('Married', 'Married'),('Stable union', 'Stable union'),('Separated or Divorced', 'Separated or Divorced'),('Widower', 'Widower')],'Marital status')
    extension_number__pc        = fields.Float('Extension Number', digits=(10, 0))
    External_Id__c              = fields.Char('External Id',size=255)
    External_Id__pc             = fields.Char('External Id',size=255)
    Favorite_Cuisine__pc        = fields.Selection([('Brasileira', 'Brasileira'),('Japonesa', 'Japonesa'),('Mexicana', 'Mexicana'),('Chinesa', 'Chinesa'),('Italiana', 'Italiana'),('Indiana', 'Indiana'),('Portuguesa', 'Portuguesa'),('Árabe', 'Árabe'),('Coreana', 'Coreana')],'Favorite Cuisine')
    Fax                 = fields.Char('Fax')
    PersonHasOptedOutOfFax      = fields.Boolean('Fax Opt Out')
    gender__pc                  = fields.Selection([('Female', 'Female'),('Male', 'Male')],'Gender')
    Risk_Level__c               = fields.Text('Risk Degree')
    financial_group__c          = fields.Selection([('1', '1'),('2', '2')],'Financial Group')
    has_gift_compliance__pc     = fields.Boolean('Has Gift Compliance')
    has_reimbursement_app__c    = fields.Boolean('Has Reimbursement App')
    has_telemedicine_app__c     = fields.Boolean('Has Telemedicine App')

    Headlight__c                = fields.Selection([('Green', 'Green'),('Yellow', 'Yellow'),('Red', 'Red')],'Headlight')
    Hobby__pc                   = fields.Selection([('cuisine', 'cuisine'),('Carpentry', 'Carpentry'),('Painting', 'Painting'),('Cutting and Sewing', 'Cutting and Sewing'),('Collector', 'Collector'),('Gardening', 'Gardening'),('Photography', 'Photography'),('Dance', 'Dance'),('Skating', 'Skating')],'Hobby')

    PersonHomePhone             = fields.Char('Home Phone')
    Image__c                    = fields.Char('Image',size=32768)

    PersonIndividualId          = fields.Many2one('res.partner',string='Individual')

    Industry                    = fields.Selection([('Agriculture', 'Agriculture'),('Banking', 'Banking'),('Biotechnology', 'Biotechnology'),('Food & Beverage', 'Food & Beverage'),('Communications', 'Communications'),('Construction', 'Construction'),('Consulting', 'Consulting'),('Education', 'Education'),('Electronics', 'Electronics'),('Energy', 'Energy'),('Engineering', 'Engineering'),('Entertainment', 'Entertainment'),('Manufacturing', 'Manufacturing'),('Chemicals', 'Chemicals'),('Finance', 'Finance'),('Government', 'Government'),('Hospitality', 'Hospitality'),('Machinery', 'Machinery'),('Environmental', 'Environmental'),('Media', 'Media'),('Recreation', 'Recreation'),('Shipping', 'Shipping'),('Healthcare', 'Healthcare'),('Insurance', 'Insurance'),('Not For Profit', 'Not For Profit'),('Technology', 'Technology'),('Telecommunications', 'Telecommunications'),('Transportation', 'Transportation'),('Utilities', 'Utilities'),('Retail', 'Retail'),('Apparel', 'Apparel'),('Other', 'Other')],'Industry')

    Start_in_Broker__c          = fields.Date('Home at Brokerage')

    State_Registration__c       = fields.Char('State registration',size=50)
    Municipal_Registration__c   = fields.Char('Municipal registration',size=100)
    Languages__pc               = fields.Char('Languages',size=100)
    # LastModifiedById already present in odoo    
    PersonLastCURequestDate     = fields.Date('Last Stay-in-Touch Request Date')
    PersonLastCUUpdateDate      = fields.Date('Last Stay-in-Touch Save Date')
    PersonLeadSource            = fields.Selection([('Quotator', 'Quotator'),('Customer Event', 'Customer Event'),('Exposure', 'Exposure'),('Google AdWords', 'Google AdWords'),('Employee Indication', 'Employee Indication'),('Mailing', 'Mailing'),('Partner', 'Partner'),('Advertising', 'Advertising'),('Site', 'Site'),('Webinar', 'Webinar'),('Others', 'Others')],'Lead Source')

    Level__pc                   = fields.Selection([('None', 'None'),('decision maker', 'decision maker'),('Influencer', 'Influencer')],'Level')

    Life__c                     = fields.Float('Life', digits=(8, 0))
    Locations__c                = fields.Char('Locations',size=255)
    logo_b64__c                 = fields.Char('B64 logo',size=32768)
    PersonMailingAddress        = fields.Text('Mailing Address')
    main_benefit__c             = fields.Selection([('Health', 'Health'),('Dental', 'Dental'),('Life', 'Life'),('Medicine', 'Medicine'),('Personal_Accidents', 'Personal Accident'),('In_Company', 'Consultoria'),('Medical_Consulting', 'Consultoria Médica'),('Meal', 'Refeição'),('Food', 'Alimentação'),('Transportation', 'Transporte'),('Pension', 'Previdência'),('Travel', 'Viagem'),('Car_Fleet', 'Frota'),('Car', 'Automóvel'),('Fuel', 'Combustível'),('Occupational_Health', 'Saúde Ocupacional	'),('Checkup', 'Check-up'),('Vaccine', 'Vacina'),('eu_protegido', 'eu_protegido'),('Fee', 'Fee')],'Main Benefit')
    Mainly_Carrier__c           = fields.Char('Mainly Carrier',size=255)

    marital_status__pc          = fields.Selection([('Single', 'Single'),('Married', 'Married'),('Stable union', 'Stable union'),('Separated or Divorced', 'Separated or Divorced'),('Widower', 'Widower')],'Marital Status')
    matters_of_interest__pc     = fields.Selection([('Policy', 'Policy'),('Religion', 'Religion'),('Technology', 'Technology'),('sports', 'sports'),('Leisure', 'Leisure'),('Travel', 'Travel')],'Matters of Interest')
    mobile__c                   = fields.Char('mobile')
    PersonMobilePhone           = fields.Char('Mobile')
    Movies__pc                  = fields.Selection([('Romance', 'Romance'),('Comedy', 'Comedy'),('Adventure', 'Adventure'),('Drama', 'Drama'),('Suspense', 'Suspense'),('Terror', 'Terror')],'Movies')
    first_name__pc              = fields.Char('Mother Name',size=80)
    number_of_children__pc      = fields.Integer('Number of Children')
    NumberofLocations__c        = fields.Integer('Number of Locations')
    Company_Origin__c           = fields.Selection([('New', 'New'),('Cross Sell', 'Cross Sell'),('Up Sell', 'Up Sell'),('Drama', 'Drama'),('redeployment', 'redeployment')],'Company Origin')
    PersonOtherAddress          = fields.Text('Other Address')
    PersonOtherPhone            = fields.Char('Other Phone')
    Ownership                   = fields.Selection([('Public', 'Public'),('Private', 'Private'),('Subsidiary', 'Subsidiary'),('Other', 'Other')],'Ownership')
    parent__pc                  = fields.Many2one('res.partner',string='Parent')
    ParentId                    = fields.Many2one('res.partner',string='Parent Account')
    IsPartner                   = fields.Boolean(string='Parent Account')
    phone__c                    = fields.Char('Phone')
    phone                       = fields.Char('Phone')
    pis_pasep__pc               = fields.Char('PIS/PASEP',size=11)
    place_to_go__pc             = fields.Selection([('South America', 'South America'),('Central America', 'Central America'),('América do Norte', 'América do Norte'),('Europe', 'Europe'),('Asia', 'Asia'),('Oceania', 'Oceania'),('Africa', 'Africa')],'Place to Go')
    Rating                      = fields.Selection([('Hot', 'Hot'),('Cold', 'Cold'),('Blocked', 'Blocked'),('Global_Contract', 'Global_Contract'),('No interest', 'No interest'),('No Profile', 'No Profile'),('Non-existent phone', 'Non-existent phone')],'Rating')
    religion__pc                = fields.Selection([('Catholic', 'Catholic'),('spiritist', 'spiritist'),('evangelical', 'evangelical'),('Muslim', 'Muslim'),('Messianic', 'Messianic'),('Buddhism', 'Buddhism'),('Islam', 'Islam'),('Hinduism', 'Hinduism'),('Jewish', 'Jewish'),('Atheist', 'Atheist')],'Religion')
    Legal_Representative__pc    = fields.Boolean('Legal representative')
    market_reserve__c           = fields.Many2one('model_market_reserve__c',string='Market Reserve')
    Reserva_de_Mercado__c       = fields.Text('Market Reserve')
    RG__pc                      = fields.Char('RG',size=20)
    role__c                     = fields.Selection([('Association', 'Association'),('Strategic Partner', 'Strategic Partner'),('Strategic Broker', 'Strategic Broker'),('Partner', 'Partner')],'Role')
    Score__c                     = fields.Selection([('Promotor', 'Promotor'),('Neutral', 'Neutral'),('Detractor', 'Detractor')],'Score')
    secondary_mobile_phone__pc  = fields.Char('Secondary Mobile Phone')
    service_type__c             = fields.Selection([('Check-up', 'Check-up'),('Homecare', 'Homecare'),('Carrier/Motorbike', 'Carrier/Motorbike'),('Vaccines', 'Vaccines')],'Service Type')
    Gender__c                   = fields.Selection([('Female', 'Female'),('Male', 'Male')],'Sex')
    ShippingAddress             = fields.Text('Shipping Address')
    Sic                         = fields.Char('SIC Code',size=20)
    SicDesc                     = fields.Char('SIC Description',size=80)
    SLA__c                      = fields.Selection([('Gold', 'Gold'),('Silver', 'Silver'),('Platinum', 'Platinum'),('Bronze', 'Bronze')],'SALAD')
    SLAExpirationDate__c        = fields.Date('SLA Expiration Date')
    SLASerialNumber__c          = fields.Char('SLA Serial Number',size=10)
    soccer_team__pc             = fields.Selection([('Flamengo RJ', 'Flamengo RJ'),('Santos SP', 'Santos SP'),('Palmeiras SP', 'Palmeiras SP'),('RS Guild', 'RS Guild'),('Athletic PR', 'Athletic PR'),('Sao Paulo-SP', 'Sao Paulo-SP'),('International RS', 'International RS'),('Corinthians SP', 'Corinthians SP'),('Fortaleza CE', 'Fortaleza CE'),('Goiás GO', 'Goiás GO'),('Bahia BA', 'Bahia BA'),('Vasco da Gama RJ', 'Vasco da Gama RJ'),('Atlético MG', 'Atlético MG'),('Fluminense RJ', 'Fluminense RJ'),('Botafogo RJ', 'Botafogo RJ'),('Ceará CE', 'Ceará CE'),('Cruzeiro MG', 'Cruzeiro MG'),('CSA AL', 'CSA AL'),('Chapecoense SC', 'Chapecoense SC'),('Avaí SC', 'Avaí SC')],'Sport Practice')

    spouse_birth_date__pc       = fields.Date('Spouse Birth Date')
    spouse_gender__pc           = fields.Selection([('Female', 'Female'),('Male', 'Male')],'Spouse Gender')
    spouse_name__pc             = fields.Char('Spouse Name',size=255)
    secondary_phone__pc         = fields.Char('Secondary phone')
    TickerSymbol                = fields.Text('Ticker Symbol')
    title__pc                   = fields.Selection([('Presidente', 'Presidente'),('Vice-Presidente', 'Vice-Presidente'),('CEO', 'CEO'),('Diretor', 'Diretor'),('Superintendente', 'Superintendente'),('Gerente', 'Gerente'),('Coordenador', 'Coordenador'),('Analista', 'Analista')],'Title')
    PersonTitle                 = fields.Char('Title',size=80)
    title_description__pc       = fields.Char('Title Description',size=255)
    treatment_name__pc          = fields.Char('Treatment Name',size=255)
    Type                        = fields.Selection([('Customer', 'Customer'),('Reseller', 'Reseller'),('Press', 'Press'),('Operator', 'Operator'),('Other', 'Other'),('Partner', 'Partner'),('Prospect', 'Prospect')],'Type')
    UpsellOpportunity__c        = fields.Selection([('Maybe', 'Maybe'),('No', 'No'),('Yes', 'Yes')],'Upsell Opportunity')
    Usu_rio_do_Messaging__c     = fields.Many2one('res.users',string='Messaging User')
    Website                     = fields.Char('Website')
    wedding_date__pc            = fields.Date('Wedding Date')
    issuing_body_rg__pc         = fields.Char('Issuing Agency RG',size=10)

    # ============== Fields For Revenue start ===========================
    # CreatedById  already in odoo
    # LastModifiedById already in odoo
    OwnerId          = fields.Many2one('res.users',string='Owner')
    Prefix__c        = fields.Char('Prefix',size=3)
    # Name             = fields.Text('Revenue',size=80) already in odoo
    Income_Type__c   = fields.Selection([('direct','Direct'),('indirect','indirect')],'Type of Revenue')
    # ============== Fields For Revenue end ===========================

    financial_group_id  = fields.Many2one('model_financial_group', string="Financial Group ID")

    portal_access_ids   = fields.One2many('portal.access','account_id',string='Portal Access IDS')
    bank_account_ids     = fields.One2many('account.setup.bank.manual.config','Account_id',string='Bank Account IDS')
    attachment_ids  = fields.One2many('ir.attachment','account_id', string='Attachment IDS')
    opportunity_ids = fields.One2many('crm.lead','account_id', string='Opportunity IDS')

    partner_ids     = fields.Many2many(string='Partner IDS', comodel_name='res.partner', relation='account_partner_rel')

    address_ids = fields.One2many('model_address','Account_id', string='Address IDS')
    benificiaty_ids  = fields.One2many('model_beneficiary_carrier', 'carrier_id', string='Benificiary IDS')

    product_family_ids  = fields.One2many('product_family', 'account_id', string='Product Family IDS')
    price_list_ids  = fields.One2many('model_price_list', 'account_id', string='Price List IDS')
    network_ids  = fields.One2many('accredited_network', 'account_id', string='Network IDS')
