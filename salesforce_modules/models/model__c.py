from odoo import models, fields, api


class ModelBrand(models.Model):
    _name = 'model_brand'
    _description = "Salesforce Brand"
    _rec_name = 'name'

    name = fields.Char('Name')


class ModelObject(models.Model):
    _name = 'ir.model'
    _inherit = ['ir.model', 'mail.thread', 'mail.activity.mixin']
    _description = "Salesforce model object"

    # CreatedById  already in odoo
    # LastModifiedById already in odoo
    Brand__c = fields.Many2one('model_brand', string='Mark',track_visibility='onchange')
    # Name        already in odoo i.e. (name)
    OwnerId = fields.Many2one('res.users', string='Owner',track_visibility='onchange')
    fleet_ids = fields.One2many('model_car_fleet_c', 'Model_id', string='Fleet IDS',track_visibility='onchange')
    opportunity_ids = fields.One2many('crm.lead', 'model_id', string='Opportunity IDS',track_visibility='onchange')
