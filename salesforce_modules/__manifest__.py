# -*- coding: utf-8 -*-
{
    'name': "salesforce_modules",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account_accountant','project','crm','hr_contract'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
        'views/account_views.xml',
        'views/geographic_scope_views.xml',
        'views/users_views.xml',
        'views/task_view.xml',
        'views/user_contract_views.xml',
        'views/revenue_view.xml',
        'views/lead_view.xml',
        'views/channel_segment_views.xml',
        'views/work_flow_config.xml',
        'views/record_type_views.xml',
        'views/type_of_operator_views.xml',
        'views/cnae_views.xml',
        'views/campaign_layout.xml',
        'views/lead_sort_columns_in_campaign_view.xml',
        'views/model__c_views.xml',
        'views/pathology_view.xml',
        'views/region_views.xml',
        'views/accredited_network_views.xml',
        'views/quote_line_item_views.xml',
        'views/quotation_item_price_views.xml',
        'views/product_views.xml',
        'views/product_family_views.xml',
        'views/product_price_views.xml',
        'views/market_reserve__c_view.xml',
        'views/network_provider_views.xml',
        'views/operator_checklist_views.xml',
        'views/price_list_views.xml',
        'views/contract_plan_views.xml',
        'views/menus.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
