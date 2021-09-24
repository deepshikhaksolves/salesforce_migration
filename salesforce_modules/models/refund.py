from odoo import models, fields, api,_

from odoo.exceptions import ValidationError


class Refund(models.Model):
    _name = 'model_refund'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Salesforce Refund'
    _rec_name = 'Name'

    # CreatedById already in odoo
    end_date = fields.Date(string="End Date",track_visibility='onchange')
    Event_c = fields.Selection([
        ('Query', 'Elective Consultation'),
        ('query_ps', 'Emergency Room Consultation'),
        ('complex_exam', 'complex exam'),
        ('Complementary Exams A', 'Complementary Exams A'),
        ('Complementary Exams B', 'Complementary Exams B'),
        ('Group 1 exams', 'Group 1 exams'),
        ('Group 2 Exams', 'Group 2 Exams'),
        ('simple_exam', 'Simple Exam'),
        ('Physiotherapy', 'Physiotherapy'),
        ('Speech Therapy', 'Speech Therapy'),
        ('franchising_internation', 'Deductible on Hospitalization'),
        ('Nutrition', 'Nutrition'),
        ('basic_procedures', 'Basic Procedures'),
        ('special_procedures', 'Special Procedures'),
        ('Psychotherapy', 'Psychotherapy'),
        ('complex_therapy', 'Complex Therapy'),
        ('Therapies', 'Therapies'),
        ('Therapy', 'Simple Therapy'),
        ('Non-Medical Therapies', 'Non-Medical Therapies')
    ], string="Event",track_visibility='onchange')
    # LastModifiedById already in odoo
    OwnerId = fields.Many2one('res.users', string="Owner",track_visibility='onchange')
    Product_id = fields.Many2one('product.template', string="Product",track_visibility='onchange')
    Name = fields.Char(string="Refund",track_visibility='onchange')
    start_date = fields.Date(string="Start Date",track_visibility='onchange')
    value = fields.Float(string="Value",track_visibility='onchange')

