from odoo import models, fields, api


class StudyConfigurationPriceTable(models.Model):
    _name = 'model_study_configuration_price_table'
    _description = "Salesforce Study Configuration Price Table"
    _rec_name = 'Name'

    # study_configuration_id = fields.Many2one('study.study', string="Study Setup") # Model Not Found
    # CreatedById already in odoo
    # LastModifiedById already in odoo
    Name = fields.Char(string="Name")
    price_table_id = fields.Many2one('price_schedule',string="Price list")