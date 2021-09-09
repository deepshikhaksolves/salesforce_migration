from odoo import models,fields,api

class Service_Benefit_C(models.Model):
    _name = 'model_service_benefit_c'
    _description = "Salesforce Service Benefit C"
    _rec_name = 'Name'

    # CreatedById  already in odoo
    # LastModifiedById already in odoo

    Benefits = fields.Selection([('Health','Health'),('Dental','Dental'),('Life','Life'),('Medicine','Medicine'),
                                 ('Personal_Accidents','Personal_Accidents'),('In_Company','Consultancy'),
                                 ('Medical_Consulting','Medical Consulting'),('Meal','Snack'),
                                 ('Food','Food'),('Transportation','Transport'),('Pension','Pension'),
                                 ('Travel','Travel'),('Car_Fleet','Fleet'),('Car','Car'),
                                 ('Fuel','Fuel'),('Occupational_Health','Occupational_Health'),
                                 ('Checkup','Check-up'),('Vaccine','Vaccine'),('I_Protected','I_Protected'),
                                 ('Fee','Fee')],string='Benefit')
    OwnerId = fields.Many2one('res.users',string='Owner')
    service_id = fields.Many2one('model_service_c',string='Service')
    Name = fields.Text(string='Service Benefit',size=80)
