from odoo import models, fields, api


class StudyConfigurationProduct(models.Model):
    _name = 'model_study_configuration_product'
    _description = "Salesforce Study Configuration Product"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'Name'

    carrier = fields.Char(string="Carrier",track_visibility='onchange')
    # CreatedById already in odoo
    Name = fields.Char(string="Identification",track_visibility='onchange')
    # LastModifiedById already in odoo
    maximum_plus_59_lives = fields.Float(string="Maximum +59 Lives",track_visibility='onchange')
    Maximum_Lives = fields.Float(string="Maximum Lives",track_visibility='onchange')
    minimum_holder_lives = fields.Float(string="Minimum Holder Lives",track_visibility='onchange')
    minimum_lives = fields.Float(string="Minimum Lives",track_visibility='onchange')
    product = fields.Many2one('product.template',string="Product",track_visibility='onchange')
    study_configuration_id = fields.Many2one('study_configuration',string="Study Configuration",track_visibility='onchange')



