from odoo import models, fields, api


class Pathology(models.Model):
    _name = 'model_pathology'
    _description = "Salesforce Pathology"
    _rec_name = 'Name'

    # CreatedById  already in odoo
    Name        = fields.Char(string='Description', size=80)
    # LastModifiedById already in odoo
    OwnerId     = fields.Many2one('res.users',string='Owner')
