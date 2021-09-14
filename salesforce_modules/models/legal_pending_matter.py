from odoo import models, fields, api


class LegalPendingMatter(models.Model):
    _name = 'model_legal_pending_matter'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Legal Pending Matter"
    _rec_name = 'Name'

    active = fields.Boolean(string="Active")
    contract_id = fields.Many2one('hr.contract', string="Contract")
    # CreatedById already in odoo
    # LastModifiedById already in odoo
    lawsuit_number = fields.Char(string="Lawsuit Number", size=255)
    lawsuit_source = fields.Selection([
        ('Client', 'Client'),
        ('Broker', 'Broker'),
        ('Operator', 'Operator')
    ], string="Lawsuit Source")
    Name = fields.Char(string="Legal pending number")
    observation = fields.Char(string="Observation", size=32768)
    OwnerId = fields.Many2one('res.users', string="Owner")
    subcontract_id = fields.Many2one('hr.contract', string="Subcontract")
    attachment_ids = fields.One2many('ir.attachment', 'legal_panding_matter_id', string="Attachment IDS")
