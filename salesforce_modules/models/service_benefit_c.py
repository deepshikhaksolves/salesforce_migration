from odoo import models,fields,api

class Service_Benefit_C(models.Model):
    _name = 'model_service_benefit_c'
    _inherit = ['mail.thread', 'mail.activity.mixin']
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
                                 ('Fee','Fee')],string='Benefit',track_visibility='onchange')
    OwnerId = fields.Many2one('res.users',string='Owner',track_visibility='onchange')
    service_id = fields.Many2one('model_service_c',string='Service',track_visibility='onchange')
    Name = fields.Char(string='Service Benefit',size=80,track_visibility='onchange')
