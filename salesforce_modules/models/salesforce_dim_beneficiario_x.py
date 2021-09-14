from odoo import models, fields, api

class Salesforce_Dim_Beneficiario_X(models.Model):
    _name = 'model_salesforce_dim_beneficiario_x'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Salesforce Dim Beneficiario X"
    _rec_name = 'beneficiary_name'

    DisplayUrl = fields.Char(string='Display URL',size=1000)
    ExternalId = fields.Char(string='External ID')
    beneficiary_id = fields.Float(string='beneficiary_id',digits=(18,0))
    birth = fields.Text(size=100,string='birth')
    beneficiary_name = fields.Char(string='payee name',size=1000)
    ownername = fields.Char(string='Title Holder',size=1000)
    sex = fields.Char(string='sex',size=100)
    beneficiary_type = fields.Char(string='Beneficiary Type',size=1000)
