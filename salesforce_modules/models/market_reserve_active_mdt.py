from odoo import models, fields, api

class Market_Reserve_Active_MDT(models.Model):
    _name = 'model_market_reserve_active_mdt'
    _description = "Salesforce Market Reserve Active MDT"
    _rec_name = 'DeveloperName'

    # CreatedById  already in odoo
    # LastModifiedById already in odoo

    DeveloperName = fields.Text(string='Custom Metadata Record Name',size=40)
    MasterLabel = fields.Text(string='Label', size=40)
    NamespacePrefix = fields.Text(string='Namespace Prefix')
    IsProtected = fields.Boolean(string='Protected Component')
    isActive = fields.Boolean(string='isActive')
