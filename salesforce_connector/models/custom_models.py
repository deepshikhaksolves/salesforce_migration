# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class SfPartnerNetworkConnectionModel(models.Model):
    _name = 'sf.pnc'
    _description = 'Salesforce Partner Network Connection'

    active = fields.Boolean(default=True)
    sf_id = fields.Char('Id')
    sf_pnc_account_id = fields.Many2one('res.partner', 'Account Id')
    sf_pnc_contact_id = fields.Many2one('res.partner', 'Contact Id')
    sf_pnc_response_date = fields.Datetime('ResponseDate')
    sf_pnc_connection_name = fields.Char('ConnectionName')
    sf_pnc_connection_status = fields.Char('Connection Status')
    sf_created_date = fields.Datetime(string="PNC Created Date")
    sf_last_modified_date = fields.Datetime(string="PNC Last Modified Date")


class SfRepCModel(models.Model):
    _name = 'sf.rep__c'
    _description = 'Salesforce Rep__c'
    _rec_name = 'sf_id'

    active = fields.Boolean(default=True)
    sf_id = fields.Char('Id')
    sf_rep_name = fields.Char('Name')
    sf_rep_phone = fields.Char('Phone__c')
    sf_rep_website = fields.Char('Website__c')
    sf_rep_address = fields.Text('Address__c')
    sf_rep_conn_received_id = fields.Many2one('sf.pnc', 'Connection Received Id')
    sf_rep_conn_sent_id = fields.Many2one('sf.pnc', 'Connection Sent Id')
    sf_rep_email = fields.Char('Email__c')
    sf_rep_is_deleted = fields.Boolean('Is Deleted')
    sf_created_date = fields.Datetime(string="Rep__c Created Date")
    sf_last_modified_date = fields.Datetime(string="Rep__c Last Modified Date")


class SfPriceBookModel(models.Model):
    _name = 'sf.pricebook'
    _description = 'Salesforce Pricebook'

    active = fields.Boolean(default=True)
    sf_id = fields.Char('Id')
    sf_pb_name = fields.Char('Name')
    sf_pb_is_active = fields.Boolean('Is Active')
    sf_pb_is_standard = fields.Boolean('Is Standard')
    sf_pb_is_archived = fields.Boolean('Is Archived')
    sf_pb_is_deleted = fields.Boolean('Is Deleted')
    sf_pb_description = fields.Text('Description')
    sf_created_date = fields.Datetime(string="Price book Created Date")
    sf_last_modified_date = fields.Datetime(string="Price book Last Modified Date")



