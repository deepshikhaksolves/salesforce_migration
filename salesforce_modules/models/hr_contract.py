from odoo import models, fields, api

class HrContract(models.Model):
    _inherit = 'hr.contract'

    Account_id = fields.Many2one('account.account', string='Account Name')
    cashier_payment = fields.Boolean(string='Accepts Payment at the Cashier')
    # Activated By added in default which is responsiblee user
    activated_date = fields.Datetime(string='Activated Date')
    adjustment_negotiation_notification = fields.Selection([
        ('60', '60'), ('90', '90'), ('120', '120')
    ], string='Adjustment Negotiation Notification')
    administrator = fields.Many2one('account.account', string='Administrator')
    absence = fields.Float(string='Away')
    Broking = fields.Float(string='Agency')
    house_hold = fields.Float(string='Aggregates')
    amount_of_wages = fields.Float(string='Amount of Wages')
    recruiter_code = fields.Float(string='Collector Code')
    retired = fields.Float(string='Retired')
    approval = fields.Float(string='Approval')
    policy = fields.Char(string='Policy')
    average_rate = fields.Float(string='Average Rate')
    calculation_basis = fields.Selection([
        ('about_agency', 'About Agency'), ('about_commission', 'About Commission')
    ], string='Calculation Basis')
    benefits = fields.Selection([
        ('health', 'Health'),('dental', 'Dental'),('life', 'Life'),('medicine', 'Medicine'),('personal accidents', 'Personal Accidents'),('in_company', 'Consultoria'),('medical_consulting', 'Medical Consulting'),('meal', 'Meal'),('food', 'Food'),('transportation', 'Transportation'),('pension', 'pension'),('travel', 'Travel'),('car_fleet', 'Fleet'),('car', 'Automobile Car'),('fuel', 'Fuel'),('occupational_health', 'Occupational Health'),('checkup', 'Check-up'),('vaccine', 'Vaccine'),('I_Protected', 'I Protected'),('fee', 'Fee'),
    ], string='Benefits')
    business_name = fields.Char(string='Business Name', size=255)
    channel_segmentation = fields.Many2one('channel_segmentation', string='Sales channel')
    cancellation_notice = fields.Text(string='Cancellation Notice')
    cancellation_requester = fields.Selection([
        ('Cliente', 'Cliente'),('Operadora', 'Operadora')
    ], string='Cancellation Requester')
    capital = fields.Selection([
        ('uniform', 'Uniform'),('multiple', 'Multiple'),('staggered', 'Staggered'),('free_choice', 'Free Choice'),('global', 'Global')
    ], string='Capital')
    max_capital_insured_complementar = fields.Float(string='Maximum Supplementary Insured Capital',)
    max_capital_insured_spouse = fields.Float(string='Maximum Capital of the Insured Spouse')
    min_capital_insured_spouse = fields.Float(string='Minimum Capital of the Insured Spouse')
    card_type = fields.Selection([
        ('physical', 'Physical'), ('virtual', 'Virtual')
    ], string='Card Type')
    carrier_2 = fields.Many2one('account.account', string='Carrier')
    carrier_data_cancelation = fields.Date(string='Carrier Data Cancelation')
    cnpj = fields.Char(string='CNPJ', size=18, )
    comission = fields.Float(string='Comission')
    company_classification = fields.Selection([
        ('small', 'Small (up to 99 lives)'), ('middle', 'Middle (100 to 999 lives)'), ('corporate', 'Corporate (1,000 or more lives)') 
    ], string='Company Classification')
    company_signed_id = fields.Many2one('res.users', string='Company Signed By')
    company_signed_date = fields.Date(string='Company Signed Date')
    additional_driver = fields.Many2one('account.account', string='Additional Driver')
    consulting = fields.Many2one('account.account', string='consulting')
    seller_consulting = fields.Many2one('res.users', string='Sales consultant')
    # EndDate created in default with name End date
    # name created in default with name name 
    contract_number = fields.Char(string='Contract Number')
    Owner_id = fields.Many2one('res.users', string='Contract Owner')
    record_type = fields.Char(string='Contract Record Type')
    # StartDate created in default with name date_start
    # contract_summary created in default with name Notes
    contract_term = fields.Integer(string='Contract Term (months)')
    contrib_devol_paid_by_broker = fields.Selection([
        ('by_fixed_amount', 'By Fixed Amount '), ('per_percent', 'Per Percent'), ('by_model', 'By Model'), ('no_contribution_return ', 'No Contribution/Return ')
    ], string='Contribution/Return Paid by the Broker')
    taxpayer = fields.Selection([
        ('by_salary_range', 'By Salary Range'), ('by_percentage', 'By Percentage'), ('by_value', 'By Value'), ('no_contribution', 'No Contribution') 
    ], string='Contributory')
    correction_index = fields.Selection([
        ('yes', 'Yes'), ('no', 'NO')
    ], string='Correction Index')
    # Broker_Partner not clear
    # CreatedById created in default with name crated by
    custome_signed_id = fields.Many2one('res.partner', string='Customer Signed By')
    custome_signed_date = fields.Date(string='Customer Signed Date')
    customer_signed_title = fields.Char(string='Customer_Signed_Title', size=40, )
    cut_off_date = fields.Float(string='Movement Cutoff Date')
    broker_start_date = fields.Date(string='Start date at brokerage')
    broker_end_date = fields.Date(string='End date at brokerage')
    date_of_issue_copay = fields.Float(string='Date of Issue - Copay')
    Date_of_Issue_Invoice = fields.Float(string='Date of Issue - Invoice')
    decline_notice = fields.Text(string='Decline Notice')
    decline_reason = fields.Selection([
        ('none', 'None'), ('high_risk', 'High risk'), ('CNAE_not_marketed ', 'CNAE not marketed '), ('out_of_coverage_area', 'Out of Coverage Area'), ('outside_the_trading_area', 'Outside the Trading Area'), ('outside_acceptance_rule', 'Outside Acceptance Rule'), ('does_not_have_a_minimum_amount_of_lives_required', 'Does not have a minimum amount of lives required'), ('due_to_the_decline_of_the_medical_area', 'Due to the decline of the Medical Area'), ('due_to_operator_decline', 'Due to Operator Decline'), ('by_company_request', 'By Company Request'), ('other', 'Other')
    ], string='	Decline Reason')
    fired = fields.Float(string='Fired')
    deployment_talk = fields.Boolean(string='Deployment Talk')
    f_description = fields.Char(string='Description')
    description = fields.Text(string='Description')
    destination = fields.Selection([
        ('north_america', 'North America'), ('central_america', 'Central America'), ('south_america', 'South America'), ('europe', 'Europe'), ('africa_asia', 'Africa, Asia'), ('asia', 'Asia'), ('oceania', 'Oceania'), ('multiple_destinations', 'Multiple Destinations'), ('Brasil', 'Brazil')
    ], string='Destination')
    due_date = fields.Date(string='Due Date')
    due_date_copay = fields.Date(string='Due Date - Copay')
    due_date_invoice = fields.Date(string='Due Date - Invoice')
    interns = fields.Float(string='Interns')
    stage_of_implanta_o = fields.Selection([
        ('documentation_analysis', 'Documentation Analysis'), ('Checklist', 'Check list'), ('implantation', 'Implantation')
    ], string='')
    executive_manager = fields.Many2one('res.users', string='Executive Manager')
    child_with_disability = fields.Float(string='Disabled children')
    financial_group = fields.Many2one('model_financial_group', string='Financial Group')
    financial_index = fields.Selection([
        ('vcmh', 'Vcmh'), ('ipca', 'ipca'), ('igpm', 'Igpm'), ('vco', 'Vco')  
    ], string='')
    flag_readjustment_notif_manager = fields.Boolean(string='Flag Readjustment Notif. Manager')
    transfer_method_out = fields.Selection([
        ('email', 'E-mail'), ('ftp', 'File Transfer Protocol (FTP)'), ('site', 'Site')
    ], string='Invoice Submission Method')
    transfer_method_card_out = fields.Selection([
        ('email', 'E-mail'), ('ftp', 'File Transfer Protocol (FTP)'), ('site', 'Site')
    ], string='How to send the card')
    transfer_method_in = fields.Selection([
        ('email', 'E-mail'), ('ftp', 'File Transfer Protocol (FTP)'), ('site', 'Site')
    ], string='Invoice Receipt Method')
    transfer_method_card_out = fields.Selection([
        ('email', 'E-mail'), ('ftp', 'File Transfer Protocol (FTP)'), ('site', 'Site')
    ], string='Card Receipt Method')
    funeral_assistance = fields.Boolean(string='Funeral Assistance')
    funeral_assistance_value = fields.Float(string='Funeral Assistance Value')
    give_up_notice = fields.Text(string='Give Up Notice')
    give_up_reason = fields.Selection([
        ('grace_period_application', 'Grace Period Application'), ('change_in_the_cost_table', 'Change in the Cost Table'), ('reactivation_in_the_current_plan', 'Reactivation in the Current Plan'), ('brokerage_transfer_cancellation', 'Brokerage Transfer Cancellation'), ('does_not_have_a_minimum_amount_of_lives_required', 'Does not have a minimum amount of lives required'), ('others', 'Others')
    ], string='Give Up Reason')
    has_checkup = fields.Boolean(string='Has Checkup?')
    has_partner = fields.Boolean(string='Has Partner')
    home_care = fields.Float(string='Home Care')
    in_approval_adjustment_negotiation = fields.Boolean(string='In Approval Adjustment Negotiation')
    in_approval_contract_cancelation = fields.Boolean(string='In Approval Contract Cancellation')
    pat_registration = fields.Float(string='PAT Registration')
    insurance_deductible = fields.Boolean(string='Insurance Deductible')
    credit_start = fields.Float(string='Start of Credit')
    # LastModifiedById created by default
    purchase_limit = fields.Selection([
        ('fixed_value', 'Fixed value'), ('percentage_of_salary', 'Percentage of salary')
    ], string='Purchase_Limit')
    claim_limit = fields.Float(string='Technical Limit')
    # main_partner_not clear
    brand = fields.Char(string='mark')
    max_capital_limit = fields.Float(string='Max Capital Limit')
    min_Capital_Limit = fields.Float(string='Min Capital Limit')
    payment_mode = fields.Selection([
        ('pre_payment', 'pre-payment'), ('post_payment', 'post-payment')
    ], string='Payment Method')
    fee_model = fields.Selection([
        ('small', 'Small'), ('rebate', 'Rebate')
    ], string='Model')
    Model = fields.Many2one('salesforce.model_c', string='Model')
    moderator_variable = fields.Selection([
        ('no_moderating_factor', 'No Moderating Factor'), ('coparticipation_reverted_company', 'Reverted to'), ('coparticipation_reverted_to_operator', 'Reverted to Operator'),
    ], string='Moderator Variable')
    moderator_variable_value = fields.Float(string='Moderator Variable Value')
    cancellation_reason = fields.Selection([
        ('cost', 'Cost'), ('service_team', 'Service Team'), ('operational', 'Operational'), ('accredited_network', 'Accredited Network'), ('insurance', 'Insurance'), ('service', 'Service')
    ], string='Reason for Cancellation')
    payment_method = fields.Selection([
        ('bank_slip', 'Bank slip'), ('credit_card', 'Credit Card'), ('debit_card', 'Debit Card'), ('check', 'check'), ('automatic_debit', 'Automatic debit'), ('money', 'Money'), ('invoice', 'Invoice'),
    ], string='Payment method')
    opportunity = fields.Many2one('crm.lead', string='Opportunity')
    contract_origin = fields.Selection([
        ('new', 'New'), ('cross_sell', 'Cross Sell'), ('up sell', 'Up Sell'), ('reimplantation', 'Reimplantation'),
    ], string='Contract Origin')
    owner_expiration_notice = fields.Selection([
        ('key', 'value')
    ], string='Owner Expiration Notice')
    parent_contract = fields.Many2one('hr.contract', string='Parent Contract')
    payment_code = fields.Char(string='payment Code', size=50, )
    pension_mode = fields.Selection([
        ('Endorsed_Plan', 'Endorsed Plan'), ('plan_instituted', 'Plan Instituted')
    ], string='Pension Mode')
    frequency = fields.Many2one('model.periodicity', string='Frequency')
    Periodicity_Card = fields.Many2one('model.periodicity', string='Frequency of Card Renewal')
    grace_period = fields.Float(string='Grace period')
    tag = fields.Char(string='Board')
    places = fields.Text(string='Places')
    Has_dps = fields.Boolean(string='Has DPS')
    payment_deadline = fields.Float(string='Payment Term')
    Previous_Broker = fields.Many2one('broker', string='Previous Broker')
    previous_policy = fields.Many2one('hr.contract', string='Previous Policy')
    # Pricebook2Id not clear
    First_Bill = fields.Float(string='First Invoice')
    product = fields.Selection([
        ('PGBL', 'PGBL'), ('VGBL', 'VGBL')
    ], string='Product')
    project_type = fields.Selection([
        ('none', 'No Project'), ('fcdlesp', 'FCDLESP'), ('opp', 'OPP'), ('sincor', 'SINCOR'), ('facility', 'Facility'),
    ], string='Project Type')
    provider = fields.Many2one('account.account', string='Project Type')
    number_of_installments = fields.Float(string='Number of installments')
    readjustment_base_date = fields.Date(string='Readjustment Base Date')
    rebate = fields.Date(string='Rebate')
    relationship_director = fields.Many2one('res.users', string='Relationship Director')
    relationship_manager = fields.Many2one('res.users', string='Relationship Manager')
    redeemed = fields.Float(string='Redeemed')
    renavam = fields.Float(string='RENAVAM')
    # ShippingAddress not clear
    hr_site = fields.Char(string='Site Hr')
    sons_capital_limit = fields.Float(string='Sons Capital Limit')
    special_terms = fields.Text(string='Special Terms')
    # status in odoo named as state
    sub_deployed_next_to_the_contract = fields.Boolean(string='Sub Deployed Next to the Contract')
    subcontract = fields.Boolean(string='Subcontract')
    subcontract_description = fields.Text(string='Subcontract Description', size=255, )
    subcontract_number = fields.Text(string='SubContract Number', size=100, )
    administration_tax = fields.Float(string='Administration fee')
    charge_rate = fields.Float(string='Loading Fee')
    emergencial_card_fee = fields.Float(string='Emergency Card Fee')
    availability_fee = fields.Float(string='Availability Rate')
    delivery_fee = fields.Float(string='Delivery Fee')
    issuance_cost = fields.Float(string='Implementation Fee')
    renewal_fee = fields.Float(string='Renewal Fee')
    output_rate = fields.Float(string='Exit Fee')	
    replace_fee = fields.Float(string='Duplicate Fee')
    contract_type = fields.Selection([
        ('corporate_collective', 'Corporate Collective'), ('collective_by_adhesion', 'Collective by Adhesion'),
    ], string='Type of contract')
    income_type = fields.Selection([
        ('temporary_income', 'Temporary Income'), ('lifetime_income', 'Lifetime Income'), ('lifetime_income_reversible_to_the_beneficiary', 'Lifetime Income Reversible to the Beneficiary')
    ], string='Type of income')
    tax_type = fields.Selection([
        ('definitive_regressive', 'Definitive Regressive'), ('compensable_progressive ', 'Compensable Progressive')
    ], string='Type of Taxation')
    total_capital = fields.Selection([
        ('total_capital', 'Total Capital')
    ], string='Total Capital')
    brokerage_transfer = fields.Boolean(string='Brokerage Transfer')
    type_of_pension = fields.Selection([
        ('open', 'Open'), ('closed', 'Closed')
    ], string='Type of Pension')
    type_of_revenue = fields.Selection([
        ('one_off', 'One-off'), ('recurrent', 'Recurrent')
    ], string='Type of Revenue')
    type_of_subcontract = fields.Selection([
        ('active', 'Active'), ('Fired_or_Retired', 'Fired and/or Retired'), ('preliminary', 'Preliminary'), ('service_provider', 'Service provider'), ('redeemed', 'Redeemed')
    ], string='Type of Subcontract')
    Value = fields.Float(string='Value')
    provisioned_commission_amount = fields.Float(string='Value of the Provisioned Commission')
    provisioned_agency_value = fields.Float(string='Provisioned Agency Value')
    contributory_value = fields.Float(string='Value of Contributariedade')
    coverage_limit_value = fields.Float(string='Coverage Limit Value')
    purchase_limit_value = fields.Float(string='Purchase Limit Value')
    moderator_factor_value = fields.Char(string='Moderating Factor Value', size=10, )
    monthly_average_value = fields.Float(string='Average Monthly Value')
    lifes = fields.Float(string='Lives')
    which_index = fields.Char(string='Which Index?', size=100, )
    address_ids = fields.One2many('model_address', 'Contract_id', string='Address')
    contact_ids = fields.One2many('res.partner', 'contract_id', string='Contacts')
    contract_team_ids = fields.One2many('contract_team', 'contract_id', string='Contract Teams')
    user_company_contract_permissions_ids = fields.One2many('user_company_contract_permissions__c', 'contract__c', string='Contract Teams')

    contract_ids = fields.One2many('hr.contract', 'parent_contract', string='Sub Contract')
    service_ids = fields.One2many('model_service_c', 'contract_id', string='Service')
    sensus_management_ids = fields.One2many('model_sensus_management_document_c', 'Contract_id', string='Sensus Management Documents')
    readjustment_ids = fields.One2many('contract.readjust', 'Contracts', string='Readjustment')
    cost_center_ids = fields.One2many('model_cost_center', 'contract_id', string='Cost Center')
    plan_ids = fields.One2many('model_contract_plan', 'Contract_id', string='Contract Plan')
    contract_partner_ids = fields.One2many('contract.partner', 'contract_id', string='Contract Partner')
    contribution_ids = fields.One2many('contract.contribution', 'contract_id', string='Contributions')
    contract_elegibility_ids = fields.One2many('contract_eligibility', 'contract_id', string='Contract Elegibilities')
    contract_financial_ids = fields.One2many('financial_contract', 'contract_id', string='Contract Financial Data')
    checklist_ids = fields.One2many('model_checklist_c', 'Contract_id', string='Checklist')
    geographic_scope_id = fields.Many2one('model_geographic_scope', string="Geographic Scope")





