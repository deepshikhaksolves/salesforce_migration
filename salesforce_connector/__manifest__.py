# -*- coding: utf-8 -*-
{
        'name': "ODOO Salesforce Connector",
        'version': '13.1.1.13',
        'category': 'Sales',
        'summary': 'ODOO Salesforce',
        'author': 'Techloyce',
        'website': 'http://www.techloyce.com',
        'images': [
                'static/description/banner.png',
        ],
        'depends': ['sale', 'crm', 'sale_crm'],
        'price': 499,
        'currency': 'EUR',
        'license': 'OPL-1',
        # only loaded in demonstration mode
        'demo': [
                'demo/demo.xml',
        ],

        # always loaded
        'data': [
                'security/ir.model.access.csv',
                'data/salesforce_data.xml',
                'data/sf_country_data.xml',
                # 'data/sf_tags.xml',
                # 'data/sf_stage_mapping.xml',
                'data/salesforce_contact_field_data.xml',
                'data/salesforce_account_field_data.xml',
                'data/salesforce_opportunity_field_data.xml',
                'data/salesforce_lead_field_data.xml',
                'data/salesforce_individual_field_data.xml',
                'data/salesforce_Rep__c_field_data.xml',
                'data/salesforce_pricebook_data.xml',
                'data/salesforce_partner_network_con_data.xml',
                'data/salesforce_job_process_cron.xml',
                'data/salesforce_Quote_Type__c_mapping.xml',
                'data/salesforce_opportunity_sales_docs.xml',
                'data/salesforce_task_field_data.xml',
                'data/mail_activity_data.xml',
                'views/salesforce_view.xml',
                'views/salesforce_logs_view.xml',
                'views/salesforce_queue_jobs_view.xml',
                # 'views/res_partner_view.xml',
                # 'views/crm_lead_view.xml',
                'views/rep__c_view.xml',
                'views/synced_records_view.xml',
                'views/salesforce_field_map_view.xml',
                'views/save_salesforce_records_in_odoo.xml',
                'views/res_config_setting_views.xml',
                'views/opportunity_sales_docs.xml',
                'views/salesforce_tasks_view.xml',
                # 'views/inherited_mail_activity_view.xml'
        ],

        'installable': True,
        'application': True,
}
