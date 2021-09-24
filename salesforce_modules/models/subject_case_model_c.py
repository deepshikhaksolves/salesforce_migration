from odoo import models,fields,api

class Subject_Case_Model_C(models.Model):
    _name = 'model_subject_case_model_c'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Subject Case Model C"
    _rec_name = 'Name'

    # CreatedById  already in odoo
    # LastModifiedById already in odoo

    Subject_id = fields.Many2one('model_subject_c',string='Subject',track_visibility='onchange')
    Name = fields.Char(string='Code',track_visibility='onchange')
    Case_Model_id = fields.Many2one('model_service_c',string='Service Model',track_visibility='onchange')
    OwnerId = fields.Many2one('res.users',string='Owner',track_visibility='onchange')
