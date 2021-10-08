from odoo import models, fields, api


class ResConfigSettingsInherit(models.TransientModel):
    _inherit = "res.config.settings"


    buisness_rules_views = fields.Many2many('ir.model',string="Buisness Rule View",domain=
                                                                    "[('model', 'in', ['crm.lead','lead_sort_colums_in_capaign','model_legal_pending_matter','model_market_reserve_active_mdt','model_market_reserve__c','model_market_reserve_duration_mdt','model_network_provider','model_operator_checklist','crm.lead.contact.role','crm.lead.competitor','crm.lead.lineitem','crm.lead.product','crm.lead.team_member','crm.lead.stage.parameter','crm.lead.stage.path','contract.partner','model_pathology_account_c','model_pathology','paying.company','model.periodicity','plan.coverage','politic.bill','portal.access','model_price_list','model_price_x_region','product.template','product_family','product.network','product_price','product.region','model_publico','model_quote','quote_line_item','quotation_item_price','model_quote_products','model_reason_for_beneficial','model_refund','model_region','model_region_city','model_region_state','model_request','service_reason_config','request_config','model_revenue_compensation','model_revenue_provisioning','channel_segmentation','model_salesforce_dim_beneficiario_x','model_sensus_management_document_c','model_service_benefit_c','model_service_c','model_sla_carrier_benefit_reason_c','res.country.state','study_configuration','model_study_configuration_price_table','model_study_configuration_product','model_subject_c','model_subject_case_model_c','project.task','res.users','user_company_contract_permissions__c','account.account','accredited_network','model_additional_parameter','model_address','model_application_parameter','account.setup.bank.manual.config','model_beneficiary','model_beneficiary_card','beneficiary.contract.plan','model_beneficiary_carrier','model_beneficiary_carrier_revenue','model_benfit_politic','model_brand_c','broker','broker.rating','model_campaign','model_campaignmember','model_car_fleet_c','model_carrier_type_c','model_case','model_case_model_c','model_case_request_c','model_case_request_sla_c','model_case_status_parameter_mdt','model_checklist_c','model_city_c','model_cnae','model_comercial_agent_c','model_comercial_structure_c','model_comments_c','model_company_parameter_c','compensation','condition','res.partner','hr.contract','contract.contribution','contract.copayment','contract.coverage','contract.line.item','model_contract_plan','contract.readjust','contract.service','contract_team','model_cost_center','res.country','operator_document','model_eligibility','contract_eligibility','event_control','hr.expense','expence_provisioning','financial_agreement','financial_contract','model_financial_group','financial_doctor','financial_group_master_user','model_geographic_scope','global_parameter','ir.attachment'])]")



    


