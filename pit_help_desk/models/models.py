# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class pit_help_desk(models.Model):
#     _name = 'pit_help_desk.pit_help_desk'
#     _description = 'pit_help_desk.pit_help_desk'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
