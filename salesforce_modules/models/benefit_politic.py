from odoo import models, fields, api


class BenefitPolitic(models.Model):
    _name = 'model_benfit_politic'
    _description = 'Salesforce Benefit Politice'
    _rec_name = 'Name'

    Actual_Tax = fields.Float(string="Actual Tax", digits=(16, 2))
    Administration_Tax =  fields.Float(string="Administration Tax", digits=(3, 2))
    Contract_End =  fields.Selection([
        ('January', 'January'),
        ('February','February'),
        ('March','March'),
        ('April','April'),
        ('May','May'),
        ('June','June'),
        ('July','July'),
        ('August','August'),
        ('September','September'),
        ('October','October'),
        ('November','November'),
        ('December','December')
    ], string="Policy Anniversary")
    Availability_Fee =  fields.Float(string="Availability Fee", digits=(3, 2))
    Average_invoice =  fields.Char(string="Average Invoice")
    Benefits = fields.Selection([
        ('Health', 'Health'),
        ('Dental', 'Dental'),
        ('Life','Life'),
        ('Medicine','Medicine'),
        ('Personal_Accidents','Personal Accident'),
        ('In_Company','Consultancy'),
        ('Medical_Consulting','Medical Consulting'),
        ('Meal','Snack'),
        ('Food','Food'),
        ('Transportation','Transport'),
        ('Pension','pension'),
        ('Travel','Travel'),
        ('Car_Fleet','Fleet'),
        ('Car','Car'),
        ('Fuel','Fuel'),
        ('Occupational_Health','Occupational_Health'),
        ('Checkup','Check-up'),
        ('Vaccine','Vaccine'),
        ('I_protected','I Protected'),
        ('Fee','Fee')
    ], string="Benefit")
    Brokerage_Transfer = fields.Boolean(string="Brokerage Transfer")
    Capital =  fields.Selection([
        ('Uniform','Uniform'),
        ('Multiple','Multiple'),
        ('Staggered','staggered'),
        ('Free choice','Free choice'),
        ('Global','Global')
    ],string="Capital")
    BenefitOperadora = fields.Char(string="Carrier Benefit")
    Charge_Rate = fields.Float(string="Charge Rate", digits=(3, 2))
    Comission = fields.Float(string="Comission", digits=(3, 2))
    # Competitor = fields.Many2one('Corretora', string="Competitor") #Model Not Found
    Account_id = fields.Many2one('account.account',string="Account")
    Contributory =  fields.Selection([
        ('By_Salary_Range', 'By Salary Range'),
        ('By_Percentage','By Percentage'),
        ('By_Value','By Value'),
        ('No_Contribution','No Contribution')
    ],string="Contributory")
    Contributory_Value = fields.Float(string="Contributory Value", digits=(5, 2))
    Coverage_Limit_Value = fields.Float(string="Coverage Limit Value", digits=(5, 2))
    # CreatedById already in odoo
    # LastModifiedById already in odoo
    Destination = fields.Selection([
        ('North_America','North America'),
        ('Central_America','Central America'),
        ('South_America','South America'),
        ('Europe','Europe'),
        ('Africa_Asia','Africa, Asia'),
        ('Asia','Asia'),
        ('Oceania','Oceania'),
        ('multiple_destinations','Multiple Destinations'),
        ('Brazil','Brazil')
    ],string="Destination")
    Effective_time_at_current_carrier = fields.Float(string="Effective time at current carrier", digits=(3, 0))
    Monthly_Bill = fields.Float(string="Monthly Invoice", digits=(16, 2))
    Funeral_Assistance = fields.Boolean(string="Funeral Assistance")
    Funeral_Assistance_Value = fields.Float(string="Funeral Assistance Value", digits=(16, 2))
    Offer = fields.Boolean(string="Generate opportunity?")
    Grace_Period = fields.Float(string="Grace Period", digits=(18, 0))
    Use_Product =  fields.Boolean(string="Has Benefit?")
    has_Checkup = fields.Boolean(string="Has Checkup?")
    Income_Type = fields.Selection([
        ('Temporary_Income','Temporary Income'),
        ('Lifetime Income','Lifetime Income'),
        ('Life_Income_Reversible_to_the_Beneficiary','Life Income Reversible to the Beneficiary')
    ],string="Income Type")
    Lead_id = fields.Many2one('crm.lead', string="Lead")
    Max_Capital_Limit = fields.Float(string="Max Capital Limit", digits=(16, 0))
    Min_Capital_Limit =  fields.Float(string="Min Capital Limit", digits=(16, 0))
    Payment_Method = fields.Selection([
        ('pre_payment','Pre Payment'),
        ('post_payment','Post Payment')
    ],string="Payment Method")
    Moderator_Variable = fields.Selection([
        ('No_Moderating_Factor', 'No Moderating Factor'),
        ('Co_participation_Reverted_Company','Reverted to Company'),
        ('Co_participation_Reverted_to_Operator','Reverted to Operator')
    ],string="Moderator Variable")
    Moderator_Variable_Value = fields.Float(string="Moderator Variable Value", digits=(5, 0))
    Monthly_Average_Value = fields.Float(string="Monthly Average Value", digits=(4, 2))
    Number_of_Installments = fields.Float(string="Number of Installments", digits=(3, 0))
    How_c = fields.Char(string="Observation", size=255)
    carrier_2_id = fields.Many2one('account.account',string="Operator")
    Output_Rate = fields.Float(string="Output Rate",digits=(3, 0))
    OwnerId = fields.Many2one('res.users', string='Owner')
    Pension_Mode = fields.Selection([
        ('Plano_Averbado','Plano Averbado'),
        ('Instituted_Plan','Instituted Plan')
    ],string="Pension Mode")
    Places = fields.Char(string="Places",size=32768)
    Name = fields.Char(string="Benefit Policy", size=80)
    Provider_id = fields.Many2one('account.account', string="Provider")
    Purchase_Limit = fields.Selection([
        ('Fixed_value','Fixed value'),
        ('Salary_Percentage','Salary Percentage')
    ],string="Purchase Limit")
    Purchase_Limit_Value = fields.Float(string="Purchase Limit Value", digits=(5, 2))
    Revenue = fields.Char(string="Revenue")
    Performing_Index = fields.Float(string="loss ratio", digits=(16, 2))
    Sons_Capital_Limit = fields.Float(string="Sons Capital Limit", digits=(16, 2))
    Tax_Type = fields.Selection([
        ('Definitive_Regressive','Definitive Regressive'),
        ('Compensable_Progressive','Compensable Progressive')
    ],string="Tax Type")
    Contract_Type = fields.Selection([
        ('Self_Management','Self Management'),
        ('Individual','Individual'),
        ('Subcontract','Subcontract')
    ],string="Type of contract")
    Total_Capital = fields.Float(string="Total Capital", digits=(16, 2))
    Type_of_Pension = fields.Selection([
        ('Open','Open'),
        ('Closed','Closed')
    ],string="Type of Pension")
    Type_of_Revenue = fields.Selection([
        ('One_off','One-off'),
        ('Recurrent','Recurrent')
    ],string="Type of Revenue")
    Life =fields.Float(string="Lives", digits=(18, 0))

    lead_id = fields.Many2one('crm.lead', string='Lead Id')