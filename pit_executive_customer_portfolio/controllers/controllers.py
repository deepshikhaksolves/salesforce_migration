# -*- coding: utf-8 -*-
# from odoo import http


# class PitExecutiveCustomerPortfolio(http.Controller):
#     @http.route('/pit_executive_customer_portfolio/pit_executive_customer_portfolio/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pit_executive_customer_portfolio/pit_executive_customer_portfolio/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pit_executive_customer_portfolio.listing', {
#             'root': '/pit_executive_customer_portfolio/pit_executive_customer_portfolio',
#             'objects': http.request.env['pit_executive_customer_portfolio.pit_executive_customer_portfolio'].search([]),
#         })

#     @http.route('/pit_executive_customer_portfolio/pit_executive_customer_portfolio/objects/<model("pit_executive_customer_portfolio.pit_executive_customer_portfolio"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pit_executive_customer_portfolio.object', {
#             'object': obj
#         })
