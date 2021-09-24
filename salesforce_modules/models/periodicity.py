from odoo import models, fields, api


class SalesforcePeriodicity(models.Model):
    _name = 'model.periodicity'
    _inherit = 'mail.thread'
    _description = "Salesforce Periodicity"

    every = fields.Integer('A Cada',size=3,track_visibility='onchange')
    user_id = fields.Many2one('res.users', string="Created By",track_visibility='onchange')
    day_of_the_week = fields.Selection([
        ('Domingo', 'Domingo'),
        ('Segunda-feira', 'Segunda-feira'),
        ('Terça-feira', 'Terça-feira'),
        ('Quarta-feira', 'Quarta-feira'),
        ('Quinta-feira', 'Quinta-feira'),
        ('Sexta-feira', 'Sexta-feira'),
        ('Sábado', 'Sábado'),
    ], string="Dia da Semana",track_visibility='onchange')
    end = fields.Date('Fim',track_visibility='onchange')
    start = fields.Datetime('Início',track_visibility='onchange')
    last_modified_by_id = fields.Many2one('res.users', string="Last Modified By",track_visibility='onchange')
    month = fields.Selection([  # this should be a multiselect picklist
        ('Janeiro', 'Janeiro'),
        ('Fevereiro', 'Fevereiro'),
        ('Março', 'Março'),
        ('Abril', 'Abril'),
        ('Maio', 'Maio'),
        ('Junho', 'Junho'),
        ('Julho', 'Julho'),
        ('Agosto', 'Agosto'),
        ('Setembro', 'Setembro'),
        ('Outubro', 'Outubro'),
        ('Novembro', 'Novembro'),
        ('Dezembro', 'Dezembro'),
    ], string="Mês",track_visibility='onchange')
    order = fields.Selection([
        ('Primeira (o)','Primeira (o)'),
        ('Segunda (o)','Segunda (o)'),
        ('Terceira (o)','Terceira (o)'),
        ('Quarta (o)','Quarta (o)'),
        ('Última (o)','Última (o)'),
    ],string="Ordem",track_visibility='onchange')
    name = fields.Char('Periodicidade',size=80,track_visibility='onchange')
    # periodicity_id = fields.Integer('Periodicidade ID')   autogenerating  Id of the records
    recurrence = fields.Integer('Recorrência',size=3,track_visibility='onchange')
    pattern = fields.Selection([
        ('Dia', 'Dia'),
        ('Semana', 'Semana'),
        ('Mês', 'Mês'),
        ('Ano', 'Ano'),
    ], string="Padrão",track_visibility='onchange')
    service_lines = fields.One2many('model_service_c', 'periodicity_id', string="Service Lines")
    opportunity_lines = fields.One2many('crm.lead','frequency',string="Opportunity Lines")