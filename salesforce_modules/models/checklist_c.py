from odoo import models, fields, api

class Checklist_C(models.Model):
    _name = 'model_checklist_c'
    _description = "Salesforce Checklist C"
    _rec_name = 'Name'

    # CreatedById  already in odoo
    # LastModifiedById already in odoo

    Name = fields.Char(string='Checklist',size=80)
    How = fields.Char(string='Comment',size=255)
    # Contract_id = fields.Many2one('model_contract',string='Contract')
    # Contract_id field is related to contract object which is not define
    critical = fields.Selection([('NOT SIGNED BY REP. COMPANY LEGAL','NOT SIGNED BY REP. COMPANY LEGAL'),
                                 ('MISSING CNPJ STAMP','MISSING CNPJ STAMP'),('PAGES MISSING','PAGES MISSING'),
                                 ('INCORRECT INFORMATION IN THE DOCUMENT','INCORRECT INFORMATION IN THE DOCUMENT'),
                                 ('NOT RECEIVED','NOT RECEIVED'),('OTHERS','OTHERS'),('UNREADABLE','UNREADABLE'),
                                 ('ERASURE','ERASURE'),('NOT SIGNED BY THE HOLDER','NOT SIGNED BY THE HOLDER')],
                                string='Review')
    regularization_date = fields.Date(string='Regularization Date')
    # Document_id = fields.Many2one('model_record',string='Document')
    # Document_id is related to model_record which is not define
    OwnerId = fields.Many2one('res.users',string='Owner')
    Status = fields.Selection([('Pending','Pending'),('Analysis','Analysis'),('critical','critical'),
                               ('Scanning','Scanning'),('Concluded','Concluded')],string='Status')
