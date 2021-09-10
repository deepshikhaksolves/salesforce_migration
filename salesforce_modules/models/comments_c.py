from odoo import models, fields, api

class Comments_C(models.Model):
    _name = 'model_comments_c'
    _description = "Salesforce Comments C"
    _rec_name = 'Name'

    # CreatedById  already in odoo
    # LastModifiedById already in odoo

    Case_id = fields.Many2one('model_case',string='Case')
    How = fields.Text(string='Comment')
    OwnerId = fields.Many2one('res.users')
    RecordTypeId = fields.Many2one('record_type', string='Record Type')
    Type = fields.Selection([('Internal Comment','Internal Comment'),('Customer follow-up','Customer follow-up'),
                             ('Solution','Solution'),('Customer Comment','Customer Comment')],
                            string='Guy')
    Name = fields.Char(string='Qualification',size=80)
