from odoo import models, fields, api

class Case_Request_SLA_C(models.Model):
    _name = 'model_case_request_sla_c'
    _description = "Salesforce Case Request SLA C"
    _rec_name = 'Name'

    # CreatedById  already in odoo
    # LastModifiedById already in odoo

    Name = fields.Char(string='Code')
    OwnerId = fields.Many2one('res.users',string='Owner')
    SLA = fields.Float(string='SALAD',digits=(5,0))
    SLA_Type = fields.Selection([('Minutes','Minutes'),('hours','hours'),('Days','Days')],string='Term Type')
