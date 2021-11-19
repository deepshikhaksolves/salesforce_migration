from odoo import models, fields, api


class BrandC(models.Model):
    _name = 'model_brand_c'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Salesforce Brand'
    _rec_name = 'Name'

    # CreatedById already in odoo
    # LastModifiedById already in odoo
    Name = fields.Char(string="Mark", size=80, track_visibility='onchange')
    OwnerId = fields.Many2one('res.users', string='Owner', track_visibility='onchange')
    model_ids = fields.One2many('salesforce.model_c', 'Brand_c', string='Model')
    fleet_ids = fields.One2many('model_car_fleet_c', 'Brand_id', string='Fleet')

