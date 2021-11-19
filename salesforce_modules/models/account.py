from odoo import models, fields, api


class RecordType(models.Model):
    _name = 'record_type'
    _description = "Salesforce Record Type"
    _rec_name = 'name'

    name = fields.Char('Name')


class TypeOfOperator(models.Model):
    _name = 'type_of_operator'
    _description = "Salesforce Operator"
    _rec_name = 'name'

    name = fields.Char('Name')


class Account(models.Model):
    _name = 'account.account'
    _inherit = ['account.account', 'mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Account"

    ABC_Analysis_pc = fields.Selection([('B', 'B'), ('B', 'B'), ('C', 'C')], 'ABC Analysis', track_visibility='onchange')
    Account_c = fields.Many2one('account.account', string='Account', track_visibility='onchange')
    # Name                = fields.Char('Account Name')
    AccountNumber = fields.Char('Account Number', size=40, track_visibility='onchange')
    OwnerId = fields.Many2one('res.users', string='Account Owner', track_visibility='onchange')
    RecordTypeId = fields.Many2one('record_type', string='Record Type', track_visibility='onchange')
    Site = fields.Char('Account Site', size=80, track_visibility='onchange')
    AccountSource = fields.Selection(
        [('Quotator', 'Quotator'), ('Customer Event', 'Customer Event'), ('Exposure', 'Exposure'),
         ('Google AdWords', 'Google AdWords'), ('Employee Indication', 'Employee Indication'), ('Mailing', 'Mailing'),
         ('Partner', 'Partner'), ('Advertising', 'Advertising'), ('Site', 'Site'), ('Webinar', 'Webinar'),
         ('Others', 'Others')], 'Account Source', track_visibility='onchange')
    Active_c = fields.Selection([('No', 'Not'), ('Yes', 'Yes')], 'Active', track_visibility='onchange')

    allow_create_accredited_net_case_c = fields.Boolean(string="Allow Create Accredited Net Case", track_visibility='onchange')
    allow_create_reimbursement_case_c = fields.Boolean(string="Allow Create Reimbursement Case", track_visibility='onchange')
    allow_direct_mail_pc = fields.Boolean(string="Allow Direct Mail", track_visibility='onchange')
    AnnualRevenue = fields.Float('Annual Revenue', digits=(18, 0), track_visibility='onchange')

    ans_start_c = fields.Date('YEARS Start', track_visibility='onchange')
    ans_code_c = fields.Float('ANS / SUSEP Code', digits=(10, 0), track_visibility='onchange')
    app_address_c = fields.Char('App Address', size=255, track_visibility='onchange')
    PersonAssistantName = fields.Char('Assistant', size=40, track_visibility='onchange')
    assistant_email_pc = fields.Char('Assistant E-mail', track_visibility='onchange')
    assistant_extension_number_pc = fields.Float('Assistant Extension Number', digits=(10, 0), track_visibility='onchange')
    assistant_mobile_phone_pc = fields.Char('Assistant Mobile Phone', track_visibility='onchange')
    PersonAssistantPhon = fields.Char('Asst. Phone', track_visibility='onchange')
    Active_pc = fields.Boolean('Active', track_visibility='onchange')
    benefits_c = fields.Selection(
        [('Health', 'Health'), ('Dental', 'Dental'), ('Life', 'Life'), ('Medicine', 'medicine'),
         ('Personal_Accidents', 'Personal Accident'), ('In_Company', 'Consultancy'),
         ('Medical_Consulting', 'Medical Consulting'), ('Meal', 'Snack'), ('Food', 'food'),
         ('Transportation', 'Transport'), ('Pension', 'pension'), ('Travel', 'Travel'), ('Car_Fleet', 'Frota'),
         ('Car', 'Car'), ('Fuel', 'Fuel'), ('Occupational_Health', 'occupational health'), ('Checkup', 'Check-up'),
         ('Vaccine', 'Vaccine'), ('I_protected', 'I Protected'), ('Fee', 'Fee')], 'Benefits', track_visibility='onchange')

    BillingAddress = fields.Text('Billing Address', track_visibility='onchange')
    PersonBirthdate = fields.Date('Birthdate', track_visibility='onchange')
    Broker_c = fields.Many2one('res.partner', string='Broker', track_visibility='onchange')
    broker_call_center_c = fields.Char('Broker Call Center', track_visibility='onchange')
    Social_Reason_c = fields.Char('Business Name', size=255, track_visibility='onchange')
    card_image_c = fields.Char('Card Image', size=32768, track_visibility='onchange')
    card_template_c = fields.Char('Card Template', size=32768, track_visibility='onchange')
    carrier_type_c = fields.Many2one('type_of_operator', string='Carrier Type', track_visibility='onchange')
    nationalh_health_card_pc = fields.Char('National Health Card', size=50, track_visibility='onchange')
    ChannelProgramLevelName = fields.Char('Channel Program Level Name', size=255, track_visibility='onchange')
    ChannelProgramName = fields.Char('Channel Program Name', size=255, track_visibility='onchange')
    cid_pc = fields.Char('CID', size=100, track_visibility='onchange')
    CNAE_c = fields.Many2one('model_cnae', string='NINE', track_visibility='onchange')
    CNPJ_c = fields.Char('CNPJ', size=18, track_visibility='onchange')
    CNS_c = fields.Integer('CNS', track_visibility='onchange')
    comercial_name_c = fields.Char('Comercial Name', size=255, track_visibility='onchange')
    Company_Segmentation_c = fields.Selection([('Small', 'Revenue'), ('Small_Large', 'Revenue between 40k and 100k'),
                                                ('Middle', 'Revenue between 100k and 250k'),
                                                ('Middle_Large', 'Revenue between 250k and 400k'),
                                                ('Corporate', 'Revenue between 400k and 1MM'),
                                                ('Corporate_Large', 'Revenue >1MM')], 'Company Segmentation', track_visibility='onchange')

    Company_Classification_c = fields.Selection(
        [('Small', 'Recipe <40k'), ('Small_Large', 'Revenue between 40k and 100k'),
         ('Middle', 'Revenue between 100k and 250k'), ('Middle_Large', 'Revenue between 250k and 400k'),
         ('Corporate', 'Revenue between 400k and 1MM'), ('Corporate_Large', 'Revenue >1MM')], 'Company_Classification', track_visibility='onchange')

    council_state_c = fields.Selection(
        [('AC', 'AC'), ('AL', 'AL'), ('AM', 'AM'), ('AP', 'AP'), ('BA', 'BA'), ('CE', 'CE'), ('DF', 'DF'), ('ES', 'ES'),
         ('GO', 'GO'), ('MA', 'MA'), ('MG', 'MG'), ('MS', 'MS'), ('MT', 'MT'), ('PA', 'PA'), ('PB', 'PB'), ('PE', 'PE'),
         ('PI', 'PI'), ('PR', 'PR'), ('RJ', 'RJ'), ('RN', 'RN'), ('RO', 'RO'), ('RR', 'RR'), ('RR', 'RR'), ('RS', 'RS'),
         ('SC', 'SC'), ('SE', 'SE'), ('SP', 'SP'), ('TO', 'TO')], 'Council State', track_visibility='onchange')

    CPF_c = fields.Char('CPF', size=14, track_visibility='onchange')
    cpf_pc = fields.Char('CPF', size=14, track_visibility='onchange')
    # CreatedById already in odoo
    IsCustomerPortal = fields.Selection([('1', '1'), ('2', '2')], 'Customer Portal Account', track_visibility='onchange')
    CustomerPriority_c = fields.Selection([('High', 'High'), ('Low', 'Low'), ('Medium', 'Medium')],
                                           'Customer Priority', track_visibility='onchange')
    customer_service_center_c = fields.Char('Customer Service Center', track_visibility='onchange')
    integration_carrier_code_c = fields.Char('Internal code', size=50, track_visibility='onchange')
    Foundation_Date_c = fields.Date('Foundation date', track_visibility='onchange')
    issuance_date_pc = fields.Date('Issuance date', track_visibility='onchange')
    Jigsaw = fields.Char('Data.com Key', size=20, track_visibility='onchange')
    department_pc = fields.Selection(
        [('Commercial', 'Commercial'), ('Purchases', 'Purchases'), ('Revenues', 'Revenues'), ('Financial', 'Financial'),
         ('Medical Management', 'Medical Management'), ('Legal', 'Legal'), ('Marketing', 'Marketing'),
         ('Operational', 'Operational'), ('After sales', 'After sales'), ('HR', 'HR')], 'Department', track_visibility='onchange')
    PersonDepartment = fields.Char('Department', size=80, track_visibility='onchange')
    department_description_pc = fields.Char('Department Description', size=255, track_visibility='onchange')
    Description = fields.Char('Description', size=32000, track_visibility='onchange')
    description_pc = fields.Char('Description', size=1000, track_visibility='onchange')
    benefits_text_c = fields.Char('Description Benefits', size=255, track_visibility='onchange')
    DNV_c = fields.Float('DNV', digits=(11, 0), track_visibility='onchange')
    PersonDoNotCall = fields.Boolean('Do Not Call', track_visibility='onchange')
    drink_pc = fields.Selection(
        [('Tequila', 'Tequila'), ('Wine', 'Wine'), ('Saque', 'Saque'), ('Beer', 'Beer'), ('Vodka', 'Vodka'),
         ('Gin', 'Gin'), ('Sparkling wine', 'Sparkling wine'), ('Champagne', 'Champagne'), ('Whisky', 'Whisky'),
         ('Liquor', 'Liquor')], 'Drink', track_visibility='onchange')
    Email_c = fields.Char('E-mail', track_visibility='onchange')
    Tier = fields.Text('Einstein Account Tier', track_visibility='onchange')
    PersonEmail = fields.Char('Email', track_visibility='onchange')
    PersonHasOptedOutOfEmail = fields.Boolean('Email Opt Out', track_visibility='onchange')
    NumberOfEmployees = fields.Float('Employees', digits=(8, 0), track_visibility='onchange')
    Marital_Status_c = fields.Selection(
        [('Single', 'Single'), ('Married', 'Married'), ('Stable union', 'Stable union'),
         ('Separated or Divorced', 'Separated or Divorced'), ('Widower', 'Widower')], 'Marital status', track_visibility='onchange')
    extension_number_pc = fields.Float('Extension Number', digits=(10, 0), track_visibility='onchange')
    External_Id_c = fields.Char('External Id', size=255, track_visibility='onchange')
    External_Id_pc = fields.Char('External Id', size=255, track_visibility='onchange')
    Favorite_Cuisine_pc = fields.Selection(
        [('Brasileira', 'Brasileira'), ('Japonesa', 'Japonesa'), ('Mexicana', 'Mexicana'), ('Chinesa', 'Chinesa'),
         ('Italiana', 'Italiana'), ('Indiana', 'Indiana'), ('Portuguesa', 'Portuguesa'), ('Árabe', 'Árabe'),
         ('Coreana', 'Coreana')], 'Favorite Cuisine', track_visibility='onchange')
    Fax = fields.Char('Fax')
    PersonHasOptedOutOfFax = fields.Boolean('Fax Opt Out', track_visibility='onchange')
    gender_pc = fields.Selection([('Female', 'Female'), ('Male', 'Male')], 'Gender', track_visibility='onchange')
    Risk_Level_c = fields.Text('Risk Degree', track_visibility='onchange')
    financial_group_c = fields.Selection([('1', '1'), ('2', '2')], 'Financial Group', track_visibility='onchange')
    has_gift_compliance_pc = fields.Boolean('Has Gift Compliance', track_visibility='onchange')
    has_reimbursement_app_c = fields.Boolean('Has Reimbursement App', track_visibility='onchange')
    has_telemedicine_app_c = fields.Boolean('Has Telemedicine App', track_visibility='onchange')

    Headlight_c = fields.Selection([('Green', 'Green'), ('Yellow', 'Yellow'), ('Red', 'Red')], 'Headlight', track_visibility='onchange')
    Hobby_pc = fields.Selection([('cuisine', 'cuisine'), ('Carpentry', 'Carpentry'), ('Painting', 'Painting'),
                                  ('Cutting and Sewing', 'Cutting and Sewing'), ('Collector', 'Collector'),
                                  ('Gardening', 'Gardening'), ('Photography', 'Photography'), ('Dance', 'Dance'),
                                  ('Skating', 'Skating')], 'Hobby', track_visibility='onchange')

    PersonHomePhone = fields.Char('Home Phone', track_visibility='onchange')
    Image_c = fields.Char('Image', size=32768, track_visibility='onchange')

    PersonIndividualId = fields.Many2one('res.partner', string='Individual', track_visibility='onchange')

    Industry = fields.Selection(
        [('Agriculture', 'Agriculture'), ('Banking', 'Banking'), ('Biotechnology', 'Biotechnology'),
         ('Food & Beverage', 'Food & Beverage'), ('Communications', 'Communications'), ('Construction', 'Construction'),
         ('Consulting', 'Consulting'), ('Education', 'Education'), ('Electronics', 'Electronics'), ('Energy', 'Energy'),
         ('Engineering', 'Engineering'), ('Entertainment', 'Entertainment'), ('Manufacturing', 'Manufacturing'),
         ('Chemicals', 'Chemicals'), ('Finance', 'Finance'), ('Government', 'Government'),
         ('Hospitality', 'Hospitality'), ('Machinery', 'Machinery'), ('Environmental', 'Environmental'),
         ('Media', 'Media'), ('Recreation', 'Recreation'), ('Shipping', 'Shipping'), ('Healthcare', 'Healthcare'),
         ('Insurance', 'Insurance'), ('Not For Profit', 'Not For Profit'), ('Technology', 'Technology'),
         ('Telecommunications', 'Telecommunications'), ('Transportation', 'Transportation'), ('Utilities', 'Utilities'),
         ('Retail', 'Retail'), ('Apparel', 'Apparel'), ('Other', 'Other')], 'Industry', track_visibility='onchange')

    Start_in_Broker_c = fields.Date('Home at Brokerage', track_visibility='onchange')

    State_Registration_c = fields.Char('State registration', size=50, track_visibility='onchange')
    Municipal_Registration_c = fields.Char('Municipal registration', size=100, track_visibility='onchange')
    Languages_pc = fields.Char('Languages', size=100, track_visibility='onchange')
    # LastModifiedById already present in odoo    
    PersonLastCURequestDate = fields.Date('Last Stay-in-Touch Request Date', track_visibility='onchange')
    PersonLastCUUpdateDate = fields.Date('Last Stay-in-Touch Save Date', track_visibility='onchange')
    PersonLeadSource = fields.Selection(
        [('Quotator', 'Quotator'), ('Customer Event', 'Customer Event'), ('Exposure', 'Exposure'),
         ('Google AdWords', 'Google AdWords'), ('Employee Indication', 'Employee Indication'), ('Mailing', 'Mailing'),
         ('Partner', 'Partner'), ('Advertising', 'Advertising'), ('Site', 'Site'), ('Webinar', 'Webinar'),
         ('Others', 'Others')], 'Lead Source', track_visibility='onchange')

    Level_pc = fields.Selection([('None', 'None'), ('decision maker', 'decision maker'), ('Influencer', 'Influencer')],
                                 'Level', track_visibility='onchange')

    Life_c = fields.Float('Life', digits=(8, 0), track_visibility='onchange')
    Locations_c = fields.Char('Locations', size=255, track_visibility='onchange')
    logo_b64_c = fields.Char('B64 logo', size=32768, track_visibility='onchange')
    PersonMailingAddress = fields.Text('Mailing Address', track_visibility='onchange')
    main_benefit_c = fields.Selection(
        [('Health', 'Health'), ('Dental', 'Dental'), ('Life', 'Life'), ('Medicine', 'Medicine'),
         ('Personal_Accidents', 'Personal Accident'), ('In_Company', 'Consultoria'),
         ('Medical_Consulting', 'Consultoria Médica'), ('Meal', 'Refeição'), ('Food', 'Alimentação'),
         ('Transportation', 'Transporte'), ('Pension', 'Previdência'), ('Travel', 'Viagem'), ('Car_Fleet', 'Frota'),
         ('Car', 'Automóvel'), ('Fuel', 'Combustível'), ('Occupational_Health', 'Saúde Ocupacional	'),
         ('Checkup', 'Check-up'), ('Vaccine', 'Vacina'), ('eu_protegido', 'eu_protegido'), ('Fee', 'Fee')],
        'Main Benefit', track_visibility='onchange')
    Mainly_Carrier_c = fields.Char('Mainly Carrier', size=255, track_visibility='onchange')

    marital_status_pc = fields.Selection(
        [('Single', 'Single'), ('Married', 'Married'), ('Stable union', 'Stable union'),
         ('Separated or Divorced', 'Separated or Divorced'), ('Widower', 'Widower')], 'Marital Status', track_visibility='onchange')
    matters_of_interest_pc = fields.Selection(
        [('Policy', 'Policy'), ('Religion', 'Religion'), ('Technology', 'Technology'), ('sports', 'sports'),
         ('Leisure', 'Leisure'), ('Travel', 'Travel')], 'Matters of Interest', track_visibility='onchange')
    mobile_c = fields.Char('mobile', track_visibility='onchange')
    PersonMobilePhone = fields.Char('Mobile', track_visibility='onchange')
    Movies_pc = fields.Selection(
        [('Romance', 'Romance'), ('Comedy', 'Comedy'), ('Adventure', 'Adventure'), ('Drama', 'Drama'),
         ('Suspense', 'Suspense'), ('Terror', 'Terror')], 'Movies', track_visibility='onchange')
    first_name_pc = fields.Char('Mother Name', size=80, track_visibility='onchange')
    number_of_children_pc = fields.Integer('Number of Children', track_visibility='onchange')
    NumberofLocations_c = fields.Integer('Number of Locations', track_visibility='onchange')
    Company_Origin_c = fields.Selection(
        [('New', 'New'), ('Cross Sell', 'Cross Sell'), ('Up Sell', 'Up Sell'), ('Drama', 'Drama'),
         ('redeployment', 'redeployment')], 'Company Origin', track_visibility='onchange')
    PersonOtherAddress = fields.Text('Other Address', track_visibility='onchange')
    PersonOtherPhone = fields.Char('Other Phone', track_visibility='onchange')
    Ownership = fields.Selection(
        [('Public', 'Public'), ('Private', 'Private'), ('Subsidiary', 'Subsidiary'), ('Other', 'Other')], 'Ownership')
    parent_pc = fields.Many2one('res.partner', string='Parent', track_visibility='onchange')
    ParentId = fields.Many2one('res.partner', string='Parent Account', track_visibility='onchange')
    IsPartner = fields.Boolean(string='Parent Account', track_visibility='onchange')
    phone_c = fields.Char('Phone', track_visibility='onchange')
    phone = fields.Char('Phone', track_visibility='onchange')
    pis_pasep_pc = fields.Char('PIS/PASEP', size=11, track_visibility='onchange')
    place_to_go_pc = fields.Selection([('South America', 'South America'), ('Central America', 'Central America'),
                                        ('América do Norte', 'América do Norte'), ('Europe', 'Europe'),
                                        ('Asia', 'Asia'), ('Oceania', 'Oceania'), ('Africa', 'Africa')], 'Place to Go', track_visibility='onchange')
    Rating = fields.Selection(
        [('Hot', 'Hot'), ('Cold', 'Cold'), ('Blocked', 'Blocked'), ('Global_Contract', 'Global_Contract'),
         ('No interest', 'No interest'), ('No Profile', 'No Profile'), ('Non-existent phone', 'Non-existent phone')],
        'Rating', track_visibility='onchange')
    religion_pc = fields.Selection(
        [('Catholic', 'Catholic'), ('spiritist', 'spiritist'), ('evangelical', 'evangelical'), ('Muslim', 'Muslim'),
         ('Messianic', 'Messianic'), ('Buddhism', 'Buddhism'), ('Islam', 'Islam'), ('Hinduism', 'Hinduism'),
         ('Jewish', 'Jewish'), ('Atheist', 'Atheist')], 'Religion', track_visibility='onchange')
    Legal_Representative_pc = fields.Boolean('Legal representative', track_visibility='onchange')
    market_reserve_c = fields.Many2one('model_market_reserve__c', string='Market Reserve', track_visibility='onchange')
    Reserva_de_Mercado_c = fields.Text('Market Reserve', track_visibility='onchange')
    RG_pc = fields.Char('RG', size=20, track_visibility='onchange')
    role_c = fields.Selection([('Association', 'Association'), ('Strategic Partner', 'Strategic Partner'),
                                ('Strategic Broker', 'Strategic Broker'), ('Partner', 'Partner')], 'Role', track_visibility='onchange')
    Score_c = fields.Selection([('Promotor', 'Promotor'), ('Neutral', 'Neutral'), ('Detractor', 'Detractor')], 'Score', track_visibility='onchange')
    secondary_mobile_phone_pc = fields.Char('Secondary Mobile Phone', track_visibility='onchange')
    service_type_c = fields.Selection(
        [('Check-up', 'Check-up'), ('Homecare', 'Homecare'), ('Carrier/Motorbike', 'Carrier/Motorbike'),
         ('Vaccines', 'Vaccines')], 'Service Type', track_visibility='onchange')
    Gender_c = fields.Selection([('Female', 'Female'), ('Male', 'Male')], 'Sex', track_visibility='onchange')
    ShippingAddress = fields.Text('Shipping Address', track_visibility='onchange')
    Sic = fields.Char('SIC Code', size=20, track_visibility='onchange')
    SicDesc = fields.Char('SIC Description', size=80, track_visibility='onchange')
    SLA_c = fields.Selection([('Gold', 'Gold'), ('Silver', 'Silver'), ('Platinum', 'Platinum'), ('Bronze', 'Bronze')],
                              'SALAD', track_visibility='onchange')
    SLAExpirationDate_c = fields.Date('SLA Expiration Date', track_visibility='onchange')
    SLASerialNumber_c = fields.Char('SLA Serial Number', size=10, track_visibility='onchange')
    soccer_team_pc = fields.Selection(
        [('Flamengo RJ', 'Flamengo RJ'), ('Santos SP', 'Santos SP'), ('Palmeiras SP', 'Palmeiras SP'),
         ('RS Guild', 'RS Guild'), ('Athletic PR', 'Athletic PR'), ('Sao Paulo-SP', 'Sao Paulo-SP'),
         ('International RS', 'International RS'), ('Corinthians SP', 'Corinthians SP'),
         ('Fortaleza CE', 'Fortaleza CE'), ('Goiás GO', 'Goiás GO'), ('Bahia BA', 'Bahia BA'),
         ('Vasco da Gama RJ', 'Vasco da Gama RJ'), ('Atlético MG', 'Atlético MG'), ('Fluminense RJ', 'Fluminense RJ'),
         ('Botafogo RJ', 'Botafogo RJ'), ('Ceará CE', 'Ceará CE'), ('Cruzeiro MG', 'Cruzeiro MG'), ('CSA AL', 'CSA AL'),
         ('Chapecoense SC', 'Chapecoense SC'), ('Avaí SC', 'Avaí SC')], 'Soccer Team', track_visibility='onchange')

    sport_practice_pc = fields.Selection(
        [('Futebol', 'Futebol'), ('Basquetebol', 'Basquetebol'), ('Surf', 'Surf'),
         ('Golf', 'Golf'), ('Tênis', 'Tênis'), ('Corrida', 'Corrida'),
         ('Voleibol', 'Voleibol'), ('Equitação', 'Equitação'),
         ('Alpinismo', 'Alpinismo'), ('Iatismo', 'Iatismo')], 'Sport Practice', track_visibility='onchange')

    spouse_birth_date_pc = fields.Date('Spouse Birth Date', track_visibility='onchange')
    spouse_gender_pc = fields.Selection([('Female', 'Female'), ('Male', 'Male')], 'Spouse Gender', track_visibility='onchange')
    spouse_name_pc = fields.Char('Spouse Name', size=255, track_visibility='onchange')
    secondary_phone_pc = fields.Char('Secondary phone', track_visibility='onchange')
    TickerSymbol = fields.Text('Ticker Symbol', track_visibility='onchange')
    title_pc = fields.Selection(
        [('Presidente', 'Presidente'), ('Vice-Presidente', 'Vice-Presidente'), ('CEO', 'CEO'), ('Diretor', 'Diretor'),
         ('Superintendente', 'Superintendente'), ('Gerente', 'Gerente'), ('Coordenador', 'Coordenador'),
         ('Analista', 'Analista')], 'Title', track_visibility='onchange')
    PersonTitle = fields.Char('Title', size=80, track_visibility='onchange')
    title_description_pc = fields.Char('Title Description', size=255, track_visibility='onchange')
    treatment_name_pc = fields.Char('Treatment Name', size=255, track_visibility='onchange')
    Type = fields.Selection(
        [('Customer', 'Customer'), ('Reseller', 'Reseller'), ('Press', 'Press'), ('Operator', 'Operator'),
         ('Other', 'Other'), ('Partner', 'Partner'), ('Prospect', 'Prospect')], 'Type', track_visibility='onchange')
    UpsellOpportunity_c = fields.Selection([('Maybe', 'Maybe'), ('No', 'No'), ('Yes', 'Yes')], 'Upsell Opportunity', track_visibility='onchange')
    Usu_rio_do_Messaging_c = fields.Many2one('res.users', string='Messaging User', track_visibility='onchange')
    Website = fields.Char('Website', track_visibility='onchange')
    wedding_date_pc = fields.Date('Wedding Date', track_visibility='onchange')
    issuing_body_rg_pc = fields.Char('Issuing Agency RG', size=10, track_visibility='onchange')

    broker_id = fields.Many2one('broker', string='Broker', track_visibility='onchange')


    # ============== Fields For Revenue start ===========================
    # CreatedById  already in odoo
    # LastModifiedById already in odoo
    OwnerId = fields.Many2one('res.users', string='Owner', track_visibility='onchange')
    Prefix_c = fields.Char('Prefix', size=3, track_visibility='onchange')
    # Name             = fields.Text('Revenue',size=80) already in odoo
    Income_Type_c = fields.Selection([('direct', 'Direct'), ('indirect', 'indirect')], 'Type of Revenue', track_visibility='onchange')
    # ============== Fields For Revenue end ===========================

    financial_group_id = fields.Many2one('model_financial_group', string="Financial Group ID", track_visibility='onchange')

    portal_access_ids = fields.One2many('portal.access', 'account_id', string='Portal Access')
    bank_account_ids = fields.One2many('account.setup.bank.manual.config', 'Account_id', string='Bank Account')
    attachment_ids = fields.One2many('ir.attachment', 'account_id', string='Attachment')
    opportunity_ids = fields.One2many('crm.lead', 'account_id', string='Opportunity')

    partner_ids = fields.Many2many(string='Partner', comodel_name='res.partner', relation='account_partner_rel')

    address_ids = fields.One2many('model_address', 'Account_id', string='Address')
    benificiaty_ids = fields.One2many('model_beneficiary_carrier', 'carrier_id', string='Benificiary')

    product_family_ids = fields.One2many('product_family', 'account_id', string='Product Family')
    price_list_ids = fields.One2many('model_price_list', 'account_id', string='Price List')
    network_ids = fields.One2many('accredited_network', 'account_id', string='Network')
    case_ids = fields.One2many('model_case', 'AccountId', string='Account')
    benefit_politic_ids = fields.One2many('model_benfit_politic', 'Account_id', string='Benefit Politic')
    contract_partner_ids = fields.One2many('contract.partner', 'partner_id', string='Partner')
    partner_id = fields.Many2one('res.partner', string='partner Name')
    carrier_id =  fields.Many2one('model_carrier_type_c')