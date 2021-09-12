from odoo import models, fields, api

class Car_Fleet_C(models.Model):
    _name = 'model_car_fleet_c'
    _description = "Salesforce Car Fleet C"
    _rec_name = 'Name'

    # CreatedById  already in odoo
    # LastModifiedById already in odoo

    Year = fields.Char(string='Year', size=9)
    #Contract_id = fields.Many2one('contract',string='Contract')
    # Field is related to contract object which is not define

    Name = fields.Char(string='Fleet')
    #Brand_id = fields.Many2one('brand',string='Mark')
    # Field is related to brand object which is not define

    Model_id =fields.Many2one('ir.model',string='Model')
    OwnerId = fields.Many2one('res.users',string='Owner')
    Day = fields.Char(string='Board',size=8)
    RENAVAM = fields.Float(string='RENAVAM',digits=(11,0))
