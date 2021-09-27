from odoo import models, fields, api


class ContractPlan(models.Model):
    _name = 'model_contract_plan'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Contract Plan"
    _rec_name = 'accommodation'

    accommodation = fields.Char('Accommodation')
    beneficiary_type = fields.Selection([('Active', 'Active'), ('Extension', 'Extension')], 'Beneficiary Type')
    # Contract_id             = fields.Many2one('',string='Contract')
    Coverage = fields.Char('Coverage')
    # CreatedById already in odoo
    Code = fields.Char('Code')
    downgrade_condition = fields.Selection(
        [('does not have', 'does not have'), ('In promoting an employee', 'In promoting an employee'),
         ('On the anniversary of the Contract', 'On the anniversary of the Contract'),
         ('At the end of the campaign', 'At the end of the campaign')], 'Downgrade Condition')

    Product_Family = fields.Char("Product Family")
    End_Date = fields.Date('End of Term')
    geographic_scope = fields.Char("Geographic Scope")
    Start_Date = fields.Date('Beginning of Effectiveness')
    # LastModifiedById already in odoo
    OwnerId = fields.Many2one('res.users', string='Owner')
    Name = fields.Char('Plan Code', size=80)
    Product_id = fields.Many2one('product.template', string='Product')
    RecordTypeId = fields.Integer('Record Type')
    upgrade_condition = fields.Selection(
        [('does not have', 'does not have'), ('In promoting an employee', 'In promoting an employee'),
         ('On the anniversary of the Contract', 'On the anniversary of the Contract'),
         ('At the end of the campaign', 'At the end of the campaign')], 'Upgrade Condition')

    Plan_Value = fields.Float('Plan Value', digits=(16, 2))

    product_price_ids = fields.One2many('product_price', 'contract_product__c', 'Product Price IDS')

    benifit_politic_id = fields.Many2one('model_benfit_politic', string='Benifit Politic Id')