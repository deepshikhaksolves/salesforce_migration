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
    delivery_installation_status = fields.Selection([
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
    ], string="Destino")
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
    forecast_category_name = fields.Selection([
        ('Omitted','Omitido'),
        ('Pipeline','Pipeline'),
        ('Best Case','Valor de referência'),
        ('Commit','Confirmação'),
        ('Closed','Fechado'),
    ], string="Forecast Category")
    frequency = fields.Many2one('periodicity', string='Frequency') #New Model hence removed
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
    payment_mode = fields.Selection([
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
    owner_id = fields.Many2one('res.users', string="Opportunity Owner")
    iq_score = fields.Integer('Opportunity Score')
    order_number = fields.Char('Order Number')
    contract_origin = fields.Selection([
        ('Novo','Novo'),
        ('Cross Sell','Cross Sell'),
        ('Up Sell','Up Sell'),
        ('Reimplantação','Reimplantação'),
    ], string="Origem do Contrato")
    opportunity_event_source = fields.Selection([
        ('Estudo','Estudo'),
        ('Visita','Visita'),
    ], string="Origem do evento oportunidade")
    orthodontics = fields.Char('Orthodontics')
    others = fields.Char('Others')
    partner_account_id = fields.Many2one('account.account', string='Partner Account')
    partnership = fields.Many2one('account.account', string='Partnership')
    pension_mode = fields.Selection([
        ('Plano Averbado', 'Plano Averbado'),
        ('	Plano Instituído', '	Plano Instituído'),
    ], string="Pension Mode")
    periodicity_renewal = fields.Integer('Periodicity Renewal')
    grace_period = fields.Integer('Período de Carência')
    tag = fields.Char('Placa')
    places = fields.Text('Places')
    has_dps = fields.Boolean('Possui DPS')
    main_competitors = fields.Char('Principais Concorrentes')
    is_private = fields.Boolean('Private')
    probability = fields.Float('Probability (%)')
    prosthesis = fields.Char('Prosthesis')
    provider = fields.Many2one('account.account', string='Provider')
    purchase_limit = fields.Selection([
        ('Valor fixo','Valor fixo'),
        ('Percentual do salário','Percentual do salário'),
    ], string="Purchase Limit")
    purchase_limit_value = fields.Float('Purchase Limit Value')
    number_of_installments = fields.Integer('Quantidade de Parcelas')
    total_opportunity_quantity = fields.Float('Quantity')
    rebate = fields.Float('Rebate')
    redeemed = fields.Integer('Redeemed')
    renavam = fields.Integer('RENAVAM')
    reserve = fields.Char('Reserva')
    market_reserve = fields.Char('Reserva de Mercado')
    reserve_days = fields.Integer('Reserve - Days')
    retired = fields.Integer('Retired')
    returned_reason = fields.Char('Returned Reason')
    revenue = fields.Float('Revenue')
    revenue_politic = fields.Float('Revenue Politic')
    roi_analysis_completed = fields.Boolean('ROI Analysis Completed')
    service_supplier = fields.Integer('Service Supplier')
    simple_test = fields.Char('Simple Test')
    sons_capital_limit = fields.Boolean('Sons Capital Limit')
    special_condition = fields.Char('Special Condition')
    stage_name = fields.Selection([
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
    ],string="Stage")
    status_change_date = fields.Date('Status Change Date')
    administration_tax = fields.Float('Taxa de Administração')
    charge_rate = fields.Float('Taxa de Carregamento')
    emergencial_card_fee = fields.Float('Taxa de Cartão Emergencial')
    availability_fee = fields.Float('Taxa de Disponibilização')
    issuance_cost = fields.Float('Taxa de Emissão')
    delivery_fee = fields.Float('Taxa de Entrega')
    output_rate = fields.Float('Taxa de Saída')
    replace_fee = fields.Float('Taxa de Segunda Via')
    therapy = fields.Char('Therapy')
    income_type = fields.Selection([
        ('Renda Temporária','Renda Temporária'),
        ('Renda Vitalícia','Renda Vitalícia'),
        ('Renda Vitalícia Reversível ao Beneficiário','Renda Vitalícia Reversível ao Beneficiário'),

    ],string="Tipo de Renda")
    Tax_Type = fields.Selection([
        ('Regressiva Definitiva', 'Regressiva Definitiva'),
        ('Progressiva Compensável', 'Progressiva Compensável'),
    ], string="Tipo de Tributação")
    total_capital = fields.Float(string="Total Capital", digits=(16, 2) )
    tracking_number = fields.Char('Tracking Number')
    brokerage_transfer = fields.Boolean('Transferência de Corretagem')
    type_business = fields.Selection([
        ('Existing Business','Existing Business'),
        ('New Business','New Business'),
    ],string="Type")
    type_of_pension = fields.Selection([
        ('Aberto','Aberto'),
        ('Fechado','Fechado'),
    ],string="Type of Pension")
    type_of_revenue = fields.Selection([
        ('Pontual','Pontual'),
        ('Recorrente','Recorrente'),
    ],string="Type of Revenue")
    broker_first_installment_value = fields.Float('Valor da Primeira Parcela - Agenciamento')
    comission_first_installment_value = fields.Float('Valor da Primeira Parcela - Comissão')
    fee_first_installment_value = fields.Float('Valor da Primeira Parcela - Fee')
    monthly_average_value = fields.Float('Valor Médio Mensal')
    wage_limit_amount = fields.Float('Wage Limit Amount')
    wage_limit_for_coparticipation = fields.Selection([
        ('Não possui','Não possui'),
        ('Por Percentual','Por Percentual'),
        ('Por Valor Fixo','Por Valor Fixo'),
    ],string="Wage Limit For Coparticipation")
    workflow_configuration = fields.Many2one('workflow_configuration', string="Workflow Configuration")
    # campaign_id = fields.Many2one('model_campaign',string ='Primary Campaign Source',ondelete='cascade')


