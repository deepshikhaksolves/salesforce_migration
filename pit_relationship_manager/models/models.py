# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class pit_relationship_manager(models.Model):
#     _name = 'pit_relationship_manager.pit_relationship_manager'
#     _description = 'pit_relationship_manager.pit_relationship_manager'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
