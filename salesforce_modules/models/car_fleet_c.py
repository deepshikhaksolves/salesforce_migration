from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Car_Fleet_C(models.Model):
    _name = 'model_car_fleet_c'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = "Salesforce Car Fleet C"
    _rec_name = 'Name'

    # CreatedById  already in odoo
    # LastModifiedById already in odoo

    Year = fields.Char(string='Year', size=9)
    Contract_id = fields.Many2one('hr.contract',string='Contract')
    Name = fields.Char(string='Fleet')
    Brand_id = fields.Many2one('model_brand_c',string='Mark')
    Model_id =fields.Many2one('ir.model',string='Model')
    OwnerId = fields.Many2one('res.users',string='Owner')
    Day = fields.Char(string='Board',size=8)
    RENAVAM = fields.Float(string='RENAVAM',digits=(11,0))

    @api.constrains('RENAVAM')
    def digit_validation(self):
        for rec in self:
            if rec.RENAVAM > 99999999999:
                raise ValidationError("Renavam should not greater then 11 digits")

