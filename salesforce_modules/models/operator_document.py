from odoo import models, fields, api


class OperatorDocument(models.Model):
    _name = 'operator_document'
    _description = "Salesforce Operator Document"
    _rec_name = 'document_id'

    checklist_carrier_id    = fields.Many2one('model_operator_checklist', string='Operator Checklist')
    # CreatedById already in odoo
    document_id             = fields.Many2one('ir.attachment', string='Document')
    # LastModifiedById already in odoo
    name                    = fields.Char(string="Carrier's Document Name")
