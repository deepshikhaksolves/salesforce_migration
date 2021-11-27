from odoo import models, fields, api


class OperatorChecklist(models.Model):
    _name = 'model_operator_checklist'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Operator Checklist"
    _rec_name = 'Name'

    # CreatedById already in odoo
    # LastModifiedById already in odoo


    name = fields.Char('Operator Checklist Name', size=80, track_visibility='onchange')
    operator_c = fields.Many2one('account.account', string='Operator',track_visibility='onchange')
    operator_document_id = fields.Many2one('operator_document', string='Operator Document',track_visibility='onchange')
