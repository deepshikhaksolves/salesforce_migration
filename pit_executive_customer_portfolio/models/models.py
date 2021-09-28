# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class pit_executive_customer_portfolio(models.Model):
#     _name = 'pit_executive_customer_portfolio.pit_executive_customer_portfolio'
#     _description = 'pit_executive_customer_portfolio.pit_executive_customer_portfolio'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
