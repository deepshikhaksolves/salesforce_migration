from odoo import models, fields, api


class SalesforceOpportunityContactRole(models.Model):
    _name = 'crm.lead.contact.role'
    _description = 'Salesforce Opportunity Contact Role'

    contact_id = fields.Many2one('res.user', string="Contact ID")
    user_id = fields.Many2one('res.users', string="Created By")
    last_modified_by_id = fields.Many2one('res.users', string="Last Modified By")
    opportunity_id = fields.Many2one('crm.lead', string="Opportunity")
    is_primary = fields.Boolean('Primary')
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
    ], string="Role")


class SalesforceOpportunityCompetitor(models.Model):
    _name = 'crm.lead.competitor'
    _description = 'Salesforce Opportunity Competitor'

    created_date = fields.Datetime(string="Created Date")
    last_modified_date = fields.Datetime(string="Last Modified Date")
    user_id = fields.Many2one('res.users', string="Created By")
    last_modified_by_id = fields.Many2one('res.users', string="Last Modified By")
    opportunity_id = fields.Many2one('crm.lead', string="Opportunity")
    is_deleted = fields.Boolean('Deleted')
    competitor_name = fields.Selection([
        ('', ''),
    ], string="Competitor Name")
    strengths = fields.Char('Strengths')
    weaknesses = fields.Char('Weaknesses')
    system_mod_stamp = fields.Datetime('System Modstamp')


class SalesforceOpportunityLineItem(models.Model):
    _name = 'crm.lead.lineitem'
    _description = 'Salesforce Opportunity Product'

    service_date = fields.Date(string="Date")
    user_id = fields.Many2one('res.users', string="Created By")
    last_modified_by_id = fields.Many2one('res.users', string="Last Modified By")
    opportunity_id = fields.Many2one('crm.lead', string="Opportunity")
    discount = fields.Float('Discount')
    quantity = fields.Float('Quantity')
    unit_price = fields.Float('Sales Price')
    Subtotal = fields.Float('Subtotal')
    TotalPrice = fields.Float('TotalPrice')
    list_price = fields.Float('List Price')
    description = fields.Char('Line Description')
    carrier = fields.Char('Operadora')
    name = fields.Char('Opportunity Product Name')
    product2Id = fields.Many2one('product.product', string="Product")
    product_code = fields.Char('Product Code')


class SalesforceOpportunityProduct(models.Model):
    _name = 'crm.lead.product'
    _inherit = 'mail.thread'
    _description = 'Salesforce Opportunity Product'

    user_id = fields.Many2one('res.users', string="Created By")
    last_modified_by_id = fields.Many2one('res.users', string="Last Modified By")
    opportunity_id = fields.Many2one('crm.lead', string="Opportunity")
    carrier = fields.Char('Operadora')
    name = fields.Char('Opportunity Product Name')
    product = fields.Many2one('product.product', string="Product")
    winner = fields.Boolean('Ganhou')
    reimbursement_value_type = fields.Selection([
        ('Fixed', 'Fixed'),
        ('Percentage', 'Percentage'),
    ], string="Reimbursement Value Type")
    life = fields.Integer('Vidas')
    reimbursement_value = fields.Float('Reimbursement Value')
    consultation_reimbursement = fields.Float('Consultation Reimbursement')


class SalesforceOpportunityTeamMember(models.Model):
    _name = 'crm.lead.team_member'
    _description = 'Salesforce Opportunity Team Member'

    user_id = fields.Many2one('res.users', string="User")
    created_by_id = fields.Many2one('res.users', string="Created By")
    last_modified_by_id = fields.Many2one('res.users', string="Last Modified By")
    opportunity_id = fields.Many2one('crm.lead', string="Opportunity")
    opportunity_access_level = fields.Selection([
        ('', ''),
    ], string="Opportunity Access")
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
    ], string="Team Role")


class SalesforceOpportunityStageParameter(models.Model):
    _name = 'crm.lead.stage.parameter'
    _description = 'Salesforce Opportunity StageParameter'

    user_id = fields.Many2one('res.users', string="User")
    developer_name = fields.Char('Custom Metadata Record Name')
    master_label = fields.Char('Label')
    namespace_prefix = fields.Char('Namespace Prefix')
    last_modified_by_id = fields.Many2one('res.users', string="Last Modified By")
    is_protected = fields.Boolean('Protected Component')
    opportunity_stage = fields.Selection([
        ('Aberto', 'Aberto'),
        ('Visita', 'Visita'),
        ('Estudo', 'Estudo'),
        ('Negociação', 'Negociação'),
        ('Liberado para Implantação', 'Liberado para Implantação'),
        ('Devolução', 'Devolução'),
        ('Aguardando Documentação', 'Aguardando Documentação'),
        ('Proposta Operadora', 'Proposta Operadora'),
        ('Em Implantação Operadora', 'Em Implantação Operadora'),
        ('Crítica', 'Crítica'),
        ('Fechada', 'Fechada'),
        ('Perdida', 'Perdida'),
    ], string="Opportunity Stage")
    process = fields.Char('Process')


class SalesforceOpportunityStagePath(models.Model):
    _name = 'crm.lead.stage.path'
    _description = 'Salesforce Opportunity StagePath'

    user_id = fields.Many2one('res.users', string="User")
    developer_name = fields.Char('Custom Metadata Record Name')
    master_label = fields.Char('Label')
    namespace_prefix = fields.Char('Namespace Prefix')
    last_modified_by_id = fields.Many2one('res.users', string="Last Modified By")
    is_protected = fields.Boolean('Protected Component')
    current_stage = fields.Char('Current Stage')
    next_stage = fields.Char('Next Stage')
