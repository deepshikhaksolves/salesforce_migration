from odoo import models,fields,api

class Sensus_Management_Document_C(models.Model):
    _name = 'model_sensus_management_document_c'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Sensus Management Document C"
    _rec_name = 'Name'

    # CreatedById  already in odoo
    # LastModifiedById already in odoo

    #Contract_id = fields.Many2one('contract',string='Contract')
    #Field is related to contract object which is not define
    #document_id = fields.Many2one('record',string='Document')
    # Field is related to record object which is not define

    Degree_of_Kinship = fields.Selection([('Spouse','Spouse'),('Companion','Companion'),('Son (a)','Son (a)'),('Stepson','Stepson'),('Aggregate','Aggregate')],string='Degree of kinship')
    Name = fields.Char(string='ID')
    OwnerId = fields.Many2one('res.users',string='Owner')
    Required = fields.Boolean(string='Required')
    Type_of_Beneficiary = fields.Selection([('Holder','Holder'),('Dependent','Dependent')],string='Type of Beneficiary')
    Type_of_Movement = fields.Selection([('Inclusion','Inclusion'),('Change','Change'),('Exclusion','Exclusion'),('Transfer','Transfer')],string='Type of Movement')
