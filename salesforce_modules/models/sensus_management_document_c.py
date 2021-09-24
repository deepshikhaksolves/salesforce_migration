from odoo import models,fields,api

class Sensus_Management_Document_C(models.Model):
    _name = 'model_sensus_management_document_c'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Sensus Management Document C"
    _rec_name = 'Name'

    # CreatedById  already in odoo
    # LastModifiedById already in odoo

    Contract_id = fields.Many2one('hr.contract',string='Contract',track_visibility='onchange')

    document_id = fields.Many2one('ir.attachment',string='Document',track_visibility='onchange')
    # Field is related to record object which is not define

    Degree_of_Kinship = fields.Selection([('Spouse','Spouse'),('Companion','Companion'),('Son (a)','Son (a)'),('Stepson','Stepson'),('Aggregate','Aggregate')],string='Degree of kinship',track_visibility='onchange')
    Name = fields.Char(string='ID',track_visibility='onchange')
    OwnerId = fields.Many2one('res.users',string='Owner',track_visibility='onchange')
    Required = fields.Boolean(string='Required',track_visibility='onchange')
    Type_of_Beneficiary = fields.Selection([('Holder','Holder'),('Dependent','Dependent')],string='Type of Beneficiary',track_visibility='onchange')
    Type_of_Movement = fields.Selection([('Inclusion','Inclusion'),('Change','Change'),('Exclusion','Exclusion'),('Transfer','Transfer')],string='Type of Movement',track_visibility='onchange')
