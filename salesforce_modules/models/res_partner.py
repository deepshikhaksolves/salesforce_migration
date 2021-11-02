from odoo import models, fields, api, _
from odoo.exceptions import UserError

class ResPartner(models.Model):
    _name = 'res.partner'
    _inherit = ['res.partner', 'mail.thread', 'mail.activity.mixin']

    ABC_Analysis = fields.Selection([
        ('A', 'A'), ('B', 'B'), ('C', 'C')
    ], string='ABC Analysis')
    AccountId = fields.Many2one('account.account', string='Account Name')
    allow_direct_mail = fields.Boolean(string='Allow Direct Mail')
    AssistantName = fields.Text(string='Assistant')
    assistant_email = fields.Char(string='Assistant E-mail')
    assistant_extension_number = fields.Float(string='Assistant Extension Number', digits=(10, 0))
    assistant_mobile_phone = fields.Char(string='Assistant Mobile Phone')
    AssistantPhone = fields.Char(string='Asst. Phone')
    Active = fields.Boolean(string='Active')
    Birthdate = fields.Date(string='Birthdate')
    nationalh_health_card = fields.Text(string='National Health Card', size=50)
    cid = fields.Text(string='CID', size=100)
    OwnerId = fields.Many2one('res.users', string='Contact Owner')
    cpf = fields.Text(string='CPF', size=14)
    # CreatedById  added default
    Department = fields.Text(string='Department', size=80)
    department_description = fields.Text(string='Department Description', size=255)
    Description = fields.Text(string='Description')
    DoNotCall = fields.Boolean(string='Do Not Call')
    Email = fields.Char(string='Email')
    HasOptedOutOfEmail = fields.Boolean(string='Email Opt Out')
    extension_number = fields.Float(string='Extension Number', digits=(10, 0))
    External_Id = fields.Text(string='External Id', size=255)
    Favorite_Cuisine = fields.Selection([
        ('Brazilian', 'Brazilian'),('Japanese', 'Japanese'),('mexican', 'mexican'),('chinese', 'chinese'),('italian', 'italian'),('indian', 'indian'),('Portuguese', 'Portuguese'),('arabic', 'arabic'),('korean', 'korean')
    ], string='Favorite Cuisine')
    Fax = fields.Char(string='Fax')
    HasOptedOutOfFax = fields.Boolean(string='Fax Opt Out')
    gender = fields.Selection([
        ('Feminine', 'Feminine'), ('Masculine', 'Masculine')
    ], string='Gender')
    has_gift_compliance = fields.Boolean(string='Has Gift Compliance')
    Hobby = fields.Selection([
        ('Cooking', 'Cooking'), ('carpentry', 'carpentry'), ('painting', 'painting'), ('Cutting_and_Sewing', 'Cutting and Sewing'), ('collector', 'collector'), ('gardening', 'gardening'), ('Photography', 'Photography'), ('dance', 'dance'), ('skating', 'skating')
    ], string='Hobby')
    HomePhone = fields.Char(string='Home Phone')
    # IndividualId
    Languages = fields.Text(string='Languages', size=100)
    # LastModifiedById created by default
    LastCURequestDate = fields.Datetime(string='Last Stay-in-Touch Request Date')
    LastCUUpdateDate = fields.Datetime(string='Last Stay-in-Touch Save Date')
    LeadSource = fields.Selection([
        ('Quotator', 'Quotator'),('Customer_Event', 'Customer Event'),('Exhibition', 'Exhibition'),('Google_AdWords', 'Google AdWords'),('Employee_Referral', 'Employee Referral'),('mailing', 'mailing'),('Partner', 'Partner'),('Advertising', 'Advertising'),('Website', 'Website'),('webinar', 'webinar'),('Others', 'Others')
    ], string='Lead Source')
    Level = fields.Selection([
        ('None', 'None'), ('decision_maker', 'decision maker'), ('Influencer', 'Influencer')
    ], string='Level')
    MailingAddress = fields.Char(string='Mailing Address')
    marital_status = fields.Selection([
        ('single', 'single'), ('married', 'married'), ('Stable_Union', 'Stable Union'), ('Separated_or_Divorced', 'Separated or Divorced'), ('widower', 'widower')
    ], string='Marital Status')
    matters_of_interest = fields.Selection([
        ('Policy', 'Policy'), ('Religion', 'Religion'),('Technology', 'Technology'),('sports', 'sports'),('Leisure', 'Leisure'),('Travel', 'Travel'),
    ], string='Matters of Interest')
    MobilePhone = fields.Char(string='Mobile')
    Movies = fields.Selection([
        ('key', 'value')
    ], string='Movies')
    Name = fields.Char(string='Name')
    number_of_children = fields.Integer(string='Number of Children')
    OtherAddress = fields.Char(string='Other Address')
    OtherPhone = fields.Char(string='Other Phone')
    parent = fields.Many2one('res.partner', string='Parent')
    Phone = fields.Char(string='Phone')
    pis_pasep = fields.Char(string='PIS/PASEP')
    place_to_go = fields.Selection([
        ('South America', 'South America'), ('Central America', 'Central America'), ('North America', 'North America'), ('Europe', 'Europe'), ('Asia', 'Asia'), ('oceania', 'oceania'), ('africa', 'africa')
    ], string='Place to Go')
    religion = fields.Selection([
        ('Catholic', 'Catholic'), ('spiritist', 'spiritist'), ('evangelical', 'evangelical'), ('Muslim', 'Muslim'), ('Messianic', 'Messianic'), ('Buddhism', 'Buddhism'), ('Islam', 'Islam'), ('Hinduism', 'Hinduism'), ('Jewish', 'Jewish'), ('Atheist', 'Atheist')
    ], string='Religion')
    ReportsToId = fields.Many2one('res.partner', string='Reports To')
    Legal_Representative = fields.Boolean(string='Legal representative')
    RG = fields.Text(string='RG', size=20)
    secondary_mobile_phone = fields.Char(string='Secondary Mobile Phone')
    soccer_team = fields.Selection([
        ('Flamengo_RJ', 'Flamengo RJ'), ('Santos SP', 'Santos SP'), ('Palmeiras SP', 'Palmeiras SP'), ('RS Guild', 'RS Guild'), ('Athletic PR', 'Athletic PR'), ('Sao Paulo SP', 'Sao Paulo SP'), ('International RS', 'International RS'), ('Corinthians SP', 'Corinthians SP'), ('Fortaleza CE', 'Fortaleza CE'), ('Goiás GO', 'Goiás GO'), ('Bahia BA', 'Bahia BA'), ('Vasco da Gama RJ', 'Vasco da Gama RJ'), ('Atlético MG', 'Atlético MG'), ('Fluminense RJ', 'Fluminense RJ'), ('Botafogo RJ', 'Botafogo RJ'), ('Ceará CE', 'Ceará CE'), ('MG Cruise', 'MG Cruise'), ('CSA AL', 'CSA AL'), ('Chapecoense SC', 'Chapecoense SC'), ('Avaí SC', 'Avaí SC')
    ], string='Soccer Team')
    sport_practice = fields.Selection([
        ('football', 'football'), ('basketball', 'basketball'), ('surf', 'surf'), ('Golf', 'Golf'), ('Tennis', 'Tennis'), ('race', 'race'), ('Volleyball', 'Volleyball'), ('Riding', 'Riding'), ('Mountaineering', 'Mountaineering'), ('yachting', 'yachting')
    ], string='Sport Practice')
    spouse_birth_date = fields.Date(string='Spouse Birth Date')
    spouse_gender = fields.Selection([
        ('Feminine', 'Feminine'), ('Masculine', 'Masculine')
    ], string='Spouse Gender')
    spouse_name = fields.Text(string='Spouse Name', size=255)
    secondary_phone = fields.Char(string='Secondary phone')
    title = fields.Selection([
        ('President', 'President'), ('Vice President', 'Vice President'), ('CEO', 'CEO'), ('Director', 'Director'), ('Superintendent', 'Superintendent'), ('Manager', 'Manager'), ('Coordinator', 'Coordinator'), ('Analyst', 'Analyst')
    ], string='Title')
    Title__c = fields.Char(string='Title', size=128)
    title_description = fields.Char(string='Title Description', size=255)
    treatment_name = fields.Char(string='Treatment Name', size=255)
    wedding_date = fields.Date(string='Wedding Date')
    issuing_body_rg = fields.Char(string='Issuing Agency RG', size=10)
    opportunity_ids = fields.One2many('crm.lead', 'partner_id', string='Opportunity IDS')
    account_ids = fields.One2many('account.account', 'partner_id', string='Account IDS')
    attachment_ids = fields.Many2many('ir.attachment', 'partner_id', string='Attachment IDS')
    case_ids = fields.One2many('model_case', 'partner_id', string='Case IDS')
    contract_id = fields.Many2one('hr.contract', string='Contract')