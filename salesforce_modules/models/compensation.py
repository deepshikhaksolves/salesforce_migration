from odoo import models, fields, api

class Compensation(models.Model):
    _name = 'compensation'

    Competence = fields.Date(string='Competence')
    # CreatedById created by default
    Payment_Day = fields.Date(string='Payday')
    # LastModifiedById created by default
    Invoice_Number = fields.Char(string='Invoice Number', size=100)
    Parcel_Number = fields.Float(string='Installment Number	', digits=(10, 0))
    Provision_Number = fields.Char(string='Provision Number', size=50)
    OwnerId = fields.Many2one('res.users', string='Owner')
    # Income = fields.Many2one('Revenue', string="Revenue") # Model Not Found
    name = fields.Char(string='Remuneration')
    Status = fields.Selection([
        ('provisioned', 'provisioned'), ('downloaded', 'downloaded')
    ], string='Status')
    Due_Date = fields.Date(string='Due_Date')