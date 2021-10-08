from odoo import models, fields, api


class Salesforce_Dim_Beneficiario_X(models.Model):
    _name = 'model_salesforce_dim_beneficiario_x'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Salesforce Dim Beneficiario X"
    _rec_name = 'beneficiary_name'

    DisplayUrl = fields.Char(string='Display URL',size=1000,track_visibility='onchange')
    ExternalId = fields.Char(string='External ID',track_visibility='onchange')
    beneficiary_id = fields.Float(string='beneficiary_id',digits=(18,0),track_visibility='onchange')
    birth = fields.Text(size=100,string='birth',track_visibility='onchange')
    beneficiary_name = fields.Char(string='payee name',size=1000,track_visibility='onchange')
    ownername = fields.Char(string='Title Holder',size=1000,track_visibility='onchange')
    sex = fields.Char(string='sex',size=100,track_visibility='onchange')
    beneficiary_type = fields.Char(string='Beneficiary Type',size=1000,track_visibility='onchange')


