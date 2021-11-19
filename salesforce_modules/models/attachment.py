from odoo import models, fields, api


class Attachment(models.Model):
    _name = 'ir.attachment'
    _inherit = ['ir.attachment', 'mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Attachment"

    active = fields.Boolean('Active', default=True)
    # CreatedById already in odoo
    # name                    already in odoo i.e. (name)
    # LastModifiedById already in odoo
    OwnerId = fields.Many2one('res.users', string='Owner')

    document_use = fields.Selection(
        [('Implantation', 'Implantation'), ('Internal deployment', 'Internal deployment'), ('Movement', 'Movement'),
         ('Administered', 'Administered')], 'Use of Documents')
    financial_contract_id = fields.Many2one('financial_contract', string="Financial Contract ID")

    account_id = fields.Many2one('account.account', string='Account ID')
    lead_id = fields.Many2one('crm.lead', string='Lead Id')
    task_id = fields.Many2one('project.task', string='Task Id')
    campaign_id = fields.Many2one('model_campaign', string='Campaign Id')
    product_id = fields.Many2one('product.template', string='Product Id')

    legal_pending_matter_id = fields.Many2one('model_legal_pending_matter', string="Legal Pending Matter ID")
    quote_id = fields.Many2one('model_quote', string="Quote ID")
    # document_use               = fields.Selection([('Implantation','Implantation'),('Internal deployment','Internal deployment'),('Movement','Movement'),('Administered','Administered')],'Use of Documents')
    # financial_contract_id    =   fields.Many2one('financial_contract', string="Financial Contract ID")
    opportunity_id = fields.Many2one('crm.lead', string="Opportunity")
    portal_access_id = fields.Many2one('portal.access', string="Portal Access")
