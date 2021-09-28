# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class pit_executive_accounting(models.Model):
#     _name = 'pit_executive_accounting.pit_executive_accounting'
#     _description = 'pit_executive_accounting.pit_executive_accounting'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
