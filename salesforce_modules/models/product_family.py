from odoo import models, fields, api

class ProductFamily(models.Model):
    _name = 'product_family'
    _description = "Salesforce Product Family"
    _rec_name = 'Name'

    benefit__c    = fields.Selection([('Health','Saúde'),('Dental','Odontológico'),('Life','Vida'),('Medicine','Medicamento'),('Personal_Accidents','Acidente Pessoal'),('In_Company','Consultoria'),('Medical_Consulting','Consultoria Médica'),('Meal','Refeição'),('Food','Alimentação'),('Transportation','Transporte'),('Pension','Previdência'),('Travel','Viagem'),('Car_Fleet','Frota'),('Car','Automóvel'),('Fuel','Combustível'),('Occupational_Health','Saúde Ocupacional'),('Checkup','Check-up'),('Vaccine','Vacina'),('eu_protegido','Eu Protegido'),('Fee','Fee')],'Benefit')
    # CreatedById  already in odoo
    # LastModifiedById  already in odoo
    Name                    = fields.Char('Name',size=80)

    # carrier__c              = 
