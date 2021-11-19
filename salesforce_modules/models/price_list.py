from odoo import models, fields, api


class PriceList(models.Model):
    _name = 'model_price_list'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Price List"
    _rec_name = 'Name'

    contract_c = fields.Many2one('hr.contract', string='Contract',track_visibility='onchange')
    # CreatedById  already in odoo
    readjustment_date_c = fields.Date('Readjustment Date',track_visibility='onchange')
    end_validity_c = fields.Date('End Effective',track_visibility='onchange')
    start_validity_c = fields.Date('Beginning of Term',track_visibility='onchange')
    # LastModifiedById  already in odoo
    maximum_lives_c = fields.Float('Maximum Lives', digits=(4, 0),track_visibility='onchange')
    maximum_holder_lives_c = fields.Float('Maximum Holder Lives', digits=(4, 0),track_visibility='onchange')
    minimum_lives_c = fields.Float('Minimum Lives', digits=(4, 0),track_visibility='onchange')
    minimum_holder_lives_c = fields.Float('Minimum Holder Lives', digits=(4, 0),track_visibility='onchange')
    Name = fields.Char('Price List Name', size=80,track_visibility='onchange')
    carrier_c = fields.Many2one('account.account', string='Operator',track_visibility='onchange')
    OwnerId = fields.Many2one('res.users', string='Owner',track_visibility='onchange')
    percentage_adjustment_c = fields.Float('Percentage readjustment', digits=(2, 2),track_visibility='onchange')
    origin_table_c = fields.Many2one('model_price_list', string='source table',track_visibility='onchange')
    account_id = fields.Many2one('account.account', string='Account Id',track_visibility='onchange')
    product_price_ids = fields.One2many('product_price', 'price_list_id', 'Product Price IDS',track_visibility='onchange')
    study_configuration_price_table_ids = fields.One2many('model_study_configuration_price_table','price_table_id')
