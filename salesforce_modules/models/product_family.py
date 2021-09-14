from odoo import models, fields, api

class ProductFamily(models.Model):
    _name = 'product_family'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Product Family"
    _rec_name = 'Name'

    benefit__c = fields.Selection([('Health','Saúde'),('Dental','Odontológico'),('Life','Vida'),('Medicine','Medicamento'),('Personal_Accidents','Acidente Pessoal'),('In_Company','Consultoria'),('Medical_Consulting','Consultoria Médica'),('Meal','Refeição'),('Food','Alimentação'),('Transportation','Transporte'),('Pension','Previdência'),('Travel','Viagem'),('Car_Fleet','Frota'),('Car','Automóvel'),('Fuel','Combustível'),('Occupational_Health','Saúde Ocupacional'),('Checkup','Check-up'),('Vaccine','Vacina'),('eu_protegido','Eu Protegido'),('Fee','Fee')],'Benefit')
    # CreatedById  already in odoo
    # LastModifiedById  already in odoo
    Name = fields.Char('Name',size=80)

    carrier__c = fields.Many2many(string='Operator', comodel_name='account.account', relation='carrier_account_rel')

    account_id = fields.Many2one('account.account', string='Account Id')
    product_ids = fields.One2many('product.template', 'product_family_id', string='Product Family IDS')
