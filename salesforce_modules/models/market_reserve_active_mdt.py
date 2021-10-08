from odoo import models, fields, api

class Market_Reserve_Active_MDT(models.Model):
    _name = 'model_market_reserve_active_mdt'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Market Reserve Active MDT"
    _rec_name = 'DeveloperName'

    # CreatedById  already in odoo
    # LastModifiedById already in odoo

    DeveloperName = fields.Char(string='Custom Metadata Record Name',size=40,track_visibility='onchange')
    MasterLabel = fields.Char(string='Label', size=40,track_visibility='onchange')
    NamespacePrefix = fields.Text(string='Namespace Prefix',track_visibility='onchange')
    IsProtected = fields.Boolean(string='Protected Component',track_visibility='onchange')
    isActive = fields.Boolean(string='isActive',track_visibility='onchange')
