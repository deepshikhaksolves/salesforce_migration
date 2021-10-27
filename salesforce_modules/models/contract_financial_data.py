from odoo import models, fields, api


class FinancialContract(models.Model):
    _name = 'financial_contract'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Financial Contract"
    _rec_name = 'name'

    Ag = fields.Boolean('Ag', track_visibility='onchange')
    approval = fields.Boolean('Approval', track_visibility='onchange')
    approval_icon = fields.Char('Approval', track_visibility='onchange')
    contract_id = fields.Many2one('hr.contract', string='Contract')
    # CreatedById already in odoo
    End_Date = fields.Date('End Date', track_visibility='onchange')
    name = fields.Char('Financial Contract', track_visibility='onchange')
    # LastModifiedById already in odoo
    OwnerId = fields.Many2one('res.users', string='Owner', track_visibility='onchange')
    Start_Date = fields.Date('Start Date', track_visibility='onchange')

    Type_of_Revenue = fields.Selection(
        [('agency', 'Agency (%)'), ('Commission', 'Commission (%)'), ('Consultancy', 'Consultancy')], 'Type of Revenue',
        track_visibility='onchange')

    Value = fields.Float(string='Value', digits=(16, 2), track_visibility='onchange')
    attachment_ids = fields.One2many('ir.attachment', 'financial_contract_id', 'Attachment IDS')
