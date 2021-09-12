
from odoo import models, fields, api

class ModelBrand(models.Model):
    _name = 'model_brand'
    _description = "Salesforce Brand"
    _rec_name = 'name'

    name    = fields.Char('Name')


class ModelObject(models.Model):
    _inherit = 'ir.model'
    _description = "Salesforce model object"

    # CreatedById  already in odoo
    # LastModifiedById already in odoo
    Brand__c    = fields.Many2one('model_brand', string='Mark')
    # Name        already in odoo i.e. (name)
    OwnerId     = fields.Many2one('res.users',string='Owner')
    fleet_ids   = fields.One2many('model_car_fleet_c', 'Model_id', string='Fleet IDS')
    opportunity_ids = fields.One2many('crm.lead', 'model_id', string='Opportunity IDS')