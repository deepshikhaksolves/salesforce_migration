from odoo import models, fields, api


class ContractPlan(models.Model):
    _name = 'model_contract_plan'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Contract Plan"
    _rec_name = 'accommodation'

    accommodation = fields.Char('Accommodation', track_visibility='onchange')
    beneficiary_type = fields.Selection([('Active', 'Active'), ('Extension', 'Extension')], 'Beneficiary Type', track_visibility='onchange')
    Contract_id = fields.Many2one('hr.contract',string='Contract')
    Coverage = fields.Char('Coverage', track_visibility='onchange')
    # CreatedById already in odoo
    Code = fields.Char('Code', track_visibility='onchange')
    downgrade_condition = fields.Selection(
        [('does not have', 'does not have'), ('In promoting an employee', 'In promoting an employee'),
         ('On the anniversary of the Contract', 'On the anniversary of the Contract'),
         ('At the end of the campaign', 'At the end of the campaign')], 'Downgrade Condition', track_visibility='onchange')

    Product_Family = fields.Char("Product Family", track_visibility='onchange')
    End_Date = fields.Date('End of Term', track_visibility='onchange')
    geographic_scope = fields.Char("Geographic Scope", track_visibility='onchange')
    Start_Date = fields.Date('Beginning of Effectiveness', track_visibility='onchange')
    # LastModifiedById already in odoo
    OwnerId = fields.Many2one('res.users', string='Owner', track_visibility='onchange')
    Name = fields.Char('Plan Code', size=80, track_visibility='onchange')
    Product_id = fields.Many2one('product.template', string='Product', track_visibility='onchange')
    RecordTypeId = fields.Integer('Record Type', track_visibility='onchange')
    upgrade_condition = fields.Selection(
        [('does not have', 'does not have'), ('In promoting an employee', 'In promoting an employee'),
         ('On the anniversary of the Contract', 'On the anniversary of the Contract'),
         ('At the end of the campaign', 'At the end of the campaign')], 'Upgrade Condition', track_visibility='onchange')

    Plan_Value = fields.Float('Plan Value', digits=(16, 2), track_visibility='onchange')

    product_price_ids = fields.One2many('product_price', 'contract_product__c', 'Product Price IDS')

    benifit_politic_id = fields.Many2one('model_benfit_politic', string='Benifit Politic Id', track_visibility='onchange')