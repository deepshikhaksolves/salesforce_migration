from odoo import models, fields, api


class OperatorDocument(models.Model):
    _name = 'operator_document'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Operator Document"
    _rec_name = 'document_id'

    checklist_carrier_id = fields.Many2one('model_operator_checklist', string='Operator Checklist')
    # CreatedById already in odoo
    document_id = fields.Many2one('ir.attachment', string='Document')
    # LastModifiedById already in odoo
    name = fields.Char(string="Carrier's Document Name")

    operator_checklist_ids = fields.One2many('model_operator_checklist', 'operator_document_id', string='Operator Document Id')

