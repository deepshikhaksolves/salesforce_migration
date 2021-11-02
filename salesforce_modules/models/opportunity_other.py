from odoo import models, fields, api


class SalesforceOpportunityContactRole(models.Model):
    _name = 'crm.lead.contact.role'
    _inherit = 'mail.thread'
    _description = 'Salesforce Opportunity Contact Role'

    contacts_id = fields.Many2one('res.partner', string="Contact",track_visibility='onchange')
    user_id = fields.Many2one('res.users', string="Created By",track_visibility='onchange')
    last_modified_by_id = fields.Many2one('res.users', string="Last Modified By",track_visibility='onchange')
    opportunity_id = fields.Many2one('crm.lead', string="Opportunity",track_visibility='onchange')
    is_primary = fields.Boolean('Primary',track_visibility='onchange')
    role = fields.Selection([
        ('Analista Senior de RH', 'Analista Senior de RH'),
        ('evaluator', 'Avaliador'),
        ('economic_buyer', 'Comprador'),
        ('Technical_Buyer', 'Comprador - Técnico'),
        ('Coordenador de RH', 'Coordenador de RH'),
        ('Decision Maker', 'Decisor'),
        ('Economic Decision Maker', 'Decisor - Compras'),
        ('Gerente de RH', 'Gerente de RH'),
        ('Influencer', 'Influenciador'),
        ('Executive Sponsor', 'Sponsor'),
        ('Business User', 'Usuário'),
        ('Other', 'Outros'),
    ], string="Role",track_visibility='onchange')

    case_id = fields.Many2one('model_case', string='Case Id')


class SalesforceOpportunityCompetitor(models.Model):
    _name = 'crm.lead.competitor'
    _inherit = 'mail.thread'
    _description = 'Salesforce Opportunity Competitor'

    created_date = fields.Datetime(string="Created Date",track_visibility='onchange')
    last_modified_date = fields.Datetime(string="Last Modified Date",track_visibility='onchange')
    user_id = fields.Many2one('res.users', string="Created By",track_visibility='onchange')
    last_modified_by_id = fields.Many2one('res.users', string="Last Modified By",track_visibility='onchange')
    opportunity_id = fields.Many2one('crm.lead', string="Opportunity",track_visibility='onchange')
    is_deleted = fields.Boolean('Deleted',track_visibility='onchange')
    competitor_name = fields.Selection([
        ('',''),
    ],string="Competitor Name",track_visibility='onchange')
    strengths = fields.Char('Strengths',size=1000,track_visibility='onchange')
    weaknesses = fields.Char('Weaknesses',size=1000,track_visibility='onchange')
    system_mod_stamp = fields.Datetime('System Modstamp',track_visibility='onchange')


class SalesforceOpportunityLineItem(models.Model):
    _name = 'crm.lead.lineitem'
    _inherit = 'mail.thread'
    _description = 'Salesforce Opportunity Product'

    service_date = fields.Date(string="Date",track_visibility='onchange')
    user_id = fields.Many2one('res.users', string="Created By",track_visibility='onchange')
    last_modified_by_id = fields.Many2one('res.users', string="Last Modified By",track_visibility='onchange')
    opportunity_id = fields.Many2one('crm.lead', string="Opportunity",track_visibility='onchange')
    discount = fields.Float('Discount',digits=(3,2),track_visibility='onchange')
    quantity = fields.Float('Quantity', digits=(10, 2),track_visibility='onchange')
    unit_price = fields.Float('Sales Price', digits=(16, 2),track_visibility='onchange')
    Subtotal = fields.Float('Subtotal', digits=(16, 2),track_visibility='onchange')
    TotalPrice = fields.Float('TotalPrice', digits=(16, 2),track_visibility='onchange')
    list_price = fields.Float('List Price', digits=(16, 2),track_visibility='onchange')
    description = fields.Char('Line Description',size=255,track_visibility='onchange')
    carrier = fields.Char('Operadora',track_visibility='onchange')
    name = fields.Char('Opportunity Product Name',size=376,track_visibility='onchange')
    product2Id = fields.Many2one('product.product', string="Product",track_visibility='onchange')
    product_code = fields.Char('Product Code',size=255,track_visibility='onchange')


class SalesforceOpportunityProduct(models.Model):
    _name = 'crm.lead.product'
    _inherit = 'mail.thread'
    _description = 'Salesforce Opportunity Product'

    user_id = fields.Many2one('res.users', string="Created By",track_visibility='onchange')
    last_modified_by_id = fields.Many2one('res.users', string="Last Modified By",track_visibility='onchange')
    opportunity_id = fields.Many2one('crm.lead', string="Opportunity",track_visibility='onchange')
    carrier = fields.Char('Operadora',track_visibility='onchange')
    name = fields.Char('Opportunity Product Name',track_visibility='onchange')
    product = fields.Many2one('product.product', string="Product",track_visibility='onchange')
    winner = fields.Boolean('Ganhou',track_visibility='onchange')
    reimbursement_value_type = fields.Selection([
        ('Fixed','Fixed'),
        ('Percentage','Percentage'),
    ],string="Reimbursement Value Type",track_visibility='onchange')
    life = fields.Integer('Vidas',size=18,track_visibility='onchange')
    reimbursement_value = fields.Float('Reimbursement Value',digits=(3,2),track_visibility='onchange')
    consultation_reimbursement = fields.Float('Consultation Reimbursement',track_visibility='onchange')


class SalesforceOpportunityTeamMember(models.Model):
    _name = 'crm.lead.team_member'
    _inherit = 'mail.thread'
    _description = 'Salesforce Opportunity Team Member'

    user_id = fields.Many2one('res.users', string="User",track_visibility='onchange')
    created_by_id = fields.Many2one('res.users', string="Created By",track_visibility='onchange')
    last_modified_by_id = fields.Many2one('res.users', string="Last Modified By",track_visibility='onchange')
    opportunity_id = fields.Many2one('crm.lead', string="Opportunity",track_visibility='onchange')
    opportunity_access_level = fields.Selection([
        ('', ''),
    ], string="Opportunity Access",track_visibility='onchange')
    team_role = fields.Selection([
        ('Analista de Cotação', 'Analista de Cotação'),
        ('Analista de Implantação', 'Analista de Implantação'),
        ('Sales Rep', 'Consultor Comercial'),
        ('Account Manager', 'Gerente de Conta'),
        ('Gerente de Relacionamento', 'Gerente de Relacionamento'),
        ('Sales Manager', 'Gerente de Vendas'),
        ('Channel Manager', 'Gerente do Canal de Venda'),
        ('indication', 'Indicação'),
        ('Pre-Sales Consultant', 'Pré-Consultor'),
        ('Executive Sponsor', 'Sponsor'),
    ], string="Member Role",track_visibility='onchange')


class SalesforceOpportunityStageParameter(models.Model):
    _name = 'crm.lead.stage.parameter'
    _inherit = 'mail.thread'
    _description = 'Salesforce Opportunity StageParameter'

    user_id = fields.Many2one('res.users', string="User",track_visibility='onchange')
    developer_name = fields.Char('Custom Metadata Record Name',size=40,track_visibility='onchange')
    master_label = fields.Char('Label',size=40,track_visibility='onchange')
    namespace_prefix = fields.Char('Namespace Prefix',track_visibility='onchange')
    last_modified_by_id = fields.Many2one('res.users', string="Last Modified By",track_visibility='onchange')
    is_protected = fields.Boolean('Protected Component',track_visibility='onchange')
    opportunity_stage = fields.Selection([
        ('Aberto','Aberto'),
        ('Visita','Visita'),
        ('Estudo','Estudo'),
        ('Negociação','Negociação'),
        ('Liberado para Implantação','Liberado para Implantação'),
        ('Devolução','Devolução'),
        ('Aguardando Documentação','Aguardando Documentação'),
        ('Proposta Operadora','Proposta Operadora'),
        ('Em Implantação Operadora','Em Implantação Operadora'),
        ('Crítica','Crítica'),
        ('Fechada','Fechada'),
        ('Perdida','Perdida'),
    ],string="Opportunity Stage",track_visibility='onchange')
    process = fields.Char('Process',size=255,track_visibility='onchange')


class SalesforceOpportunityStagePath(models.Model):
    _name = 'crm.lead.stage.path'
    _inherit = 'mail.thread'
    _description = 'Salesforce Opportunity StagePath'

    user_id = fields.Many2one('res.users', string="User",track_visibility='onchange')
    developer_name = fields.Char('Custom Metadata Record Name',size=40,track_visibility='onchange')
    master_label = fields.Char('Label',size=40,track_visibility='onchange')
    namespace_prefix = fields.Char('Namespace Prefix',track_visibility='onchange')
    last_modified_by_id = fields.Many2one('res.users', string="Last Modified By",track_visibility='onchange')
    is_protected = fields.Boolean('Protected Component',track_visibility='onchange')
    current_stage = fields.Char('Current Stage',size=255,track_visibility='onchange')
    next_stage = fields.Char('Next Stage',size=255,track_visibility='onchange')