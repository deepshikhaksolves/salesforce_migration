from odoo import models, fields, api

class Salesforce_Dim_Beneficiario_X(models.Model):
    _name = 'model_salesforce_dim_beneficiario_x'
    _description = "Salesforce Salesforce Dim Beneficiario X"
    _rec_name = 'ExternalId'

    DisplayUrl = fields.Char(string='Display URL')
    ExternalId = fields.Char(string='External ID')
    beneficiary_id = fields.Float(string='beneficiary_id',digits=(18,0))
    birth = fields.Text(size=100,string='birth')
    beneficiary_name = fields.Text(string='payee name',size=1000)
    ownername = fields.Text(string='Title Holder',size=1000)
    sex = fields.Text(string='sex',size=100)
    beneficiary_type = fields.Text(string='Beneficiary Type',size=1000)
