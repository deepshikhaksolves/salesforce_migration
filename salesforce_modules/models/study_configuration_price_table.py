from odoo import models, fields, api


class StudyConfigurationPriceTable(models.Model):
    _name = 'model_study_configuration_price_table'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Study Configuration Price Table"
    _rec_name = 'Name'

    study_configuration_id = fields.Many2one('study_configuration', string="Study Setup",track_visibility='onchange')
    # CreatedById already in odoo
    # LastModifiedById already in odoo
    Name = fields.Char(string="Name",track_visibility='onchange')
    price_table_id = fields.Many2one('model_price_list',string="Price list")