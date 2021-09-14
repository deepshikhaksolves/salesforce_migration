from odoo import models, fields, api

class contractCoverage(models.Model):
    _name = 'contract.coverage'

    coverage = fields.Selection([
        ('consultation', 'Consultation'),('exam', 'exam'),('emergency_room', 'Emergency Room'),('Clinical_and_surgical_admission', 'Clinical and surgical admission'),('crisis_psychotherapy_(up_to_40_sessions/year)', 'Crisis Psychotherapy (up to 40 sessions/year)'),('myopia_surgery_from_5_degrees', 'Myopia Surgery From 5 Degrees'),('nutritionist_(up_to_12_appointments/year', 'Nutritionist (up to 12 appointments/year'),('occupational_therapy_(up_to_40_appointments/year)', 'Occupational therapy (up to 40 appointments/year)'),('speech_therapy_(up_to_24_consultations/year)', 'Speech Therapy (up to 24 consultations/year) '),('corneal_kidney_and_bone_marrow_transplantation', 'Corneal, kidney and bone marrow transplantation'),('transplants', 'Transplants'),('myopia_surgery', 'myopia surgery'),('remission_by_incumbent_death', 'Remission by incumbent death'),('repayment_term', 'Repayment Term'),('rear_team', 'Rear team'),('vaccines', 'Vaccines'),('travel_assistance', 'Travel Assistance'),('check_up', 'Check up'),('card_validity_and_cost', 'Card validity and cost'),('revaluation_period', 'Rrevaluation Period'),('type_of_hiring', 'Type of hiring'),('services_provided', 'Services Provided'),('prior_authorization', 'Prior authorization'),('loss_analysis', 'loss analysis'),('contract_term', 'Contract term'),('card_cost', ''),('shortages', 'Shortages'),('dependents', 'Dependents'),('work_accident', 'work accident'),('service_network', 'service network'),
    ], string='Coverage')
    condition = fields.Char(string='Condition', size=255, )
    contracts = fields.Many2one('hr.contract', string='Contracts')
    # CreatedById created by default
    additive_end = fields.Date(string='End of Additive')
    # id created default
    additive_start = fields.Date(string='Start of the Additive')
    # LastModifiedById created default
    owner_id = fields.Many2one('res.users', string='Owner')
    contract_plan = fields.Many2one('model_contract_plan', string='Contract Plan')
    record_type_id = fields.Char(string='Record Type')