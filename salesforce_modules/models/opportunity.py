from odoo import models, fields, api


class SalesforceOpprtunity(models.Model):
    _inherit = 'crm.lead'
    _description = "Salesforce Opportunity"

    absence = fields.Integer('Absence',size=6)
    account_id = fields.Many2one('account.account', string='Account Name')
    actual_tax = fields.Float("Actual Tax",digits=(16,2))
    administrator_id = fields.Many2one('account.account', string='Administrator')
    amount = fields.Float('Amount',digits=(16,2))
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
    broker_value = fields.Float('Broker Value',digits=(16,2))
    broking = fields.Float('Broking (%)',digits=(16,2))
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
    child_with_disability = fields.Integer('Child With Disability',size=6)
    claim_limit = fields.Float('Claim Limit',digits=(3,2))
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
    commision = fields.Float('Comission (%)',digits=(16,2))
    commision_value = fields.Float('Comission Value',digits=(16,2))
    complex_tests = fields.Char('Complex Test',size=255)
    additional_driver = fields.Many2one('account.account', string='Condutor Adicional')
    contract_id = fields.Many2one('hr.contract', 'Contract')
    contrib_devol_paid_by_broker = fields.Selection([
        ('Sem Contribuição/Devolução','Sem Contribuição/Devolução'),
        ('Por Valor Fixo','Por Valor Fixo'),
        ('Por Percentual','Por Percentual'),
        ('Por Modelo','Por Modelo'),
    ], string="Contribuition/Devol. Paid By Broker")
    contributory_descriptions = fields.Char('Contributory Description',size=255)
    contributory_value = fields.Float('Contributory Value',digits=(5,2))
    contributory = fields.Selection([
        ('Por Faixa Salarial','Por Faixa Salarial'),
        ('Por Percentual','Por Percentual'),
        ('Sem Contributariedade','Sem Contributariedade'),
    ], string="Contributário")
    coverage_limit_value = fields.Float('Coverage Limit Value',digits=(5,2))
    cpf = fields.Text('CPF')
    user_id = fields.Many2one('res.users', string="Created By")
    current_generators = fields.Text('Current Generator(s)',size=100)
    policy_anniversary_date = fields.Date('Data Aniversário da Apólice')
    cut_off_date = fields.Integer('Data de Corte',size=2)
    due_date = fields.Date('Data de Vencimento')
    days_in_current_status = fields.Integer('Days In Current Status')
    delivery_installation_status = fields.Selection([
        ('In progress','In progress'),
        ('Yet to begin','Yet to begin'),
        ('Completed','Completed'),
    ], string="Delivery/Installation Status")
    deployment_talk = fields.Boolean('Deployment Talk')
    description = fields.Text('Description',size=32000)
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
    emergency_room_appointments = fields.Char('Emergency Room Appointment',size=255)
    expected_revenue = fields.Float('Expected Revenue',digits=(16,2))
    externals_id = fields.Char('External Id',size=255)
    moderator_variable = fields.Selection([
        ('Sem Fator Moderador','Sem Fator Moderador'),
        ('Coparticipacao_Revertida_Empresa','Revertida para Empresa'),
        ('Coparticipacao_Revertida_para_Operadora','Revertida para Operadora'),
        ('Franquia','Franquia'),
    ], string="Fator Moderador")
    fee = fields.Float('Fee',digits=(16,2))
    contract_end = fields.Date('Fim do Contrato')
    fired = fields.Integer('Fired',size=6)
    mailing_origin = fields.Char('Fonte do Mailing',size=255)
    forecast_category_name = fields.Selection([
        ('Omitted','Omitido'),
        ('Pipeline','Pipeline'),
        ('Best Case','Valor de referência'),
        ('Commit','Confirmação'),
        ('Closed','Fechado'),
    ], string="Forecast Category")
    frequency = fields.Many2one('model.periodicity', string='Frequency') #New Model hence removed
    employee = fields.Integer('Funcionários',size=18)
    funeral_assistance = fields.Boolean('Funeral Assistance')
    funeral_assistance_value = fields.Float('Funeral Assistance Value',digits=(16,2))
    has_checkup = fields.Boolean('Has Checkup?')
    home_care = fields.Integer('Home Care',size=6)
    hospitalization = fields.Text('Hospilization')
    household = fields.Integer('Household',size=6)
    nominative = fields.Boolean('Indicado')
    cancel_information = fields.Text('Informações para Cancelamento',size=32768)
    broker_number_benefit = fields.Integer('Installment Number - Broker',size=18)
    comission_number_benefit = fields.Integer('Installment Number - Comission',size=18)
    fee_number_benefit = fields.Integer('Installment Number - Fee',size=18)
    interns = fields.Integer('Interns',size=6)
    invoice = fields.Float('Invoice',digits=(16,2))
    broker_schedule_start = fields.Date('Início Agendamento - Agenciamento')
    comission_schedule_start = fields.Date('Início Agendamento - Comissão')
    fee_schedule_start = fields.Date('Início Agendamento - Fee')
    credit_start = fields.Integer('Início do Crédito',size=2)
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
    life = fields.Integer('Life',size=18)
    life_contract = fields.Integer('Life Contract',size=18)
    lost_comment = fields.Char('Lost Comment',size=255)
    mainly_carrier = fields.Char('Mainly Carrier',size=255)
    brand = fields.Char('Brand')
    max_capital_limit = fields.Float('Max Capital Limit',digits=(16,2))
    medical_appointment = fields.Char('Medical Appointment',size=255)
    min_capital_limit = fields.Float('Min Capital Limit',digits=(16,2))
    payment_mode = fields.Selection([
        ('pre_pagamento','Pré-pagamento'),
        ('pos_pagamento','Pós-pagamento'),
    ],string="Modalidade de Pagamento")
    fee_model = fields.Selection([
        ('Small','Small'),
        ('Rebate','Rebate'),
    ],string="Model")
    modelo_id = fields.Many2one('Modelo',string="Modelo")  #model not created yet
    moderator_variable_value = fields.Float('Moderator Variable Value',digits=(5,2))
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
    next_step = fields.Char('Next Step',size=255)
    contract_carrier = fields.Many2one('account.account', string='Operadora do Contrato')
    name = fields.Char('Opportunity Name',size=120)
    owner_id = fields.Many2one('res.users', string="Opportunity Owner")
    iq_score = fields.Integer('Opportunity Score',size=9)
    order_number = fields.Char('Order Number',size=8)
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
    orthodontics = fields.Char('Orthodontics',size=255)
    others = fields.Char('Others',size=255)
    partner_account_id = fields.Many2one('account.account', string='Partner Account')
    partnership = fields.Many2one('account.account', string='Partnership')
    pension_mode = fields.Selection([
        ('Plano Averbado', 'Plano Averbado'),
        ('	Plano Instituído', '	Plano Instituído'),
    ], string="Pension Mode")
    periodicity_renewal = fields.Integer('Periodicity Renewal',size=3)
    grace_period = fields.Integer('Período de Carência',size=18)
    tag = fields.Char('Placa',size=7)
    places = fields.Text('Places',size=32768)
    has_dps = fields.Boolean('Possui DPS')
    main_competitors = fields.Char('Principais Concorrentes',size=100)
    is_private = fields.Boolean('Private')
    probability = fields.Float('Probability (%)',digits=(3,2))
    prosthesis = fields.Char('Prosthesis',size=255)
    provider = fields.Many2one('account.account', string='Provider')
    purchase_limit = fields.Selection([
        ('Valor fixo','Valor fixo'),
        ('Percentual do salário','Percentual do salário'),
    ], string="Purchase Limit")
    purchase_limit_value = fields.Float('Purchase Limit Value',digits=(5,2))
    number_of_installments = fields.Integer('Quantidade de Parcelas',size=3)
    total_opportunity_quantity = fields.Float('Quantity',digits=(16,2))
    rebate = fields.Float('Rebate',digits=(3,2))
    redeemed = fields.Integer('Redeemed',size=6)
    renavam = fields.Integer('RENAVAM',size=11)
    reserve = fields.Char('Reserva')
    market_reserve = fields.Char('Reserva de Mercado',size=28)
    reserve_days = fields.Integer('Reserve - Days')
    retired = fields.Integer('Retired',size=6)
    returned_reason = fields.Char('Returned Reason',size=255)
    revenue = fields.Float('Revenue')
    revenue_politic = fields.Float('Revenue Policy',digits=(16,2))
    roi_analysis_completed = fields.Boolean('ROI Analysis Completed')
    service_supplier = fields.Integer('Service Supplier',size=6)
    simple_test = fields.Char('Simple Test',size=255)
    sons_capital_limit = fields.Boolean('Sons Capital Limit',digits=(16,2))
    special_condition = fields.Char('Special Condition',size=131072)
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
    administration_tax = fields.Float('Taxa de Administração',digits=(3,2))
    charge_rate = fields.Float('Taxa de Carregamento',digits=(3,2))
    emergencial_card_fee = fields.Float('Taxa de Cartão Emergencial',digits=(3,2))
    availability_fee = fields.Float('Taxa de Disponibilização',digits=(3,2))
    issuance_cost = fields.Float('Taxa de Emissão',digits=(3,2))
    delivery_fee = fields.Float('Taxa de Entrega',digits=(3,2))
    output_rate = fields.Float('Taxa de Saída',digits=(3,2))
    replace_fee = fields.Float('Taxa de Segunda Via',digits=(3,2))
    therapy = fields.Char('Therapy',size=255)
    income_type = fields.Selection([
        ('Renda Temporária','Renda Temporária'),
        ('Renda Vitalícia','Renda Vitalícia'),
        ('Renda Vitalícia Reversível ao Beneficiário','Renda Vitalícia Reversível ao Beneficiário'),

    ],string="Tipo de Renda")
    Tax_Type = fields.Selection([
        ('Regressiva Definitiva', 'Regressiva Definitiva'),
        ('Progressiva Compensável', 'Progressiva Compensável'),
    ], string="Tipo de Tributação")
    total_capital = fields.Float(string="Total Capital", digits=(16, 2))
    tracking_number = fields.Char('Tracking Number',size=12)
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
    broker_first_installment_value = fields.Float('Valor da Primeira Parcela - Agenciamento', digits=(16, 2))
    comission_first_installment_value = fields.Float('Valor da Primeira Parcela - Comissão', digits=(16, 2))
    fee_first_installment_value = fields.Float('Valor da Primeira Parcela - Fee', digits=(18, 0))
    monthly_average_value = fields.Float('Valor Médio Mensal', digits=(4, 2))
    wage_limit_amount = fields.Float('Wage Limit Amount', digits=(16, 2))
    wage_limit_for_coparticipation = fields.Selection([
        ('Não possui','Não possui'),
        ('Por Percentual','Por Percentual'),
        ('Por Valor Fixo','Por Valor Fixo'),
    ],string="Wage Limit For Coparticipation")
    workflow_configuration = fields.Many2one('workflow_configuration', string="Workflow Configuration")
    campaigns_id = fields.Many2one('model_campaign',string ='Primary Campaign Source',ondelete='cascade')
    model_id   = fields.Many2one('ir.model', string='Model ID')
    channel_id = fields.Many2one('channel_segmentation', string='Channel Id')

    quotation = fields.Many2one('model_quote', string='Quotation')
    synced_quote_id = fields.Many2one('model_quote', string='Synced Quote')
    opportunity_team_lines = fields.One2many('crm.lead.team_member','opportunity_id', string="Opportunity Team Lines")
    contact_role_lines = fields.One2many('crm.lead.contact.role','opportunity_id',string="Contact Role Lines")
    contact_partner_lines = fields.One2many('contract.partner','opportunity_id',string="Contact Partner Lines")
    quote_lines = fields.One2many('model_quote','OpportunityId',string="Quotes Lines")
    competitor_lines = fields.One2many('crm.lead.competitor','opportunity_id',string="Competitor Lines")
    attachment_lines = fields.One2many('ir.attachment','opportunity_id',string="Attachment Lines")
    product_lines = fields.One2many('crm.lead.product','opportunity_id',string="Product Lines")
    case_lines = fields.One2many('model_case','opportunity_id',string="Case Lines")