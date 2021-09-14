from odoo import models, fields, api


class FinancialContract(models.Model):
    _name = 'financial_contract'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Financial Contract"
    _rec_name = 'name'


    Ag  = fields.Boolean('Ag')
    approval  = fields.Boolean('Approval')
    approval_icon = fields.Char('Approval')
    contract_id   = fields.Many2one('hr.contract', string='Contract')
    # CreatedById already in odoo
    End_Date    = fields.Date('End Date')
    name        = fields.Char('Financial Contract')
    # LastModifiedById already in odoo
    OwnerId     = fields.Many2one('res.users',string='Owner')
    Start_Date  = fields.Date('Start Date')   

    Type_of_Revenue = fields.Selection([('agency','Agency (%)'),('Commission','Commission (%)'),('Consultancy','Consultancy')],'Type of Revenue')

    Value       = fields.Float(string='Value',digits=(16,2))
    attachment_ids    = fields.One2many('ir.attachment', 'financial_contract_id', 'Attachment IDS')
