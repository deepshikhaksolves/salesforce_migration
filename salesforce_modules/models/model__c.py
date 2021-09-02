
from odoo import models, fields, api

class ModelBrand(models.Model):
    _name = 'model_brand'
    _description = "Salesforce Brand"
    _rec_name = 'name'

    name    = fields.Char('Name')


class ModelObject(models.Model):
    _name = 'model__c'
    _description = "Salesforce model object"
    _rec_name = 'Name'

    # CreatedById  already in odoo
    # LastModifiedById already in odoo
    Brand__c    = fields.Many2one('model_brand', string='Mark')
    Name        = fields.Text(string='Model')
    OwnerId     = fields.Many2one('res.users',string='Owner')
