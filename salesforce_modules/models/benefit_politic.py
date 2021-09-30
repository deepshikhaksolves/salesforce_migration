from odoo import models, fields, api


class BenefitPolitic(models.Model):
    _name = 'model_benfit_politic'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Salesforce Benefit Politice'
    _rec_name = 'Name'

    Actual_Tax = fields.Float(string="Actual Tax", track_visibility='onchange')
    Administration_Tax = fields.Float(string="Administration Tax", track_visibility='onchange')
    Contract_End = fields.Selection([
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December')
    ], string="Policy Anniversary", track_visibility='onchange')
    Availability_Fee = fields.Float(string="Availability Fee", track_visibility='onchange')
    Average_invoice = fields.Char(string="Average Invoice", track_visibility='onchange')
    Benefits = fields.Selection([
        ('Health', 'Health'),
        ('Dental', 'Dental'),
        ('Life', 'Life'),
        ('Medicine', 'Medicine'),
        ('Personal_Accidents', 'Personal Accident'),
        ('In_Company', 'Consultancy'),
        ('Medical_Consulting', 'Medical Consulting'),
        ('Meal', 'Snack'),
        ('Food', 'Food'),
        ('Transportation', 'Transport'),
        ('Pension', 'pension'),
        ('Travel', 'Travel'),
        ('Car_Fleet', 'Fleet'),
        ('Car', 'Car'),
        ('Fuel', 'Fuel'),
        ('Occupational_Health', 'Occupational_Health'),
        ('Checkup', 'Check-up'),
        ('Vaccine', 'Vaccine'),
        ('I_protected', 'I Protected'),
        ('Fee', 'Fee')
    ], string="Benefit", track_visibility='onchange', required=True)
    Brokerage_Transfer = fields.Boolean(string="Brokerage Transfer", track_visibility='onchange')
    Capital = fields.Selection([
        ('Uniform', 'Uniform'),
        ('Multiple', 'Multiple'),
        ('Staggered', 'staggered'),
        ('Free choice', 'Free choice'),
        ('Global', 'Global')
    ], string="Capital", track_visibility='onchange')
    BenefitOperadora = fields.Char(string="Carrier Benefit", track_visibility='onchange')
    Charge_Rate = fields.Float(string="Charge Rate", track_visibility='onchange')
    Comission = fields.Float(string="Comission", track_visibility='onchange')
    Competitor = fields.Many2one('broker', string="Competitor", track_visibility='onchange')
    Account_id = fields.Many2one('account.account', string="Account", track_visibility='onchange')
    Contributory = fields.Selection([
        ('By_Salary_Range', 'By Salary Range'),
        ('By_Percentage', 'By Percentage'),
        ('By_Value', 'By Value'),
        ('No_Contribution', 'No Contribution')
    ], string="Contributory", track_visibility='onchange')
    Contributory_Value = fields.Float(string="Contributory Value", track_visibility='onchange')
    Coverage_Limit_Value = fields.Float(string="Coverage Limit Value", track_visibility='onchange')
    # CreatedById already in odoo
    # LastModifiedById already in odoo
    Destination = fields.Selection([
        ('North_America', 'North America'),
        ('Central_America', 'Central America'),
        ('South_America', 'South America'),
        ('Europe', 'Europe'),
        ('Africa_Asia', 'Africa, Asia'),
        ('Asia', 'Asia'),
        ('Oceania', 'Oceania'),
        ('multiple_destinations', 'Multiple Destinations'),
        ('Brazil', 'Brazil')
    ], string="Destination", track_visibility='onchange')
    Effective_time_at_current_carrier = fields.Float(string="Effective time at current carrier", track_visibility='onchange')
    Monthly_Bill = fields.Float(string="Monthly Invoice", track_visibility='onchange')
    Funeral_Assistance = fields.Boolean(string="Funeral Assistance", track_visibility='onchange')
    Funeral_Assistance_Value = fields.Float(string="Funeral Assistance Value", track_visibility='onchange')
    Offer = fields.Boolean(string="Generate opportunity?", track_visibility='onchange')
    Grace_Period = fields.Float(string="Grace Period", track_visibility='onchange')
    Use_Product = fields.Boolean(string="Has Benefit?", track_visibility='onchange')
    has_Checkup = fields.Boolean(string="Has Checkup?", track_visibility='onchange')
    Income_Type = fields.Selection([
        ('Temporary_Income', 'Temporary Income'),
        ('Lifetime Income', 'Lifetime Income'),
        ('Life_Income_Reversible_to_the_Beneficiary', 'Life Income Reversible to the Beneficiary')
    ], string="Income Type", track_visibility='onchange')
    Lead_id = fields.Many2one('crm.lead', string="Lead", track_visibility='onchange')
    Max_Capital_Limit = fields.Float(string="Max Capital Limit", track_visibility='onchange')
    Min_Capital_Limit = fields.Float(string="Min Capital Limit", track_visibility='onchange')
    Payment_Method = fields.Selection([
        ('pre_payment', 'Pre Payment'),
        ('post_payment', 'Post Payment')
    ], string="Payment Method", track_visibility='onchange')
    Moderator_Variable = fields.Selection([
        ('No_Moderating_Factor', 'No Moderating Factor'),
        ('Co_participation_Reverted_Company', 'Reverted to Company'),
        ('Co_participation_Reverted_to_Operator', 'Reverted to Operator')
    ], string="Moderator Variable", track_visibility='onchange')
    Moderator_Variable_Value = fields.Float(string="Moderator Variable Value", track_visibility='onchange')
    Monthly_Average_Value = fields.Float(string="Monthly Average Value", track_visibility='onchange')
    Number_of_Installments = fields.Float(string="Number of Installments", track_visibility='onchange')
    How_c = fields.Char(string="Observation", size=255, track_visibility='onchange')
    carrier_2_id = fields.Many2one('account.account', string="Operator", track_visibility='onchange')
    Output_Rate = fields.Float(string="Output Rate", track_visibility='onchange')
    OwnerId = fields.Many2one('res.users', string='Owner', track_visibility='onchange')
    Pension_Mode = fields.Selection([
        ('Plano_Averbado', 'Plano Averbado'),
        ('Instituted_Plan', 'Instituted Plan')
    ], string="Pension Mode", track_visibility='onchange')
    Places = fields.Char(string="Places", size=32768, track_visibility='onchange')
    Name = fields.Char(string="Benefit Politic", size=80, track_visibility='onchange', required=True)
    Provider_id = fields.Many2one('account.account', string="Provider", track_visibility='onchange')
    Purchase_Limit = fields.Selection([
        ('Fixed_value', 'Fixed value'),
        ('Salary_Percentage', 'Salary Percentage')
    ], string="Purchase Limit", track_visibility='onchange')
    Purchase_Limit_Value = fields.Float(string="Purchase Limit Value", track_visibility='onchange')
    Revenue = fields.Char(string="Revenue", track_visibility='onchange')
    Performing_Index = fields.Float(string="loss ratio", track_visibility='onchange')
    Sons_Capital_Limit = fields.Float(string="Sons Capital Limit", track_visibility='onchange')
    Tax_Type = fields.Selection([
        ('Definitive_Regressive', 'Definitive Regressive'),
        ('Compensable_Progressive', 'Compensable Progressive')
    ], string="Tax Type", track_visibility='onchange')
    Contract_Type = fields.Selection([
        ('Self_Management', 'Self Management'),
        ('Individual', 'Individual'),
        ('Subcontract', 'Subcontract')
    ], string="Type of contract", track_visibility='onchange')
    Total_Capital = fields.Float(string="Total Capital", track_visibility='onchange')
    Type_of_Pension = fields.Selection([
        ('Open', 'Open'),
        ('Closed', 'Closed')
    ], string="Type of Pension", track_visibility='onchange')
    Type_of_Revenue = fields.Selection([
        ('One_off', 'One-off'),
        ('Recurrent', 'Recurrent')
    ], string="Type of Revenue", track_visibility='onchange')
    Life = fields.Float(string="Lives", track_visibility='onchange')

    lead_id = fields.Many2one('crm.lead', string='Lead Id', track_visibility='onchange')

    contract_plan_ids = fields.One2many('model_contract_plan','benifit_politic_id', string='Contract Plan IDS')
    politic_bill_ids = fields.One2many('politic.bill','benefit_politic_id', string='Contracted Plan')
