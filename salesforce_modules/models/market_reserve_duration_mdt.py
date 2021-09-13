from odoo import models, fields, api

class Market_Reserve_Duration_MDT(models.Model):
    _name = 'model_market_reserve_duration_mdt'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Market Reserve Duration MDT"
    _rec_name = 'DeveloperName'

    # CreatedById  already in odoo
    # LastModifiedById already in odoo

    DeveloperName = fields.Char(string='Custom Metadata Record Name',size=40)
    MasterLabel = fields.Char(string='Label', size=40)
    NamespacePrefix = fields.Text(string='Namespace Prefix')
    IsProtected = fields.Boolean(string='Protected Component')
    Duration = fields.Float(string='Duration',digits=(18,0))
