from odoo import models, fields, api

class Checklist_C(models.Model):
    _name = 'model_checklist_c'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Checklist C"
    _rec_name = 'Name'

    # CreatedById  already in odoo
    # LastModifiedById already in odoo

    Name = fields.Char(string='Checklist',size=80)
    How = fields.Char(string='Comment',size=255)
    Contract_id = fields.Many2one('hr.contract',string='Contract')

    critical = fields.Selection([('NOT SIGNED BY REP. COMPANY LEGAL','NOT SIGNED BY REP. COMPANY LEGAL'),
                                 ('MISSING CNPJ STAMP','MISSING CNPJ STAMP'),('PAGES MISSING','PAGES MISSING'),
                                 ('INCORRECT INFORMATION IN THE DOCUMENT','INCORRECT INFORMATION IN THE DOCUMENT'),
                                 ('NOT RECEIVED','NOT RECEIVED'),('OTHERS','OTHERS'),('UNREADABLE','UNREADABLE'),
                                 ('ERASURE','ERASURE'),('NOT SIGNED BY THE HOLDER','NOT SIGNED BY THE HOLDER')],
                                string='Review')
    regularization_date = fields.Date(string='Regularization Date')
    Document_id = fields.Many2one('ir.attachment',string='Document')
    OwnerId = fields.Many2one('res.users',string='Owner')
    Status = fields.Selection([('Pending','Pending'),('Analysis','Analysis'),('critical','critical'),
                               ('Scanning','Scanning'),('Concluded','Concluded')],string='Status')
