# -*- coding: utf-8 -*-

from odoo import models, fields


class SalesForceSyncHistory(models.Model):

    _name = 'salesforce.sync.history'
    _order = 'sync_date desc'
    _description = 'Salesforce Sync History'

    type = fields.Selection([('Account', 'Account'), ('Contact', 'Contact'), ('Individual', 'Individual'),
                            ('PartnerNetworkConnection', 'PartnerNetworkConnection'), ('Rep__c', 'Rep__c'),
                             ('Pricebook2', 'Pricebook2'), ('Opportunity', 'Opportunity'),
                             ('Lead', 'Lead'),('Task','Task')], string="Type")
    sf_id = fields.Char('Salesforce Record Id', readonly=True, default=0)
    sync_date = fields.Datetime('Sync Date', readonly=True, required=True, default=fields.Datetime.now)
    operation = fields.Selection([('salesforce_to_odoo', 'Salesforce to Odoo')],
                                    string="Operation")
    status = fields.Selection([('success', 'Success'), ('failed', 'Failed')], string="Operation Status")
    message = fields.Text('Summary')

    def create_log_param(self, type, sf_id, status, operation, message=False):
        """
        """
        params = {
            'type': type,
            'sf_id': sf_id,
            'operation': operation,
            'message': message,
            'status': status
        }
        self.sudo().create(params)


    # no_of_orders_sync = fields.Integer('Sync SalesOrders', readonly=True)
    # no_of_products_sync = fields.Integer('Sync Products', readonly=True)
    # no_of_customers_sync = fields.Integer('Sync Customers', readonly=True)
    # no_of_opportunities_sync = fields.Integer('Sync Opportunities', readonly=True)
    # document_link = fields.Char('Document Link', readonly=True)


# class SalesForceFailedLog(models.Model):
