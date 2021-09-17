# -*- coding: utf-8 -*-

from odoo import models, fields

class SalesForceModelMap(models.Model):
    _name = 'sf.model.mapping'
    _rec_name = 'sf_model'
    _description = "Salesforce Model to odoo model mapping"

    o_model = fields.Many2one('ir.model', string='Odoo Model')
    sf_model = fields.Char(string='Salesforce Model', required=True)
    sf_columns_map = fields.One2many('sf.columns.mapping', 'main_field_map', string='Columns to be Mapped')
    # odoo_field = fields.Many2one('ir.model.fields', string="Odoo Field")
    # sf_field = fields.Char(string="Salesforce Field")

class SalesForceMappedColumnsMap(models.Model):
    _name = 'sf.columns.mapping'
    _description = "Salesforce columns to odoo columns mapping"

    main_field_map = fields.Many2one('sf.model.mapping', string="Salesforce Model Mapped")
    o_model = fields.Many2one('ir.model', related='main_field_map.o_model', store=True, string="Model")
    sf_model = fields.Char(related='main_field_map.sf_model', store=True, string="Salesforce Model")
    type = fields.Selection([('integer', 'Integer'), ('char', 'Char'), ('float', 'Float'), ('text', 'Text'),
                             ('date', 'Date'), ('selection', 'Selection'),
                             ('boolean', 'Boolean'), ('datetime', 'Datetime'), ('many2one', 'Many2one'),
                             ('one2many', 'One2many'), ('many2many', 'Many2many'), ('Lookup', 'Lookup')],
                            string="Field Type", required=False)
    sf_relational_model = fields.Char(string="Salesforce Reference Model", required=False)
    query_field = fields.Boolean('Is query field', default=True)
    odoo_field = fields.Many2one('ir.model.fields', string="Odoo Field")
    sf_field = fields.Char(string="Salesforce Field")

class SalesForceStagesMappedCRMStages(models.Model):
    _name = 'sf.stages.mapping'
    _rec_name = 'sf_stage_name'
    _description = "Salesforce Stage Name mapping"

    sf_stage_name = fields.Char('Salesforce Stage Name', required=True)
    sf_crm_stage = fields.Many2one('crm.stage', string='CRM Stage', required=True)
    mark = fields.Selection([
        ('won','Mark Won in CRM'),
        ('lost','Mark Lost in CRM'),
        ('archive','Mark Archive in CRM'),
        ('canceled','Mark Canceled in CRM')
    ])

    tags = fields.Many2one('crm.lead.tag', string='Additional tag')

    # _sql_constraints = [(
    #     'unique sf stage name',
    #     'UNIQUE(sf_stage_name)',
    #     "Salesforce Stage already exist with this name"
    # )]


class sf_country_mapping(models.Model):
    _name = 'sf.country.map'
    _description = 'Salesforce country mapping to odoo default country'

    _rec_name = 'sf_country_name'

    sf_country_name = fields.Char(string='Sf country Name', required=True)
    sf_res_partner_ids = fields.One2many('res.partner', 'country_id', string='sf Res partner ids')
    sf_our_matched_country = fields.Many2one('res.country', string='Matched Country name')

    def write(self, vals):
        if vals.get('sf_our_matched_country'):
            country_id = vals.get('sf_our_matched_country')
            for partner_id in self.sf_res_partner_ids:
                partner_id.write({'country_id': country_id})
        super( sf_country_mapping, self ).write(vals)


class sf_state_mapping(models.Model):
    _name = 'sf.state.map'
    _description = 'Salesforce state mapping to odoo default state'

    _rec_name = 'sf_state_name'

    sf_state_name = fields.Char(string='Sf State Name', required=True)
    sf_res_partner_ids = fields.One2many('res.partner', 'state_id', string='sf Res partner ids')
    sf_our_matched_state = fields.Many2one('res.country.state', string='Matched state name')

    def write(self, vals):
        if vals.get('sf_our_matched_state'):
            state_id = vals.get('sf_our_matched_state')
            for partner_id in self.sf_res_partner_ids.ids:
                partner_id.write({'state_id': state_id})
        super(sf_state_mapping, self).write(vals)


class rfq_type_mapping(models.Model):
    _name = 'sf.quote.type.map'
    _rec_name = 'quote_type_name'
    _description = "Salesforce Custom field Quote_Type__c mapping"

    quote_type_name = fields.Char('Quote_Type__C Name', required=True)
    # quote_type_ids = fields.One2many('crm.lead', 'RFQ_type',string="Opportunity ids")

    def write(self, vals):
        if vals.get('quote_type_ids'):
            quote_type_id = self.env['sf.quote.type.map'].search([('quote_type_name', '=', self.quote_type_name)]).id
            for opportunity in self.quote_type_ids:
                opportunity.write({'RFQ_type': quote_type_id})
        super(rfq_type_mapping, self).write(vals)

class SalesforecTaskTypemapping(models.Model):
    _name = 'salesforce.task.type.mapping'
    _description = 'mapping for salesforce task to odoo activity task'
    _rec_name = 'task_name'

    task_name = fields.Many2one('salesforce.task.types',string='Task Type', ondelete='cascade')
    mapped_task_name = fields.Many2one('mail.activity.type',string='Mapped activity type', ondelete='cascade')