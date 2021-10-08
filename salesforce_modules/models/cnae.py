from odoo import models, fields, api


class CNAE(models.Model):
    _name = 'model_cnae'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce CNAE"
    _rec_name = 'Code'

    Code = fields.Char('Name', size=80)
    # CreatedById  already in odoo
    Description__c = fields.Char('Description', size=255)
    # LastModifiedById already in odoo
    OwnerId = fields.Many2one('res.users', string='Owner')
    Parent_Code__c = fields.Many2one('model_cnae', string='Parent Code')
    Risk_Level__c = fields.Selection([('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], 'Risk Level')
