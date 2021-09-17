from odoo import models, fields, api, _
from simple_salesforce import Salesforce
from odoo.exceptions import Warning
from datetime import datetime
from dateutil.rrule import rrule, DAILY
from dateutil.parser import parse
from dateutil.relativedelta import *
from odoo.exceptions import ValidationError, RedirectWarning, UserError
import logging
import re

_logger = logging.getLogger(__name__)


class SalesForceImporter(models.Model):

    _name = 'salesforce.connector'
    _rec_name = 'field_name'
    _description = "Salesforce Connector"

    sales_force = None
    field_name = fields.Char('salesforce_connector')
    include_custm = fields.Boolean('Include Custom Fields')
    max_rec_per_job = fields.Integer('Maximum Record Per JOB', default=100)
    accounts = fields.Boolean('Import Accounts')
    contacts = fields.Boolean('Import Contacts')
    individuals = fields.Boolean('Import Individuals')
    partner_ntwrk_con = fields.Boolean('Import Partner Network Connection')
    pricebook = fields.Boolean('Import Pricebook')
    rep__c = fields.Boolean('Import Rep__c')
    leads = fields.Boolean('Import Leads')
    opportunities = fields.Boolean('Import Opportunities')
    sales_orders = fields.Boolean('Import Sale Orders')
    tasks = fields.Boolean('Import Tasks')
    geographic_scope = fields.Boolean('Import Geographic Scope')
    products = fields.Boolean('Export Products')
    from_date = fields.Date('From Date', compute="_compute_date", store=True, required=True,
                            default=fields.Date.today() + relativedelta(days=-7))
    to_date = fields.Date('To Date', compute="_compute_date", store=True, required=True, default=fields.Date.today())
    last_sync_date = fields.Date('Last Sync Date', readonly=True)
    last_daily_sync_date = fields.Date(default=fields.Date.today() + relativedelta(days=-7))

    _sql_constraints = [
        ('check_max_rec_per_job', 'CHECK(max_rec_per_job <= 1000 AND max_rec_per_job > 0)',
         'Maximum Record Per JOB must be between 1 and 1000'),
    ]

    @api.depends('last_sync_date')
    def _compute_date(self):
        if self.last_sync_date:
            self.from_date = self.last_sync_date
            self.to_date = self.last_sync_date + relativedelta(days=+7)
        else:
            self.to_date = fields.Date.today()
            self.from_date = fields.Date.today() + relativedelta(days=-7)

    @api.onchange('from_date', 'to_date')
    def _validate_range_date(self):
        if self.from_date and self.to_date:
            if self.from_date > self.to_date or self.from_date == self.to_date:
                raise ValidationError(_('Date must be in valid range.!!'))

    def sync_salesforce_daily(self, **kwargs):
        """
        This method runs by the cron to create job queues for the salesforce models
        ,it will take the models from the form ,the checkboxes that are already ticked
        :param kwargs:
        :return:
        """
        salesforce = self.search([], limit=1)
        salesforce.from_date = salesforce.last_daily_sync_date
        salesforce.to_date = salesforce.from_date + relativedelta(days=1)
        salesforce.last_daily_sync_date = salesforce.to_date
        salesforce.sync_data()
        # run the method to convert salesforce tasks to activities, just to nake sure that they convert every time
        # the daily cron job runs
        # self.env.ref('salesforce_connector.sf_sync_record').start_convert_task_to_activities()
        # self.env.ref('salesforce_connector.sf_sync_record').start_saving_sales_docs_urls()


    def sync_data(self):
        """
        this function checks the user selection for import data and on the basis of this 
        selection it call create_job_queues function

        :return:
        """
        if self.accounts or self.products or self.sales_orders or self.opportunities or self.contacts or \
                self.individuals or self.partner_ntwrk_con or self.pricebook or self.rep__c or self.leads or self.tasks or self.geographic_scope:
            self.create_job_queues()
        else:
            raise Warning(_("No Option Checked.",))

    def connect_to_salesforce(self):
        """
        test user connection

        """
        try:
            username = self.env['ir.config_parameter'].sudo().get_param('sf_username')
            password = self.env['ir.config_parameter'].sudo().get_param('sf_password')
            sf_organization = self.env['ir.config_parameter'].sudo().get_param('organization_id')
            sf_domain = self.env['ir.config_parameter'].sudo().get_param('sf_domain')
            version = self.env['ir.config_parameter'].sudo().get_param('version')

            type(self).sales_force = Salesforce(username=username,
                                            password=password,
                                            organizationId=sf_organization,
                                            domain=sf_domain,
                                            version=version)
            print(self.sales_force)
        except Exception as e:
            Warning(_(str(e)))

    # def get_image(self):
    #     self.env['sf.queue.jobs'].get_account_records_image()

    def create_job_queues(self):
        """This creates job queues to import data from SalesForce
        :return: N/A
        """
        self.connect_to_salesforce()
        if self.sales_force is None:
            raise Warning(_("Kindly provide SalesForce Credentials for odoo user",))
        if self.leads:
            self._add_records_to_queue('Lead', 'crm.lead', self.from_date, self.to_date, self.include_custm,
                                       self.max_rec_per_job)
        if self.opportunities:
            self._add_records_to_queue('Opportunity', 'crm.lead', self.from_date, self.to_date, self.include_custm,
                                       self.max_rec_per_job)
        if self.rep__c:
            self._add_records_to_queue('Rep__c', 'sf.rep__c', self.from_date, self.to_date, self.include_custm,
                                       self.max_rec_per_job)
        if self.pricebook:
            self._add_records_to_queue('Pricebook2', 'sf.pricebook', self.from_date, self.to_date, self.include_custm,
                                       self.max_rec_per_job)
        if self.partner_ntwrk_con:
            self._add_records_to_queue('PartnerNetworkConnection', 'sf.pnc', self.from_date, self.to_date,
                                       self.include_custm, self.max_rec_per_job)
        if self.individuals:
            self._add_records_to_queue('Individual', 'res.partner', self.from_date, self.to_date, self.include_custm,
                                       self.max_rec_per_job)
        if self.contacts:
            self._add_records_to_queue('Contact', 'res.partner', self.from_date, self.to_date, self.include_custm,
                                       self.max_rec_per_job)
        if self.accounts:
            self._add_records_to_queue('Account', 'res.partner', self.from_date, self.to_date, self.include_custm,
                                       self.max_rec_per_job)
        if self.tasks:
            self._add_records_to_queue('Task', 'salesforce.tasks', self.from_date, self.to_date, self.include_custm,
                                       self.max_rec_per_job)

        if self.geographic_scope:
            self._add_records_to_queue('Scopes', 'model_geographic_scope', self.from_date, self.to_date, self.include_custm,
                                       self.max_rec_per_job)

        if self.sales_orders:
            # data_dictionary["sales_orders"] = self.import_sale_orders()
            self.import_sale_orders()

        # if self.products:
        #     self.export_products()

        # Process the cron
        cron_record = self.env.ref('salesforce_connector.sf_ir_cron_job_process')
        if cron_record:
            next_exc_time = datetime.now()
            cron_record.sudo().write({'nextcall': next_exc_time,
                                      'active': True,
                                      'numbercall': 1
                                      })
            cron_record.sudo().write({'code':'model.process_queue_jobs(for_new=True)'})

    def _add_records_to_queue(self, sf_model, odoo_model, from_date, to_date, include_custm, max_rec_per_job):
        vals = []
        for dt in rrule(DAILY, dtstart=from_date, until=to_date):
            if dt.date() != to_date:
                nxt_date = dt + relativedelta(days=+1)
                model = self.env['ir.model'].search([('model', '=', odoo_model)])
                data = {
                        'from_date': dt,
                        'odoo_model': model.id,
                        'state': 'new',
                        'import_status': 'not_imported',
                        'to_date': nxt_date,
                        'sf_model': sf_model,
                        'include_custm': include_custm,
                        'max_rec_per_job': max_rec_per_job
                }
                vals.append(data)
        if vals:
            self.env['sf.queue.jobs'].create(vals)
        self.env['salesforce.sync.history'].create_log_param(sf_model, '', 'success', 'salesforce_to_odoo',
                                                             sf_model + ' value has been successfully added to queue')

    def search_count(self, sf_model, from_date=False, to_date=False):
        if not self.sales_force:
            self.connect_to_salesforce()
        query = "SELECT COUNT(Id) FROM {sf_model} where LastModifiedDate > {from_date} and LastModifiedDate < {to_date}".format\
            (sf_model=sf_model,from_date=from_date.strftime('%Y-%m-%dT%H:%M:%SZ'), to_date=to_date.strftime('%Y-%m-%dT%H:%M:%SZ'))
        records = self.sales_force.query_all(query)['records']
        print('total records are ', records[0].get('expr0'))
        return records[0].get('expr0')

    def _query_to_salesforce(self, model, sf_model, record_id=False, from_date=False, to_date=False, include_custom=False, offset=False, limit=False):
        self.connect_to_salesforce()
        records = []
        query_fields = self._get_sales_force_query_fields(model, sf_model, include_custom)
        if query_fields:
            query = "SELECT {query_fields} FROM {sf_model} %s".format(query_fields=query_fields,
                                                                   sf_model=sf_model)
            extend_query = ''
            if record_id:
                extend_query = "where id='%s'" % record_id
            if from_date and to_date and not record_id:
                extend_query = "where LastModifiedDate > %s and LastModifiedDate < %s" % (from_date.strftime('%Y-%m-%dT%H:%M:%SZ'), to_date.strftime('%Y-%m-%dT%H:%M:%SZ'))
            if limit > 0:
                extend_query += ' LIMIT {limit}'.format(limit=limit)
                if offset:
                    extend_query += ' OFFSET {offset}'.format(offset=offset)
            records = self.sales_force.query_all(query % extend_query)["records"]
        return records

    def _get_sales_force_query_fields(self, o_model, sf_model, include_custom):
        query = """SELECT sf_field from sf_columns_mapping
                    WHERE o_model = {o_model}
                    AND sf_model = '{sf_model}'
                    AND sf_model is not NULL
                    AND o_model is not NULL
                    AND query_field = true
                    AND sf_field is not NULL""".format(o_model=o_model.id,
                                                      sf_model=sf_model)
        final_query = query if include_custom else query + """ AND sf_field NOT LIKE '%__c'"""

        self.env.cr.execute(final_query)
        valid_records = self.env.cr.dictfetchall()
        # Provide unique salesforce columns
        fields_list = list(set([rec.get('sf_field') for rec in valid_records]))
        sf_fields = ', '.join(fields_list)
        return sf_fields

    #: Get Name, Email, username and id of a salesforce user
    def get_salesforce_user_info(self):
        self.env['sf.queue.jobs'].update_fields_on_records('crm.lead', 'Lead')

    def get_user_info(self, salesforce_user_ids=None):
        if not self.sales_force:
            self.connect_to_salesforce()

        query = "SELECT Name,Email,Username,Id,IsActive FROM User WHERE Id in {Id} and Email like '%@mclpcb.com'". \
            format(Id=salesforce_user_ids)
        if len(salesforce_user_ids) == 1:
            query = "SELECT Name,Email,Username,Id,IsActive FROM User WHERE Id = '{Id}' and Email like '%@mclpcb.com'". \
            format(Id=salesforce_user_ids[0])

        records = self.sales_force.query_all(query)['records']
        # print('total users are ', records[0].get('expr0'))
        return records

    def _prepare_create_data(self, sf_data, odoo_model, sf_model):
        create_data = {}
        _logger.info('Record started creating')
        # if the sf_model type is lead then
        if sf_model == 'Lead':
            #: if the is_converted is true means it is already converted into opportunity
            #: So no need to make a lead record for it because lead/opportunity is same relation in odoo

            if sf_data.get('IsConverted', False):
                self.env['salesforce.sync.history'].create_log_param(
                    sf_model, '', 'success',
                    'salesforce_to_odoo',
                    sf_model + f" with {sf_data.get('Id', '')} Id is already an opportunity")
                _logger.info('Lead with %s sf_id is already a opportunity', sf_data.get('Id', ''))
                return {'__not_needed_record': True}

            #: check if this lead is converted to opportunity in odoo
            is_lead_converted_to_opportunity = self.env['crm.lead'].search([
                ('sf_id', '=', sf_data.get('Id')), ('type', '=', 'opportunity')])

            #: if lead is converted to opportunity in odoo then skip this id
            if is_lead_converted_to_opportunity:
                self.env['salesforce.sync.history'].create_log_param(
                    sf_model, '', 'success',
                    'salesforce_to_odoo',
                    sf_model + f" with {sf_data.get('Id', '')} Id is converted to an opportunity in odoo")
                _logger.info('Lead with %s sf_id is converted to an opportunity', sf_data.get('Id', ''))
                return {'__not_needed_record': True}

            create_data['type'] = 'lead'
            if 'Address' in sf_data:
                address_data = self.create_address_data(None, sf_data['Address'])
                if address_data:
                    address_data = address_data[2]
                    create_data['zip'] = address_data['zip']
                    create_data['city'] = address_data['city']
                    create_data['street'] = address_data['street']
                    create_data['country_id'] = address_data['country_id']
                    create_data['state_id'] = address_data['state_id']
                    del sf_data['Address']

            #: concatenate FirstName and LastName for lead contact_name
            contact_name = ''
            if 'FirstName' in sf_data and sf_data['FirstName']:
                contact_name = f"{sf_data['FirstName']}"
                del sf_data['FirstName']

            if 'LastName' in sf_data and sf_data['LastName']:
                contact_name = f"{contact_name} {sf_data['LastName']}"
                del sf_data['LastName']

            create_data['contact_name'] = contact_name

            # description = ''
            # #: concatenate description and comment for lead internal notes
            # if 'Description' in sf_data and sf_data['Description']:
            #     description = f"{sf_data['Description']}"
            #     # del sf_data['Description']
            #
            # if 'Comments__c' in sf_data and sf_data['Comments__c']:
            #     description = f"{description}  " \
            #                   f"{sf_data['Comments__c']}"
            #     # del sf_data['Comments__c']
            #
            # create_data['description'] = description

            #: if company name don't exist then we will enter n/a cause its required
            if not sf_data.get('Company', False):
                create_data['name'] = 'n/a'
                # del sf_data['Company']
            else:
                create_data['name'] = sf_data.get('Company', 'n/a')
                # del sf_data['Company']

        for rec in sf_data:
            sf_field = self.env['sf.columns.mapping'].search([('o_model', '=', odoo_model.model),
                                                              ('sf_model', '=', sf_model),
                                                              ('sf_field', '=', rec)], limit=1)
            odoo_field = sf_field.odoo_field
            if sf_field and odoo_field and sf_data[rec]:
                value = self._create_fields_data(sf_data[rec], odoo_field, odoo_model, sf_model,
                                                 sf_field, sf_field.sf_relational_model)
                if value or odoo_field.ttype == 'boolean':
                    if odoo_field.ttype == 'one2many':
                        # only billing and shipping address is one2many
                        if 'sf_country_name' not in create_data and value[0][2]['type'] in ['other', 'delivery', 'invoice']:
                            create_data['sf_country_name'] = sf_data[rec]['country']  # get the sf_country_name for mapping
                            create_data['sf_state'] = sf_data[rec]['state']  # get the sf_state name for mapping

                        if odoo_field.name in create_data:
                            create_data[odoo_field.name].append(value[0])

                        else:
                            create_data[odoo_field.name] = value

                    elif odoo_field.ttype == 'many2one':
                        if odoo_field.name == 'stage_id':
                            create_data[odoo_field.name] = value[0]# stage id
                            create_data['sf_stage_name'] = value[1] # sf stage name
                        else:
                            if odoo_field.name == 'sf_related_account_id':
                                # for contacts,only id for parent_id so that contact
                                # can connect to their respective company
                                create_data['parent_id'] = value
                            elif odoo_field.name == 'RFQ_type':
                                create_data['RFQ_type'] = value

                            # if no sf_related_account_id means no parent id
                            create_data[odoo_field.name] = value
                    else:
                        if sf_model == 'Opportunity' and odoo_field.name == 'name':
                            create_data[odoo_field.name] = value[0]
                            create_data['rev_code'] = value[1]

                        else:
                            create_data[odoo_field.name] = value

        _logger.info('Salesforce Record been created')
        return create_data

    def _create_fields_data(self, value, odoo_field, odoo_model, sf_model, sf_field, sf_relational_model):
        if not sf_field.type == 'Lookup':
            if odoo_field.ttype == 'date' and value:
                return parse(value)

            elif odoo_field.ttype == 'datetime' and value:
                date = str(parse(value))
                return datetime.strptime(date.split('+')[0], "%Y-%m-%d %H:%M:%S")

            elif odoo_field.ttype == 'many2one':
                # we first check the salesforce stage name in stage mapping
                # and search for related crm stage name if any
                # if found then return that stage_id otherwise
                # create new stage and return that new stage_id
                if odoo_field.name == 'stage_id':
                    sf_mapped_stage = self.env['sf.stages.mapping'].search([("sf_stage_name", "=", value)])

                    if sf_mapped_stage:
                        return ( sf_mapped_stage.sf_crm_stage.id, value)

                    else:
                        odoo_stage = self.env['crm.stage'].search( [("name", "=", value)] )
                        if not odoo_stage:
                            odoo_stage = self.env["crm.stage"].create( {
                                "name": value
                            })
                        return (odoo_stage.id, value)

                elif odoo_field.name == 'RFQ_type':
                    quote_type = self.env['sf.quote.type.map'].search([("quote_type_name", "=", value)])
                    if not quote_type:
                        quote_type = self.env['sf.quote.type.map'].create(
                            {'quote_type_name': value})

                    return quote_type.id

                elif sf_relational_model:
                    return self._update_many2one_field(value, sf_relational_model)
                else:
                    try:
                        many2one_record = self.env[odoo_field.relation].search([('name', '=', value)], limit=1)
                        if not many2one_record:
                            res = self.env[odoo_field.relation].create({'name': value})
                            if res:
                                return res.id
                            else:
                                return None
                        return many2one_record.id

                    except Exception as e:
                        _logger.info('%s Error occurred in many2one mapping', e)
                        return None

            elif odoo_field.ttype == 'one2many':
                data =[]
                if sf_field.sf_field in ['BillingAddress', 'OtherAddress', 'MailingAddress', 'ShippingAddress']:
                    if sf_field.sf_field in ['OtherAddress', 'MailingAddress']:
                        type = 'other'
                    elif sf_field.sf_field == 'BillingAddress':
                        type = 'invoice'
                    elif sf_field.sf_field == 'ShippingAddress':
                        type = 'delivery'
                    data.append(self.create_address_data(type, value))
                    return data
                else:
                    pass

            elif odoo_field.ttype == 'many2many':
                pass

            elif sf_model == 'Opportunity' and odoo_field.name == 'name':
                customer_part_number = re.split('Rev|rev|REV', value, 1)
                rev_code = ''
                if len(customer_part_number) == 2:
                    rev_code = customer_part_number[1].strip()
                    return customer_part_number[0].strip('-| '), rev_code

                return value, rev_code

            elif odoo_field.ttype == 'selection':
                try:
                    # Fixme: in case company business type is related field on res.partner
                    # then it won't get updated in opportunity but if the res.partner get updated then
                    # it will also get the value then
                    for selection_field in odoo_field.selection_ids:
                        if value.lower() == selection_field.name.lower():
                            return selection_field.name
                    _logger.info('%s Selection field do not match any value,value is %s', odoo_field.name, value)
                    return ''
                except Exception as e:
                    _logger.info(f'Error occur during selection field matching ,{str(e)}')
                    self.env['salesforce.sync.history'].create_log_param(
                            sf_model, '', 'failed',
                            'salesforce_to_odoo',
                            sf_model + ' With error ' + str(e))
                    return  ''
            else:
                return value

        else:
            if sf_field.type == 'Lookup' and isinstance(value, dict):
                odoo_field_name = odoo_field.name
                sf_field_name = odoo_field_name.split('_')[1]
                return value.get(sf_field_name, '')


    def create_address_data(self, address_type, address):
        data = {}
        if address:
            data["street"] = address["street"] if address["street"] else ""
            data["city"] = address["city"] if address["city"] else ""
            data["zip"] = address["postalCode"] if address["postalCode"] else ""
            data["type"] = address_type

            state = country = None

            if address['country'] is not None:
                countries = self.env['sf.country.map'].search([('sf_country_name', 'ilike', address['country'])])
                for matched_country in countries:
                    if matched_country.sf_country_name.lower() == address['country'].lower():
                        country = matched_country.sf_our_matched_country
                        break

                if not country:
                    countries = self.env['res.country'].search([('name', 'ilike', address['country'])])
                    for matched_country in countries:
                        if matched_country.name.lower() == address['country'].lower():
                            country = matched_country
                            break

            if address['state'] is not None:
                states = self.env['sf.state.map'].search([('sf_state_name', 'ilike', address['state'])])
                for matched_states in states:
                    if matched_states.sf_state_name.lower() == address['state'].lower():
                        state = matched_states.sf_our_matched_state
                        break

                if not state:
                    states = self.env['res.country.state'].search( [('name', 'ilike', address['state'])])
                    for matched_states in states:
                        if matched_states.name.lower() == address['state'].lower():
                            state = matched_states
                            break

                    if not state:
                        states = self.env['res.country.state'].search([('code', 'ilike', address['state'])])
                        for matched_states in states:
                            if matched_states.code.lower() == address['state'].lower():
                                if country is not None and matched_states.country_id.id == country.id:
                                    state = matched_states
                                    break

            if country is None or ( country and address['country'].lower() != country.name.lower() ):
                if state:
                    country = state.country_id

            data["country_id"] = country.id if country else None # if nothing found need to put 1 first country
            data["state_id"] = state.id if state else None
            if address['country'] is not None:
                data['sf_country_name'] = address['country']

            if address['state'] is not None:
                data['sf_state'] = address['state']

            return (0, 0, data)

    def _update_many2one_field(self, value, sf_relational_model):
        odoo_model = self._check_if_mapping_exist(sf_relational_model)
        if odoo_model:
            record_exist = self._check_existing_value(value, odoo_model.o_model.model, sf_relational_model)
            if record_exist:
                return record_exist.id
            else:
                record = self._query_to_salesforce(odoo_model.o_model, sf_relational_model, value)
                if sf_relational_model in ['Account', 'Contact', 'Individual']:
                    if sf_relational_model == 'Account':
                        id_field = 'sf_account_id'
                    elif sf_relational_model == 'Contact':
                        id_field = 'sf_contact_id'
                    else: 
                        id_field = 'sf_individual_id'
                else:
                    id_field = 'sf_id'
                json_data = {id_field: record[0]['Id'], 'name': record[0]['Name']}
                created_record = self.env[odoo_model.o_model.model].create(json_data)
                self.env['salesforce.sync.history'].create_log_param(sf_relational_model, json_data.get(id_field), 'success',
                                                                     'salesforce_to_odoo',
                                                                     "Created Successfully")

                return created_record.id if created_record else False
        else:
            return False
        
    def _check_if_mapping_exist(self, sf_model):
        odoo_model = self.env['sf.model.mapping'].search([('sf_model', '=', sf_model)])
        return odoo_model if odoo_model else False
            
    def _create_records_in_odoo(self, model, sf_model, records):
        try:
            create_list = []
            for rec in records:
                if sf_model in ['Account', 'Contact', 'Individual']:
                    if sf_model == 'Account':
                        id_field = 'sf_account_id'
                    elif sf_model == 'Contact':
                        id_field = 'sf_contact_id'
                    else:
                        id_field = 'sf_individual_id'
                else:
                    id_field = 'sf_id'
                record_exist = self.env[model].search([(id_field, '=', rec.get(id_field)),
                                                       (id_field, '!=', False),
                                                       ('active', 'in', [True, False])], limit=1)
                if record_exist:
                    # check record exist for which sf_model
                    # if for Accounts we have to deal with Addresses otherwise same address can replicate multiple times
                    if id_field == 'sf_account_id':
                        print('A partner already exist with this id')
                        address_type_to_id = {}

                        old_addresses = record_exist.child_ids.ids if record_exist.child_ids else None

                        if old_addresses is not None:
                            for address_id in old_addresses:
                                address_record = self.env[model].search([('id', '=', address_id)])
                                print(address_record)
                                if address_record.type in ['delivery', 'invoice', 'other']:
                                    address_type_to_id[address_record.type] = address_id

                            new_child_ids = []
                            for incoming_address in rec.get('child_ids', []):
                                current_address_type = incoming_address[2]['type']

                                if current_address_type in address_type_to_id:
                                    new_child_ids.append((1, address_type_to_id[current_address_type], incoming_address[2]))
                                else:
                                    new_child_ids.append(incoming_address)

                            rec.update({'child_ids': new_child_ids, 'is_company': True})

                        else:
                            rec.update({'is_company': True})

                    elif sf_model == 'Opportunity':
                        # when it is an Opportunity we first write the record and then we check for tags
                        # otherwise the write operation afterwards will override by it
                        record_exist.write(rec)
                        self.update_opportunity(record_exist)
                        continue

                    # records other than opportunity and accounts
                    record_exist.write(rec)

                    # for country mapping
                    if sf_model in ['Account', 'Contact', 'Individual']:
                        self.update_country_mapping(record_exist.id)
                        self.update_state_mapping(record_exist.id)

                    self.env['salesforce.sync.history'].create_log_param( sf_model, rec.get( id_field ), 'success',
                                                                          'salesforce_to_odoo',
                                                                          "Updated Successfully" )
                else:
                    create_list.append(rec)
            if create_list:
                if model == 'res.partner' and sf_model == 'Account':
                    for single_record in create_list:
                        single_record.update({'is_company': True})
                res = self.env[model].create(create_list)

                if res:
                    # if the created record is for account model then for country mapping call update_country_mapping
                    if sf_model in ['Account', 'Contact', 'Individual']:
                        for new_record in res:
                            self.update_country_mapping(new_record.id)
                            self.update_state_mapping(new_record.id)

                    # if sf_model is Opportunity then we need to update the tags and take additional actions
                    if sf_model == 'Opportunity':
                        for new_record in res:
                            self.update_opportunity(new_record)

                    if sf_model == 'Lead':
                        for new_record in res:
                            print(sf_model)
                    self.env['salesforce.sync.history'].create_log_param( sf_model, '', 'success', 'salesforce_to_odoo',
                                                                          str(len(res)) + " " + sf_model +
                                                                          " records created successfully" )

        except Exception as e:
            raise e

    def update_country_mapping(self, partner_id):
        # first if the account have child ids i.e;Billing and Shipping Address
        # get all addresses
        all_partner_ids = [partner_id]
        this_partner = self.env['res.partner'].search([('id', '=', partner_id)])

        if this_partner.child_ids.ids:
            all_partner_ids.extend(this_partner.child_ids.ids)

        for every_address in all_partner_ids:
            # get the partner_id of the address
            that_partner = self.env['res.partner'].search([('id', '=', every_address)])
            # search the sf country in country mapping

            if that_partner.sf_country_name:
                country_matched = None
                given_country = that_partner.sf_country_name
                # get the exact sf_country_name from the mapping if not found then create one
                countries = self.env['sf.country.map'].search([('sf_country_name', 'ilike', that_partner.sf_country_name)])
                for matched_country in countries:
                    if matched_country.sf_country_name.lower() == given_country.lower():
                        country_matched = matched_country
                        break

                if country_matched:
                    # if we find matched country in country mapping then we will update the country id of
                    # partner to the mapped country_id
                    that_partner.write({'country_id': country_matched.sf_our_matched_country.id})
                    country_matched.write({'sf_res_partner_ids': [(4, every_address)]})
                    country_matched.env.cr.commit()

                # else if  no mapping for sf country name then create a mapping
                else:
                    # first check if there is country name in in partner
                    if that_partner.sf_country_name:
                        new_country_map = self.env['sf.country.map'].create({
                            'sf_country_name': that_partner.sf_country_name,
                            'sf_our_matched_country': that_partner.country_id.id,
                            'sf_res_partner_ids': [(4, every_address)]})

                        if new_country_map:
                            _logger.info(f'{that_partner.sf_country_name} -> {that_partner.country_id.name}'
                                         f' new country mapping added')

    def update_state_mapping(self, partner_id):
        # first if the account have child ids i.e;Billing and Shipping Address
        # get all addresses
        all_partner_ids = [partner_id]
        this_partner = self.env['res.partner'].search( [('id', '=', partner_id)])

        if this_partner.child_ids.ids:
            all_partner_ids.extend(this_partner.child_ids.ids)

        for every_address in all_partner_ids:
            # get the partner_id of the address
            that_partner = self.env['res.partner'].search([('id', '=', every_address)])
            # search the sf_state in state mapping

            if that_partner.sf_state:
                state_matched = None
                given_state = that_partner.sf_state
                # get the exact sf_country_name from the mapping if not found then create one
                states = self.env['sf.state.map'].search([('sf_state_name', 'ilike', that_partner.sf_state)])
                for matched_states in states:
                    if matched_states.sf_state_name.lower() == given_state.lower():
                        state_matched = matched_states
                        break

                if state_matched:
                    # if we find matched state in state mapping then we will update the state id of partner
                    # to the mapped state_id
                    that_partner.write({'state_id': state_matched.sf_our_matched_state.id})
                    state_matched.write({'sf_res_partner_ids': [(4, every_address)]})
                    state_matched.env.cr.commit()

                # else if  no mapping for sf state name then create a mapping
                else:
                    # first check if there is sf_state  in partner
                    if that_partner.sf_state:
                        new_state_map = self.env['sf.state.map'].create({
                            'sf_state_name': that_partner.sf_state,
                            'sf_our_matched_state': that_partner.state_id.id,
                            'sf_res_partner_ids': [(4, every_address)]})

                        if new_state_map:
                            _logger.info(f'{that_partner.sf_state} -> {that_partner.state_id.name}'
                                         f' new state mapping added')

    # update opportunity record
    def update_opportunity(self, new_record):
        #: when stage changed  or done some action on opportunity the date_closed will change accordingly so
        # print(f"{new_record.name} ===> {new_record.date_closed}")
        other_actions = self.env['sf.stages.mapping'].search([("sf_stage_name", "=", new_record.sf_stage_name)])
        if other_actions.tags:
            print( other_actions.tags.id )
            new_record.write({'tag_ids': [(4, other_actions.tags.id)]})
            print(new_record)

        if other_actions.mark == 'lost':
            result = new_record.action_set_lost(lost_reason=False, won_status='lost')

        if other_actions.mark == 'won':
            new_record.action_set_won_rainbowman()

        if other_actions.mark == 'archive':
            new_record.toggle_active()

        new_record.write({'date_closed': new_record.sf_closed_date})

    def _check_existing_value(self, value, model, sf_model):
        if value:
            if sf_model in ['Account', 'Contact', 'Individual']:
                if sf_model == 'Account':
                    id_field = 'sf_account_id'
                elif sf_model == 'Contact':
                    id_field = 'sf_contact_id'
                else:
                    id_field = 'sf_individual_id'
            else:
                id_field = 'sf_id'
            record_exist = self.env[model].search([(id_field, '=', value)], limit=1)
            return record_exist if record_exist else False





