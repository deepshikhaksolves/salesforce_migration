from odoo import models, fields, api


class SalesforcePlanCoverage(models.Model):
    _name = 'plan.coverage'
    _inherit = 'mail.thread'
    _description = 'Salesforce Plan Coverage'

    name = fields.Char('Coverage')
    coverage = fields.Selection([
        ('Consulta', 'Consulta'),
        ('Exame', 'Exame'),
        ('Pronto-socorro', 'Pronto-socorro'),
        ('Internação clínica e cirúrgica', 'Internação clínica e cirúrgica'),
        ('Psicoterapia de crise (até 40 sessões/ano', 'Psicoterapia de crise (até 40 sessões/ano'),
        ('Cirurgia de miopia a partir de 5 graus', 'Cirurgia de miopia a partir de 5 graus'),
        ('Nutricionista (até 12 consultas/ano)', 'Nutricionista (até 12 consultas/ano)'),
        ('Terapia ocupacional (até 40 consultas/ano)', 'Terapia ocupacional (até 40 consultas/ano)'),
        ('Fonoaudiologia (até 24 consultas/ano)', 'Fonoaudiologia (até 24 consultas/ano)'),
        ('Transplante córnea, rim e medula óssea', 'Transplante córnea, rim e medula óssea'),
        ('Transplantes', 'Transplantes'),
        ('Cirurgia miopia', 'Cirurgia miopia'),
        ('Remissão por morte titular', 'Remissão por morte titular'),
        ('Prazo de reembolso', 'Prazo de reembolso'),
        ('Equipe de retaguarda', 'Equipe de retaguarda'),
        ('Vacinas', 'Vacinas'),
        ('Assistencia viagem', 'Assistencia viagem'),
        ('Check up', 'Check up'),
        ('Validade e custo do cartão', 'Validade e custo do cartão'),
        ('Período de reavaliação', 'Período de reavaliação'),
        ('Tipo de contratação', 'Tipo de contratação'),
        ('Serviços prestados', 'Serviços prestados'),
        ('Autorização prévia', 'Autorização prévia'),
        ('Análise sinistralidade', 'Análise sinistralidade'),
        ('Prazo do contrato', 'Prazo do contrato'),
        ('Custo do cartão', 'Custo do cartão'),
        ('Carências', 'Carências'),
        ('Dependentes', 'Dependentes'),
        ('Acidente de trabalho', 'Acidente de trabalho'),
        ('Rede de atendimento', 'Rede de atendimento'),
    ], string="Coverage")
    condition = fields.Char('Condition')
    user_id = fields.Many2one('res.users', string="Created By")
    operator_description = fields.Char('Description in the Operator')
    start_of_coverage = fields.Date('Start of Coverage')
    end_of_coverage = fields.Date('End of Coverage')
    plan_id = fields.Many2one('product.product', 'Plano')
    last_modified_by_id = fields.Many2one('res.users', string="Last Modified By")
    owner_id = fields.Many2one('account.account', string='Owner')
