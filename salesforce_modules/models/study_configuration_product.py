from odoo import models, fields, api


class StudyConfigurationProduct(models.Model):
    _name = 'model_study_configuration_product'
    _description = "Salesforce Study Configuration Product"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'Name'

    carrier = fields.Char(string="Carrier")
    # CreatedById already in odoo
    Name = fields.Char(string="Identification")
    # LastModifiedById already in odoo
    maximum_plus_59_lives = fields.Float(string="Maximum +59 Lives", digits=(6, 0))
    Maximum_Lives = fields.Float(string="Maximum Lives", digits=(6, 0))
    minimum_holder_lives = fields.Float(string="Minimum Holder Lives", digits=(6, 0))
    minimum_lives = fields.Float(string="Minimum Lives", digits=(6, 0))
    product = fields.Many2one('product.template', string="Product")
    study_configuration_id = fields.Many2one('study_configuration', string="Study Configuration")
