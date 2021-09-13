from odoo import models, fields, api

class ContractCopayment(models.Model):
    _name = 'contract.copayment'

    name = fields.Char(string='Contract Copayment')
    contract = fields.Many2one('hr.contract', string='Contract')
    # CreatedById created by default
    # LastModifiedById created by default
    limit = fields.Float(string='Limit')
    owner_id = fields.Many2one('res.users', string='Owner')
    # Plan = fields.Many2one('comodel_name', string='') contract plan
    type_of_procedures = fields.Selection([
        ('consultation', 'Elective Consultation'), ('consultation_ps', 'Emergency Room Consultation'), ('exam_complex', 'Complex Exam'), ('complementary_Exams_a', 'Complementary Exams A'), ('Complementary Exams B', 'complementary_exams_b'), ('exams_group_1', 'Exams Group 1'), ('exams_group_2', 'Exams Group 2 '), ('simple_exam', 'Simple exam'), ('physiotherapy', 'Physiotherapy'), ('speech_therapy', 'Speech Therapy'),('franchise_internacao', 'Franchise in Hospitalization'), ('nutrition', 'nutrition'), ('basic_procedures', 'Basic Procedures'), ('special_procedures', 'Special Procedures'), ('psychotherapy', 'psychotherapy'), ('therapy_complex', 'Complex Therapy'), ('therapies', 'Therapies'), ('therapy', 'Simple Therapy'), ('non_medical_therapies', 'Non-Medical Therapies')
    ], string='Type of Procedures')
    value_Type = fields.Selection([
        ('fixed', 'Fixed'), ('percentage', 'Percentage')
    ], string='Value Type')
    value = fields.Float(string='Value')