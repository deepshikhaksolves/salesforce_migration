from odoo import models, fields, api


class Attachment(models.Model):
    _inherit = 'ir.attachment'
    _description = "Salesforce Attachment"


    active       = fields.Boolean('Active',default=True)
    # CreatedById already in odoo
    # name                    already in odoo i.e. (name)
    # LastModifiedById already in odoo
    OwnerId                 = fields.Many2one('res.users',string='Owner')

    document_use               = fields.Selection([('Implantation','Implantation'),('Internal deployment','Internal deployment'),('Movement','Movement'),('Administered','Administered')],'Use of Documents')
   