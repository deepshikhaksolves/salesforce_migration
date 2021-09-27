from odoo import models, fields, api


class Pathology_Account_C(models.Model):
    _name = 'model_pathology_account_c'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Pathology Account C"
    _rec_name = 'Name'

    account_id = fields.Many2one('account.account', string='Account',track_visibility='onchange')
    # CreatedById already in odoo
    pathology_start_date = fields.Date(string='Date Onset of the Pathology',track_visibility='onchange')
    # LastModifiedById already in odoo
    Name = fields.Char(string='Pathology Name Account', size=80,track_visibility='onchange')
    OwnerId = fields.Many2one('res.users', string='Owner',track_visibility='onchange')
    pathology_id = fields.Many2one('model_pathology', string='Pathology',track_visibility='onchange')
