from odoo import models, fields, api

class RequestConfig(models.Model):
    _name = 'request_config'
    _description = "Salesforce Request Configuration"
    _rec_name = 'Name'

    # Subject_Case_Model        = fields.Many2one('', string='Subject Setting')
    # CreatedById  already in odoo
    Customer_Service_Model   = fields.Char('Customer Service Model')
    Name                     = fields.Char('Code')
    FormulaEntitlement       = fields.Char('Entitlement')
    # LastModifiedById already in odoo
    OwnerId             = fields.Many2one('res.users',string='Owner')
    Request_id          = fields.Many2one('model_request',string='Request')
    Subject             = fields.Char('Subject')