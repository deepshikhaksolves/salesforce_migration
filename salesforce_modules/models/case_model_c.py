from odoo import models, fields, api

class Case_Model_C(models.Model):
    _name = 'model_case_model_c'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Case Model C"
    _rec_name = 'Name'

    # CreatedById  already in odoo
    # LastModifiedById already in odoo

    Name = fields.Char(string="Name",size=80)
    OwnerId = fields.Many2one('res.users',string='Owner')
    Status_Case_Model = fields.Selection([('Active','Active'),('Called off','Called off')],string='Status')