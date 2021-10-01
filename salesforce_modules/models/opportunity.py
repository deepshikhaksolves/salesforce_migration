from odoo import models, fields, api


class SalesforceOpprtunity(models.Model):
    _inherit = 'crm.lead'
    _description = "Salesforce Opportunity"

    absence = fields.Integer('Absence',size=6,track_visibility='onchange')
    account_id = fields.Many2one('account.account', string='Account Name',track_visibility='onchange')
    actual_tax = fields.Float("Actual Tax",digits=(16,2),track_visibility='onchange')
    administrator_id = fields.Many2one('account.account', string='Administrator',track_visibility='onchange')
    amount = fields.Float('Amount',digits=(16,2),track_visibility='onchange')
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
    ],default='Janeiro', string="Aniversário da Apólice",track_visibility='onchange') # order is according to salesforce object
    actual_birth_policy_order = fields.Text('Aniversário da Apólice Atual Ordem',track_visibility='onchange')
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
        ('Fee', 'Fee')], string="Benefit",track_visibility='onchange')
    broker_value = fields.Float('Broker Value',digits=(16,2),track_visibility='onchange')
    broking = fields.Float('Broking (%)',digits=(16,2),track_visibility='onchange')
    budget_confirmed = fields.Boolean('Budget Confirmed',track_visibility='onchange')
    calculation_basis = fields.Selection([
        ('Sobre Agenciamento','Sobre Agenciamento'),
        ('Sobre Comissão','Sobre Comissão'),
    ], string="Calculation Basis",track_visibility='onchange')
    capital = fields.Selection([
        ('Uniforme', 'Uniforme'),
        ('Múltiplo', 'Múltiplo'),
        ('Escalonado', 'Escalonado'),
        ('Livre escolha', 'Livre escolha'),
        ('Global', 'Global'),
    ], string="Capital",track_visibility='onchange')
    child_with_disability = fields.Integer('Child With Disability',size=6,track_visibility='onchange')
    claim_limit = fields.Float('Claim Limit',digits=(3,2),track_visibility='onchange')
    account_rating = fields.Text('Classificação da Conta',track_visibility='onchange')
    contract_rating_del = fields.Selection([
        ('Small', 'Receita <40k'),
        ('Small_Large', 'Receita entre 40k e100k'),
        ('Middle', 'Receita entre 100k e 250k'),
        ('Middle_Large', 'Receita entre 250k e 400k'),
        ('Corporate', 'Receita entre 400k e 1MM'),
        ('Corporate_Large', 'Receita >1MM'),
    ], string="Classificação do Contrato",track_visibility='onchange')
    close_date = fields.Date('Close Date',track_visibility='onchange')
    account_cnpj = fields.Text('CNPJ da Conta',track_visibility='onchange')
    commision = fields.Float('Comission (%)',digits=(16,2),track_visibility='onchange')
    commision_value = fields.Float('Comission Value',digits=(16,2),track_visibility='onchange')
    complex_tests = fields.Char('Complex Test',size=255,track_visibility='onchange')
    additional_driver = fields.Many2one('account.account', string='Condutor Adicional',track_visibility='onchange')
    contract_id = fields.Many2one('hr.contract', 'Contract',track_visibility='onchange')
    contrib_devol_paid_by_broker = fields.Selection([
        ('Sem Contribuição/Devolução','Sem Contribuição/Devolução'),
        ('Por Valor Fixo','Por Valor Fixo'),
        ('Por Percentual','Por Percentual'),
        ('Por Modelo','Por Modelo'),
    ], string="Contribuition/Devol. Paid By Broker",track_visibility='onchange')
    contributory_descriptions = fields.Char('Contributory Description',size=255,track_visibility='onchange')
    contributory_value = fields.Float('Contributory Value',digits=(5,2),track_visibility='onchange')
    contributory = fields.Selection([
        ('Por Faixa Salarial','Por Faixa Salarial'),
        ('Por Percentual','Por Percentual'),
        ('Sem Contributariedade','Sem Contributariedade'),
    ], string="Contributário",track_visibility='onchange')
    coverage_limit_value = fields.Float('Coverage Limit Value',digits=(5,2),track_visibility='onchange')
    cpf = fields.Text('CPF',track_visibility='onchange')
    user_id = fields.Many2one('res.users', string="Created By",track_visibility='onchange')
    current_generators = fields.Text('Current Generator(s)',size=100,track_visibility='onchange')
    policy_anniversary_date = fields.Date('Data Aniversário da Apólice',track_visibility='onchange')
    cut_off_date = fields.Integer('Data de Corte',size=2,track_visibility='onchange')
    due_date = fields.Date('Data de Vencimento',track_visibility='onchange')
    days_in_current_status = fields.Integer('Days In Current Status',track_visibility='onchange')
    delivery_installation_status = fields.Selection([
        ('In progress','In progress'),
        ('Yet to begin','Yet to begin'),
        ('Completed','Completed'),
    ], string="Delivery/Installation Status",track_visibility='onchange')
    deployment_talk = fields.Boolean('Deployment Talk',track_visibility='onchange')
    description = fields.Text('Description',size=32000,track_visibility='onchange')
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
    ], string="Destino",track_visibility='onchange')
    discovery_completed = fields.Boolean('Discovery Completed',track_visibility='onchange')
    emergency_room_appointments = fields.Char('Emergency Room Appointment',size=255,track_visibility='onchange')
    expected_revenue = fields.Float('Expected Revenue',digits=(16,2),track_visibility='onchange')
    externals_id = fields.Char('External Id',size=255,track_visibility='onchange')
    moderator_variable = fields.Selection([
        ('Sem Fator Moderador','Sem Fator Moderador'),
        ('Coparticipacao_Revertida_Empresa','Revertida para Empresa'),
        ('Coparticipacao_Revertida_para_Operadora','Revertida para Operadora'),
        ('Franquia','Franquia'),
    ], string="Fator Moderador",track_visibility='onchange')
    fee = fields.Float('Fee',digits=(16,2),track_visibility='onchange')
    contract_end = fields.Date('Fim do Contrato',track_visibility='onchange')
    fired = fields.Integer('Fired',size=6,track_visibility='onchange')
    mailing_origin = fields.Char('Fonte do Mailing',size=255,track_visibility='onchange')
    forecast_category_name = fields.Selection([
        ('Omitted','Omitido'),
        ('Pipeline','Pipeline'),
        ('Best Case','Valor de referência'),
        ('Commit','Confirmação'),
        ('Closed','Fechado'),
    ], string="Forecast Category",track_visibility='onchange')
    frequency = fields.Many2one('model.periodicity', string='Frequency',track_visibility='onchange') #New Model hence removed
    employee = fields.Integer('Funcionários',size=18,track_visibility='onchange')
    funeral_assistance = fields.Boolean('Funeral Assistance',track_visibility='onchange')
    funeral_assistance_value = fields.Float('Funeral Assistance Value',digits=(16,2),track_visibility='onchange')
    has_checkup = fields.Boolean('Has Checkup?',track_visibility='onchange')
    home_care = fields.Integer('Home Care',size=6,track_visibility='onchange')
    hospitalization = fields.Text('Hospilization',track_visibility='onchange')
    household = fields.Integer('Household',size=6,track_visibility='onchange')
    nominative = fields.Boolean('Indicado',track_visibility='onchange')
    cancel_information = fields.Text('Informações para Cancelamento',size=32768,track_visibility='onchange')
    broker_number_benefit = fields.Integer('Installment Number - Broker',size=18,track_visibility='onchange')
    comission_number_benefit = fields.Integer('Installment Number - Comission',size=18,track_visibility='onchange')
    fee_number_benefit = fields.Integer('Installment Number - Fee',size=18,track_visibility='onchange')
    interns = fields.Integer('Interns',size=6,track_visibility='onchange')
    invoice = fields.Float('Invoice',digits=(16,2),track_visibility='onchange')
    broker_schedule_start = fields.Date('Início Agendamento - Agenciamento',track_visibility='onchange')
    comission_schedule_start = fields.Date('Início Agendamento - Comissão',track_visibility='onchange')
    fee_schedule_start = fields.Date('Início Agendamento - Fee',track_visibility='onchange')
    credit_start = fields.Integer('Início do Crédito',size=2,track_visibility='onchange')
    is_trigger = fields.Boolean('IsTrigger',track_visibility='onchange')
    last_modified_by_id = fields.Many2one('res.users', string="Last Modified By",track_visibility='onchange')
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
    ],string="Lead Source",track_visibility='onchange')
    life = fields.Integer('Life',size=18,track_visibility='onchange')
    life_contract = fields.Integer('Life Contract',size=18,track_visibility='onchange')
    lost_comment = fields.Char('Lost Comment',size=255,track_visibility='onchange')
    mainly_carrier = fields.Char('Mainly Carrier',size=255,track_visibility='onchange')
    brand = fields.Char('Brand',track_visibility='onchange')
    max_capital_limit = fields.Float('Max Capital Limit',digits=(16,2),track_visibility='onchange')
    medical_appointment = fields.Char('Medical Appointment',size=255,track_visibility='onchange')
    min_capital_limit = fields.Float('Min Capital Limit',digits=(16,2),track_visibility='onchange')
    payment_mode = fields.Selection([
        ('pre_pagamento','Pré-pagamento'),
        ('pos_pagamento','Pós-pagamento'),
    ],string="Modalidade de Pagamento",track_visibility='onchange')
    fee_model = fields.Selection([
        ('Small','Small'),
        ('Rebate','Rebate'),
    ],string="Model",track_visibility='onchange')
    modelo_id = fields.Many2one('ir.model',string="Modelo",track_visibility='onchange')  #model not created yet
    moderator_variable_value = fields.Float('Moderator Variable Value',digits=(5,2),track_visibility='onchange')
    motive_of_gain = fields.Selection([
        ('Expertise','Expertise'),
        ('Gestão de Sinistro','Gestão de Sinistro'),
        ('Preço','Preço'),
        ('Relacionamento','Relacionamento'),
        ('Serviço','Serviço'),
    ],string="Motivo de Ganho",track_visibility='onchange')
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
    ], string="Motivo de Perda",track_visibility='onchange')
    next_step = fields.Char('Next Step',size=255,track_visibility='onchange')
    contract_carrier = fields.Many2one('account.account', string='Operadora do Contrato',track_visibility='onchange')
    name = fields.Char('Opportunity Name',size=120,track_visibility='onchange')
    owner_id = fields.Many2one('res.users', string="Opportunity Owner",track_visibility='onchange')
    iq_score = fields.Integer('Opportunity Score',size=9,track_visibility='onchange')
    order_number = fields.Char('Order Number',size=8,track_visibility='onchange')
    contract_origin = fields.Selection([
        ('Novo','Novo'),
        ('Cross Sell','Cross Sell'),
        ('Up Sell','Up Sell'),
        ('Reimplantação','Reimplantação'),
    ], string="Origem do Contrato",track_visibility='onchange')
    opportunity_event_source = fields.Selection([
        ('Estudo','Estudo'),
        ('Visita','Visita'),
    ], string="Origem do evento oportunidade",track_visibility='onchange')
    orthodontics = fields.Char('Orthodontics',size=255,track_visibility='onchange')
    others = fields.Char('Others',size=255,track_visibility='onchange')
    partner_account_id = fields.Many2one('account.account', string='Partner Account',track_visibility='onchange')
    partnership = fields.Many2one('account.account', string='Partnership',track_visibility='onchange')
    pension_mode = fields.Selection([
        ('Plano Averbado', 'Plano Averbado'),
        ('	Plano Instituído', '	Plano Instituído'),
    ], string="Pension Mode",track_visibility='onchange')
    periodicity_renewal = fields.Integer('Periodicity Renewal',size=3,track_visibility='onchange')
    grace_period = fields.Integer('Período de Carência',size=18,track_visibility='onchange')
    tag = fields.Char('Placa',size=7,track_visibility='onchange')
    places = fields.Text('Places',size=32768,track_visibility='onchange')
    has_dps = fields.Boolean('Possui DPS',track_visibility='onchange')
    main_competitors = fields.Char('Principais Concorrentes',size=100,track_visibility='onchange')
    is_private = fields.Boolean('Private',track_visibility='onchange')
    probability = fields.Float('Probability (%)',digits=(3,2),track_visibility='onchange')
    prosthesis = fields.Char('Prosthesis',size=255,track_visibility='onchange')
    provider = fields.Many2one('account.account', string='Provider',track_visibility='onchange')
    purchase_limit = fields.Selection([
        ('Valor fixo','Valor fixo'),
        ('Percentual do salário','Percentual do salário'),
    ], string="Purchase Limit",track_visibility='onchange')
    purchase_limit_value = fields.Float('Purchase Limit Value',digits=(5,2),track_visibility='onchange')
    number_of_installments = fields.Integer('Quantidade de Parcelas',size=3,track_visibility='onchange')
    total_opportunity_quantity = fields.Float('Quantity',digits=(16,2),track_visibility='onchange')
    rebate = fields.Float('Rebate',digits=(3,2),track_visibility='onchange')
    redeemed = fields.Integer('Redeemed',size=6,track_visibility='onchange')
    renavam = fields.Integer('RENAVAM',size=11,track_visibility='onchange')
    reserve = fields.Char('Reserva',track_visibility='onchange')
    market_reserve = fields.Char('Reserva de Mercado',size=28,track_visibility='onchange')
    reserve_days = fields.Integer('Reserve - Days',track_visibility='onchange')
    retired = fields.Integer('Retired',size=6,track_visibility='onchange')
    returned_reason = fields.Char('Returned Reason',size=255,track_visibility='onchange')
    revenue = fields.Float('Revenue',track_visibility='onchange')
    revenue_politic = fields.Float('Revenue Policy',digits=(16,2),track_visibility='onchange')
    roi_analysis_completed = fields.Boolean('ROI Analysis Completed',track_visibility='onchange')
    service_supplier = fields.Integer('Service Supplier',size=6,track_visibility='onchange')
    simple_test = fields.Char('Simple Test',size=255,track_visibility='onchange')
    sons_capital_limit = fields.Float('Sons Capital Limit',digits=(16,2),track_visibility='onchange')
    special_condition = fields.Char('Special Condition',size=131072,track_visibility='onchange')
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
    ],string="Stage",track_visibility='onchange')
    status_change_date = fields.Date('Status Change Date',track_visibility='onchange')
    administration_tax = fields.Float('Taxa de Administração',digits=(3,2),track_visibility='onchange')
    charge_rate = fields.Float('Taxa de Carregamento',digits=(3,2),track_visibility='onchange')
    emergencial_card_fee = fields.Float('Taxa de Cartão Emergencial',digits=(3,2),track_visibility='onchange')
    availability_fee = fields.Float('Taxa de Disponibilização',digits=(3,2),track_visibility='onchange')
    issuance_cost = fields.Float('Taxa de Emissão',digits=(3,2),track_visibility='onchange')
    delivery_fee = fields.Float('Taxa de Entrega',digits=(3,2),track_visibility='onchange')
    output_rate = fields.Float('Taxa de Saída',digits=(3,2),track_visibility='onchange')
    replace_fee = fields.Float('Taxa de Segunda Via',digits=(3,2),track_visibility='onchange')
    therapy = fields.Char('Therapy',size=255,track_visibility='onchange')
    income_type = fields.Selection([
        ('Renda Temporária','Renda Temporária'),
        ('Renda Vitalícia','Renda Vitalícia'),
        ('Renda Vitalícia Reversível ao Beneficiário','Renda Vitalícia Reversível ao Beneficiário'),
    ],string="Tipo de Renda",track_visibility='onchange')
    Tax_Type = fields.Selection([
        ('Regressiva Definitiva', 'Regressiva Definitiva'),
        ('Progressiva Compensável', 'Progressiva Compensável'),
    ], string="Tipo de Tributação",track_visibility='onchange')
    total_capital = fields.Float(string="Total Capital", digits=(16, 2),track_visibility='onchange')
    tracking_number = fields.Char('Tracking Number',size=12,track_visibility='onchange')
    brokerage_transfer = fields.Boolean('Transferência de Corretagem',track_visibility='onchange')
    type_business = fields.Selection([
        ('Existing Business','Existing Business'),
        ('New Business','New Business'),
    ],string="Type",track_visibility='onchange')
    type_of_pension = fields.Selection([
        ('Aberto','Aberto'),
        ('Fechado','Fechado'),
    ],string="Type of Pension",track_visibility='onchange')
    type_of_revenue = fields.Selection([
        ('Pontual','Pontual'),
        ('Recorrente','Recorrente'),
    ],string="Type of Revenue",track_visibility='onchange')
    broker_first_installment_value = fields.Float('Valor da Primeira Parcela - Agenciamento', digits=(16, 2),track_visibility='onchange')
    comission_first_installment_value = fields.Float('Valor da Primeira Parcela - Comissão', digits=(16, 2),track_visibility='onchange')
    fee_first_installment_value = fields.Float('Valor da Primeira Parcela - Fee', digits=(18, 0),track_visibility='onchange')
    monthly_average_value = fields.Float('Valor Médio Mensal', digits=(4, 2),track_visibility='onchange')
    wage_limit_amount = fields.Float('Wage Limit Amount', digits=(16, 2),track_visibility='onchange')
    wage_limit_for_coparticipation = fields.Selection([
        ('Não possui','Não possui'),
        ('Por Percentual','Por Percentual'),
        ('Por Valor Fixo','Por Valor Fixo'),
    ],string="Wage Limit For Coparticipation",track_visibility='onchange')
    workflow_configuration = fields.Many2one('workflow_configuration', string="Workflow Configuration",track_visibility='onchange')
    campaigns_id = fields.Many2one('model_campaign',string ='Primary Campaign Source',ondelete='cascade',track_visibility='onchange')
    model_id   = fields.Many2one('ir.model', string='Model ID',track_visibility='onchange')
    channel_id = fields.Many2one('channel_segmentation', string='Channel Id',track_visibility='onchange')

    quotation = fields.Many2one('model_quote', string='Quotation',track_visibility='onchange')
    synced_quote_id = fields.Many2one('model_quote', string='Synced Quote',track_visibility='onchange')
    opportunity_team_lines = fields.One2many('crm.lead.team_member','opportunity_id', string="Opportunity Team Lines")
    contact_role_lines = fields.One2many('crm.lead.contact.role','opportunity_id',string="Contact Role Lines")
    contact_partner_lines = fields.One2many('contract.partner','opportunity_id',string="Contact Partner Lines")
    quote_lines = fields.One2many('model_quote','OpportunityId',string="Quotes Lines")
    competitor_lines = fields.One2many('crm.lead.competitor','opportunity_id',string="Competitor Lines")
    attachment_lines = fields.One2many('ir.attachment','opportunity_id',string="Attachment Lines")
    product_lines = fields.One2many('crm.lead.product','opportunity_id',string="Product Lines")
    case_lines = fields.One2many('model_case','opportunity_id',string="Case Lines")
    opportunity_quote_id = fields.Many2one('model_quote', string='Opportunity Quote')