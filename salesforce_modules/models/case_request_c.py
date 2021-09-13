from odoo import models, fields, api

class Case_Request_C(models.Model):
    _name = 'model_case_request_c'
    _description = "Salesforce Case Request C"
    _rec_name = 'Name'

    # CreatedById  already in odoo
    # LastModifiedById already in odoo

    Subject_id = fields.Many2one('model_subject_c',string='Subject')
    Case_id = fields.Many2one('model_case',string='Service')
    Comments = fields.Text(string='Comment')
    Name = fields.Char(string='Code')
    Cancel_Date = fields.Datetime(string='Cancellation Date')
    Case_Model_id = fields.Many2one('model_service_c',string='Service Model')
    Case_Reason = fields.Selection([('Information','Information'),('Request','Request'),('Complaint','Complaint')],string='Reason for Service')
    OwnerId = fields.Many2one('res.users',string='Owner')
    # Case_Request_SLA_id = fields.Many2one('model_request_deadline',string='Service Request Deadline')
    # Case_Request_SLA_id field oject request deadline not define
    Case_Priority = fields.Selection([('Low','Low'),('Average','Average'),('High','High')],string='Priority of Service')
    SLAF = fields.Text(string='SALAD')
    Request_id = fields.Many2one('model_request',string='Request')
    Status = fields.Selection([('In progress','In progress'),('Waiting','Waiting'),('Back','Back'),('returned','returned'),
                               ('Closed','Closed'),('Successfully completed','Successfully completed'),
                               ('Finished unsuccessfully','Finished unsuccessfully'),('Called off','Called off'),
                               ('In-Process Analysis','In-Process Analysis'),('Criticized Process','Criticized Process'),
                               ('declined','declined'),('Registration in System','Registration in System'),
                               ('Sent to Operator','Sent to Operator'),('Deployment Layout','Deployment Layout'),
                               ('Cards','Cards'),('Books','Books'),('Bank data','Bank data'),('Billing Layout','Billing Layout'),
                               ('No return','No return'),('Pending','Pending'),('Requested','Requested'),('Returned for Regularization','Returned for Regularization'),
                               ('Invalid Bank Data','Invalid Bank Data'),('Returned by the Operator','Returned by the Operator'),
                               ('Documents Received','Documents Received'),('Regularized','Regularized'),('Programed payment','Programed payment'),
                               ('Paid out','Paid out'),('I do not pay','I do not pay'),('refused','refused'),('Indemnified','Indemnified'),
                               ('Partially Indemnified','Partially Indemnified'),('Awaiting NF','Awaiting NF'),('Awaiting Billet Generation','Awaiting Billet Generation'),
                               ('Awaiting Validation','Awaiting Validation'),('Order in Process','Order in Process')],string='Status')
