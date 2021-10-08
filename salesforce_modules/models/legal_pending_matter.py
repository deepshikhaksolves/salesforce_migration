from odoo import models, fields, api


class LegalPendingMatter(models.Model):
    _name = 'model_legal_pending_matter'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Legal Pending Matter"
    _rec_name = 'Name'

    active = fields.Boolean(string="Active",track_visibility='onchange')
    contract_id = fields.Many2one('hr.contract', string="Contract",track_visibility='onchange')
    # CreatedById already in odoo
    # LastModifiedById already in odoo
    lawsuit_number = fields.Char(string="Lawsuit Number", size=255,track_visibility='onchange')
    lawsuit_source = fields.Selection([
        ('Client', 'Client'),
        ('Broker', 'Broker'),
        ('Operator', 'Operator')
    ], string="Lawsuit Source",track_visibility='onchange')
    Name = fields.Char(string="Legal pending number",track_visibility='onchange')
    observation = fields.Char(string="Observation", size=32768,track_visibility='onchange')
    OwnerId = fields.Many2one('res.users', string="Owner",track_visibility='onchange')
    subcontract_id = fields.Many2one('hr.contract', string="Subcontract",track_visibility='onchange')
    attachment_ids = fields.One2many('ir.attachment', 'legal_pending_matter_id', string="Attachment IDS")
