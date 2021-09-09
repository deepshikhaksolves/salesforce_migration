from odoo import models, fields, api


class ContractTeam(models.Model):
    _name = 'contract_team'
    _description = "Salesforce Contract Team"
    _rec_name = 'user_id'


    contract_id             = fields.Many2one('hr.contract', string='Contract')
    # CreatedById already in odoo
    name                    = fields.Char('ID')
    key                     = fields.Char('Key', size=255)
    # LastModifiedById already in odoo
    OwnerId                 = fields.Many2one('res.users',string='Owner')
    team_role               = fields.Selection([('pre_sales_consultant','Pré-Consultor'),('sales_rep','Consultor de Vendas'),('sales_manager','Gerente de Vendas'),('sales_director','Diretor de Vendas'),('service_desk','Posto de Atendimento'),('relationship_assistant','Assistente de Relacionamento')],'Team Role')
    user_id                 = fields.Many2one('res.users', string='User')

