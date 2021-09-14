from odoo import models, fields, api

class Subject_C(models.Model):
    _name ="model_subject_c"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Subject C"
    _rec_name = 'Name'

    # CreatedById already in odoo
    # LastModifiedById already in odoo

    Name = fields.Char(string='Name', size=80)
    OwnerId = fields.Many2one('res.users', string='Owner')
    Status =  fields.Selection([('Open','Open'),('In Progress','In Progress'),('Closed','Closed'),('Called Off','Called Off')], string='Status')