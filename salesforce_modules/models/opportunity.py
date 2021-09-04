from odoo import models, fields, api

class SalesforceOpprtunity(models.Model):
    _inherit = 'crm.lead'
    _description = "Salesforce Opportunity"

    absence = fields.Integer('Absence')
    account_id = fields.Many2one('account.account', string='Account Name')
    actual_tax = fields.Float("Actual Tax")
    administrator_id = fields.Many2one('account.account', string='Administrator')
    amount = fields.Float('Amount')
    policy_expiration = fields.Selection([
        ('Dezembro', 'Dezembro'),
        ('Novembro', 'Novembro'),
        ('Agosto', 'Agosto'),
        ('Julho', 'Julho'),
        ('Outubro', 'Outubro'),
        ('Março', 'Março'),
        ('Abril', 'Abril'),
        ('Fevereiro	', 'Fevereiro	'),
        ('Setembro', 'Setembro'),
        ('Junho', 'Junho'),
        ('Maio', 'Maio'),
        ('Janeiro', 'Janeiro'),
    ],default='Janeiro', string="Aniversário da Apólice") # order is according to salesforce object
    actual_birth_policy_order = fields.Text('Aniversário da Apólice Atual Ordem')
    benefits = fields.Selection([
        ('Health', 'Saúde'),
        ('Dental', 'Odontológico'),
        ('Life', 'Vida'),
        ('Medicine', 'Medicamento'),
        ('Personal_Accidents', 'Acidente Pessoal'),
        ('In_Company', 'Consultoria'),
        ('Medical_Consulting', 'Consultoria Médica'),
        ('Meal', 'Refeição'),
        ('Food', 'Alimentação'),
        ('Transportation', 'Transporte'),
        ('Pension', 'Previdência'),
        ('Travel', 'Viagem'),
        ('Car_Fleet', 'Frota'),
        ('Car', 'Automóvel'),
        ('Fuel', 'Combustível'),
        ('Occupational_Health', 'Saúde Ocupacional'),
        ('Checkup', 'Check-up'),
        ('Vaccine', 'Vacina'),
        ('eu_protegido', 'Eu Protegido'),
        ('Fee', 'Fee')], string="Benefit")
    broker_value = fields.Float('Broker Value')
    broking = fields.Float('Broking (%)')
    budget_confirmed = fields.Boolean('Budget Confirmed')
    calculation_basis = fields.Selection([
        ('Sobre Agenciamento','Sobre Agenciamento'),
        ('Sobre Comissão','Sobre Comissão'),
    ], string="Calculation Basis")
    capital = fields.Selection([
        ('Uniforme', 'Uniforme'),
        ('Múltiplo', 'Múltiplo'),
        ('Escalonado', 'Escalonado'),
        ('Livre escolha', 'Livre escolha'),
        ('Global', 'Global'),
    ], string="Capital")
    child_with_disability = fields.Integer('Child With Disability')
    claim_limit = fields.Float('Claim Limit')
    account_rating = fields.Text('Classificação da Conta')
    contract_rating_del = fields.Selection([
        ('Small', 'Receita <40k'),
        ('Small_Large', 'Receita entre 40k e100k'),
        ('Middle', 'Receita entre 100k e 250k'),
        ('Middle_Large', 'Receita entre 250k e 400k'),
        ('Corporate', 'Receita entre 400k e 1MM'),
        ('Corporate_Large', 'Receita >1MM'),
    ], string="Classificação do Contrato")
    close_date = fields.Date('Close Date')
    account_cnpj = fields.Text('CNPJ da Conta')
    commision = fields.Float('Comission (%)')
    commision_value = fields.Float('Comission Value')
    complex_test = fields.Text('Complex Test')
    additional_driver = fields.Many2one('account.account', string='Condutor Adicional')
    contract_id = fields.Many2one('hr.contract', 'Contract')
    contrib_devol_paid_by_broker = fields.Selection([
        ('Sem Contribuição/Devolução','Sem Contribuição/Devolução'),
        ('Por Valor Fixo','Por Valor Fixo'),
        ('Por Percentual','Por Percentual'),
        ('Por Modelo','Por Modelo'),
    ], string="Contribuition/Devol. Paid By Broker")
    contributory_description = fields.Text('Contributory Description')
    contributory_value = fields.Float('Contributory Value')
    contributory = fields.Selection([
        ('Por Faixa Salarial','Por Faixa Salarial'),
        ('Por Percentual','Por Percentual'),
        ('Sem Contributariedade','Sem Contributariedade'),
    ], string="Contributário")
    coverage_limit_value = fields.Float('Coverage Limit Value')
    cpf = fields.Text('CPF')
    user_id = fields.Many2one('res.users', string="Created By")
    current_generators = fields.Text('Current Generator(s)')
    policy_anniversary_date = fields.Date('Data Aniversário da Apólice')
    cut_off_date = fields.Integer('Data de Corte')
    due_date = fields.Date('Data de Vencimento')
    days_in_current_status = fields.Integer('Days In Current Status')
    Ddelivery_installation_status = fields.Selection([
        ('In progress','In progress'),
        ('Yet to begin','Yet to begin'),
        ('Completed','Completed'),
    ], string="Delivery/Installation Status")
    deployment_talk = fields.Boolean('Deployment Talk')
    description = fields.Text('Description')
    destination = fields.Selection([
        ('América do Norte','América do Norte'),
        ('América Central','América Central'),
        ('América do Sul','América do Sul'),
        ('Europa','Europa'),
        ('África, Ásia','África, Ásia'),
        ('Ásia','Ásia'),
        ('Oceania','Oceania'),
        ('Múltiplos destinos','Múltiplos destinos'),
        ('Brasil','Brasil'),
    ], string="Destino"),
    discovery_completed = fields.Boolean('Discovery Completed')
    emergency_room_appointment = fields.Text('Emergency Room Appointment')
    expected_revenue = fields.Float('Expected Revenue')
    external_id = fields.Text('External Id')
    moderator_variable = fields.Selection([
        ('Sem Fator Moderador','Sem Fator Moderador'),
        ('Coparticipacao_Revertida_Empresa','Revertida para Empresa'),
        ('Coparticipacao_Revertida_para_Operadora','Revertida para Operadora'),
        ('Franquia','Franquia'),
    ], string="Fator Moderador")
    fee = fields.Float('Fee')
    contract_end = fields.Date('Fim do Contrato')
    fired = fields.Integer('Fired')
    mailing_origin = fields.Char('Fonte do Mailing')
    ForecastCategoryName = fields.Selection([
        ('Omitted','Omitido'),
        ('Pipeline','Pipeline'),
        ('Best Case','Valor de referência'),
        ('Commit','Confirmação'),
        ('Closed','Fechado'),
    ], string="Forecast Category")
    frequency = fields.Many2one('periodicity', string='Frequency') #New Model
    employee = fields.Integer('Funcionários')
    funeral_assistance = fields.Boolean('Funeral Assistance')
    funeral_assistance_value = fields.Float('Funeral Assistance Value')
    has_checkup = fields.Boolean('Has Checkup?')
    home_care = fields.Integer('Home Care')
    hospitalization = fields.Text('Hospilization')
    household = fields.Integer('Household')
    nominative = fields.Boolean('Indicado')
    cancel_information = fields.Text('Informações para Cancelamento')
    broker_number_benefit = fields.Integer('Installment Number - Broker')
    comission_number_benefit = fields.Integer('Installment Number - Comission')
    fee_number_benefit = fields.Integer('Installment Number - Fee')
    interns = fields.Integer('Interns')
    invoice = fields.Float('Invoice')
    broker_schedule_start = fields.Date('Início Agendamento - Agenciamento')
    comission_schedule_start = fields.Date('Início Agendamento - Comissão')
    fee_schedule_start = fields.Date('Início Agendamento - Fee')
    credit_start = fields.Integer('Início do Crédito')
    is_trigger = fields.Boolean('IsTrigger')
    last_modified_by_id = fields.Many2one('res.users', string="Last Modified By")
    lead_source = fields.Selection([
        ('Cotador','Cotador'),
        ('Evento_do_Cliente','Evento do Cliente'),
        ('Exposição','Exposição'),
        ('Google_AdWords','Google AdWords'),
        ('Indicação de funcionário','Indicação de funcionário'),
        ('Mailing','Mailing'),
        ('Parceiro','Parceiro'),
        ('Propaganda','Propaganda'),
        ('Site','Site'),
        ('Webinar','Webinar'),
        ('Outros','Outros'),
    ],string="Lead Source")
    life = fields.Integer('Life')
    life_contract = fields.Integer('Life Contract')
    lost_comment = fields.Char('Lost Comment')
    mainly_carrier = fields.Char('Mainly Carrier')
    brand = fields.Char('Marca')
    max_capital_limit = fields.Float('Max Capital Limit')
    medical_appointment = fields.Char('Medical Appointment')
    min_capital_limit = fields.Float('Min Capital Limit')
    Payment_Mode = fields.Selection([
        ('pre_pagamento','Pré-pagamento'),
        ('pos_pagamento','Pós-pagamento'),
    ],string="Modalidade de Pagamento")
    fee_model = fields.Selection([
        ('Small','Small'),
        ('Rebate','Rebate'),
    ],string="Model")
    modelo_id = fields.Many2one('Modelo',string="Modelo")  #model not created yet
    moderator_variable_value = fields.Float('Moderator Variable Value')
    motive_of_gain = fields.Selection([
        ('Expertise','Expertise'),
        ('Gestão de Sinistro','Gestão de Sinistro'),
        ('Preço','Preço'),
        ('Relacionamento','Relacionamento'),
        ('Serviço','Serviço'),
    ],string="Motivo de Ganho")
    loss_reason = fields.Selection([
        ('Amarra contratual', 'Amarra contratual'),
        ('Benefício flexível', 'Benefício flexível'),
        ('Broker mundial', 'Broker mundial'),
        ('Convertido', 'Convertido'),
        ('Alto risco', 'Declinado'),
        ('Expertise', 'Expertise'),
        ('Pesquisa de mercado', 'Pesquisa de mercado'),
        ('Price', 'Preço'),
        ('Rede', 'Rede'),
        ('Relacionamento', 'Relacionamento'),
        ('Serviço', 'Serviço'),
        ('Other', 'Other'),
    ], string="Motivo de Perda")
    next_step = fields.Char('Next Step')
    contract_carrier = fields.Many2one('account.account', string='Operadora do Contrato')
    name = fields.Char('Opportunity Name')


class SalesforcePeriodicity(models.Model):
    _name = 'periodicity'
    _description = "Salesforce Periodicity"

    every = fields.Integer('A Cada')
    user_id = fields.Many2one('res.users', string="Created By")
    Day_of_the_Week = fields.Selection([
        ('Domingo','Domingo'),
        ('Segunda-feira','Segunda-feira'),
        ('Terça-feira','Terça-feira'),
        ('Quarta-feira','Quarta-feira'),
        ('Quinta-feira','Quinta-feira'),
        ('Sexta-feira','Sexta-feira'),
        ('Sábado','Sábado'),
    ], string="Dia da Semana")
    end = fields.Date('Fim')
    start = fields.Datetime('Início')
    last_modified_by_id = fields.Many2one('res.users', string="Last Modified By")
    month = fields.Selection([   # this should be a multiselect picklist
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
    ], string="Mês")
    order = fields.Selection([
        ('Primeira (o)','Primeira (o)'),
        ('Segunda (o)','Segunda (o)'),
        ('Terceira (o)','Terceira (o)'),
        ('Quarta (o)','Quarta (o)'),
        ('Última (o)','Última (o)'),
    ],string="Ordem")
    name = fields.char('Periodicidade')
    # periodicity_id = fields.Integer('Periodicidade ID')   autogenerating  Id of the records
    recurrence = fields.Integer('Recorrência')