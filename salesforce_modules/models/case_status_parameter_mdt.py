from odoo import models, fields, api

class Case_Status_Parameter_MDT(models.Model):
    _name = 'model_case_status_parameter_mdt'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Case_Status_Parameter_MDT"
    _rec_name = 'DeveloperName'

    # CreatedById  already in odoo
    # LastModifiedById already in odoo

    DeveloperName = fields.Char(string='Custom Metadata Record Name',size=40)
    MasterLabel = fields.Char(string='Label',size=40)
    NamespacePrefix = fields.Text(string='Namespace Prefix')
    IsProtected = fields.Boolean(string='Protected Component')
    process = fields.Selection([('Contract Services','Contract Services')],string='Process')
    status = fields.Selection([('New','New'),('classified','classified'),('Alert','Alert Sent'),('On Hold','In Progress'),
                               ('Awaiting Customer Return','Awaiting Customer Return'),('Negotiation','Negotiation'),
                               ('Closed','Closed'),('Called off','Called offs'),('Released for Deployment','Released for Deployment'),
                               ('Checklist + Welcome','Checklist + Welcome'),('Awaiting Documentation','Awaiting Documentation'),
                               ('Document Analysis','Document Analysis'),('Review/Awaiting Documentation','Review/Awaiting Documentation'),
                               ('Shipping to Operator','Shipping to Operator'),('Operator Review','Operator Review'),
                               ('Implemented in the Operator','Implemented in the Operator'),('Contract Activation','Contract Activation'),
                               ('Released for Service','Released for Service')],string='Status')
