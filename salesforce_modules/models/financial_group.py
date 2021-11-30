from odoo import models, fields, api


class FinancialGroup(models.Model):
    _name = 'model_financial_group'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Financial Group"
    _rec_name = 'name'

    active = fields.Boolean('Active',track_visibility='onchange', default=True)
    approval_connection = fields.Selection(
        [('Active Beneficiary', 'Active Beneficiary'), ('Company Email', 'Company Email'), ('Manual', 'Manual')],
        'Approval Connection',track_visibility='onchange')
    company_classification = fields.Selection(
        [('Small', 'Small (up to 99 lives)'), ('Middle', 'Middle (100 to 999 lives)'),
         ('Corporate', 'Corporate (1,000 or more lives)')], 'Company Classification')
    cost_center = fields.Char('Cost Center', size=50,track_visibility='onchange')
    covid = fields.Selection([('Dont Show Covid', 'Dont Show Covid'), ('Mandatory Trail', 'Mandatory Trail'),
                              ('Mandatory CRM for positive', 'Mandatory CRM for positive'),
                              ('Mandatory CRM for negative', 'Mandatory CRM for negative'),
                              ('Mandatory certificate for positive', 'Mandatory certificate for positive'),
                              ('Mandatory certificate for negative', 'Mandatory certificate for negative')], 'Covid',track_visibility='onchange')
    # CreatedById already in odoo
    domain = fields.Char('Domain', size=255,track_visibility='onchange')

    dr_protected = fields.Boolean('Protected Dr',track_visibility='onchange')
    drive_path = fields.Char('Drive Path', size=255,track_visibility='onchange')
    I_protected = fields.Selection([('no_access', 'No access'), ('allow_holder', 'Access for Holders'),
                                    ('allow_all', 'Access for Holders and Dependents')], 'I Protected',track_visibility='onchange')
    folder_template = fields.Char('Folder Template', size=255,track_visibility='onchange')

    general_rule_group_backoffice_id = fields.Char('General Rule Group Backoffice Id', size=255,track_visibility='onchange')
    general_rule_group_company_id = fields.Char('General Rule Group Company Id', size=255,track_visibility='onchange')
    name = fields.Char('Financial Group', size=80,track_visibility='onchange')
    # LastModifiedById already in odoo
    OwnerId = fields.Many2one('res.users', string='Owner')
    profile = fields.Selection(
        [('administrator', 'administrator'), ('Financial', 'Financial'), ('Operacional', 'Operacional'),
         ('Medical Management', 'Medical Management')], 'Profile',track_visibility='onchange')
    rh_protected = fields.Boolean('HR Protected',track_visibility='onchange')
    screening_code = fields.Char('Screening Code', size=255,track_visibility='onchange')
    started = fields.Boolean('Started',track_visibility='onchange')
    storage_code = fields.Char('Storage Code', size=255,track_visibility='onchange')
    trail_code = fields.Char('Trail Code', size=255,track_visibility='onchange')

    account_ids = fields.One2many('account.account', 'financial_group_id', string='Account IDS')
    cost_center_ids = fields.One2many('model_cost_center', 'financial_group_id', string='Cost Center IDS')
    portal_access_ids = fields.One2many('portal.access', 'financial_group_id', string='Portal Access IDS')
    contract_ids =  fields.One2many('hr.contract', 'financial_group')
    financial_group_master_users_ids = fields.One2many('financial_group_master_user','financial_group_id')
    user_company_contract_permission_ids = fields.One2many('user_company_contract_permissions__c','financial_group_c')
    financial_group_doctor_ids =  fields.One2many('financial_doctor','financial_group_id')