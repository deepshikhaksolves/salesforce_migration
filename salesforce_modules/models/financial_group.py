from odoo import models, fields, api


class FinancialGroup(models.Model):
    _name = 'model_financial_group'
    _description = "Salesforce Financial Group"
    _rec_name = 'name'


    active                  = fields.Boolean('Active')
    approval_connection     = fields.Selection([('Active Beneficiary','Active Beneficiary'),('Company Email','Company Email'),('Manual','Manual')],'Approval Connection')
    company_classification  = fields.Selection([('Small','Small (up to 99 lives)'),('Middle','Middle (100 to 999 lives)'),('Corporate','Corporate (1,000 or more lives)')],'Company Classification')
    cost_center             = fields.Char('Cost Center', size=50)
    covid                   = fields.Selection([('Dont Show Covid','Dont Show Covid'),('Mandatory Trail','Mandatory Trail'),('Mandatory CRM for positive','Mandatory CRM for positive'),('Mandatory CRM for negative','Mandatory CRM for negative'),('Mandatory certificate for positive','Mandatory certificate for positive'),('Mandatory certificate for negative','Mandatory certificate for negative')],'Covid')
    # CreatedById already in odoo
    domain                  = fields.Char('Domain', size=255)

    dr_protected            = fields.Boolean('Protected Dr')
    drive_path              = fields.Char('Drive Path', size=255)
    I_protected             = fields.Selection([('no_access','No access'),('allow_holder','Access for Holders'),('allow_all','Access for Holders and Dependents')],'I Protected')
    folder_template         = fields.Char('Folder Template', size=255)

    general_rule_group_backoffice_id      = fields.Char('General Rule Group Backoffice Id', size=255)
    general_rule_group_company_id         = fields.Char('General Rule Group Company Id', size=255)
    name                                  = fields.Char('Financial Group', size=80)
    # LastModifiedById already in odoo
    OwnerId                               = fields.Many2one('res.users',string='Owner')
    profile                 = fields.Selection([('administrator','administrator'),('Financial','Financial'),('Operacional','Operacional'),('Medical Management','Medical Management')],'Profile')
    rh_protected            = fields.Boolean('HR Protected')
    screening_code          = fields.Char('Screening Code', size=255)
    started                 = fields.Boolean('Started')
    storage_code            = fields.Char('Storage Code', size=255)
    trail_code              = fields.Char('Trail Code', size=255)
    
    account_ids             = fields.One2many('account.account', 'financial_group_id', string='Account IDS')
    cost_center_ids         = fields.One2many('model_cost_center', 'financial_group_id', string='Cost Center IDS')
    portal_access_ids       = fields.One2many('portal.access', 'financial_group_id', string='Portal Access IDS')