import json
import logging
from odoo import models, fields,api, _
from odoo.exceptions import Warning,ValidationError
from dateutil.rrule import rrule, DAILY
from dateutil.relativedelta import *
from datetime import timedelta, datetime
from base64 import encodebytes
from collections import defaultdict
import re

_logger = logging.getLogger(__name__)

class SfQueueManager(models.Model):
    _name = 'sf.queue.jobs'
    _description = 'This is used to Sync all the record in queues'
    _rec_name = 'sf_model'
    _order = 'id desc'

    sf_model = fields.Selection([('Account', 'Account'), ('Contact', 'Contact'), ('Individual', 'Individual'),
                                 ('PartnerNetworkConnection', 'PartnerNetworkConnection'), ('Rep__c', 'Rep__c'),
                                 ('Pricebook2', 'Pricebook2'), ('Opportunity', 'Opportunity'),
                                 ('Lead', 'Lead'), ('Task','Task')], string="Salesforce Model")
    odoo_model = fields.Many2one('ir.model', string="odoo Model")
    o_model = fields.Many2one('ir.model', string="o Model")
    from_date = fields.Datetime('From Date')
    to_date = fields.Datetime('To Date')
    # main_total_records = fields.Integer('Total Records per date', default=0)
    # main_job = fields.Boolean('Is main job or child job', default=False)
    record_count = fields.Integer('Total Records', default=0)
    job_records = fields.Text(string='Salesforce Records')
    processed_rec_count = fields.Integer('Processed Records', default=0)
    state = fields.Selection([('new', 'New'), ('progress', 'In Progress'), ('done', 'Done'), ('failed', 'Failed')],
                             string='State')
    import_status = fields.Selection([('imported', 'Imported'), ('not_imported', 'Not Imported Yet'),
                                      ('failed_import', 'Import Failed'), ('re_import', 'Re Importing')],
                                     string='Import Status', default='not_imported')
    include_custm = fields.Boolean('Include Custom Fields')
    max_rec_per_job = fields.Integer('Maximum Record Per JOB')
    sf_offset = fields.Integer('Offset value', default=0)
    create_date = fields.Datetime('Created On', readonly=True, required=True, default=fields.Datetime.now)
    all_sf_models = set()

    def process_queue_jobs(self, for_new=False):
        salesforce = self.env['salesforce.connector'].browse(1)
        is_the_last_step = False
        state = []
        if for_new:
            state = ['new', 'progress']
        else:
            state = ['failed', 'progress']

        all_job = False
        if not self.id:
            all_job = True
            # removed failed from the list ,if failed leave it as is don't process it unless stated manually
            # state = ['new'] if for_new else ['new', 'progress']
            self = self.search([('state', 'in', state)])

        for record in self:
            type(self).all_sf_models.add(record.sf_model)
            record.state = 'progress'
            _logger.info('New record in progress- id %s', record.id)
            # record.env.cr.commit()
            try:
                total_records = salesforce.search_count(sf_model=record.sf_model, from_date=record.from_date, to_date=record.to_date)
                # record.main_total_records = total_records
                if total_records >= 2000:
                    previous_time_segment_records = total_records
                    hour_delta = 1
                    # calculate total hours in between from_date and to_date time,convert seconds difference to hours
                    total_hours_range = (record.to_date - record.from_date).seconds // 3600
                    while total_records >= 2000:
                        new_to_date = record.to_date - timedelta(hours=hour_delta)
                        if new_to_date <= record.from_date:
                            raise Exception('Time goes beyond down from from_date time')

                        total_records = salesforce.search_count( sf_model=record.sf_model, from_date=record.from_date, to_date=new_to_date )
                        if total_records < 2000:
                            # change the current record to_date time and create a new record with from time
                            old_to_date = record.to_date
                            record.record_count = total_records
                            record.state = 'new'
                            record.to_date = new_to_date
                            # record.env.cr.commit()

                            # creating a new record with from_date = to_new_date
                            new_job = record.copy()
                            new_job.from_date = new_to_date
                            new_job.to_date = old_to_date
                            new_job.sf_offset = 0
                            new_job.state = 'new'
                            new_job.record_count = previous_time_segment_records - total_records
                            # new_job.env.cr.commit()
                            break

                        if hour_delta >= (total_hours_range/2):
                            hour_delta += 0.1
                        elif hour_delta >= (total_hours_range / 4):
                            hour_delta += 0.05
                        elif hour_delta >= (total_hours_range / 5):
                            hour_delta += 0.02
                        else:
                            hour_delta += 0.5
                else:
                    record.record_count = total_records
                    _logger.info('Total records are %s ', total_records)
                    # record.env.cr.commit()

                # if record_count is zero then no need to use that record
                if record.record_count == 0:
                    # record.state = 'done'
                    record.write({'state': 'done'})
                    record.import_status = 'imported'
                    record.env.cr.commit()
                    # record.env.cr.commit()
                    continue

                records = salesforce._query_to_salesforce(model=record.odoo_model, sf_model=record.sf_model,
                                                          from_date=record.from_date, to_date=record.to_date,
                                                          include_custom=record.include_custm,
                                                          offset=record.sf_offset, limit=record.max_rec_per_job)
                record.record_count = len(records) if records else 0
                # record.env.cr.commit()
                if record.max_rec_per_job > 0 and record.record_count > 0 and record.record_count == record.max_rec_per_job:
                    new_job = record.copy()
                    new_job.sf_offset += record.max_rec_per_job
                    new_job.state = 'new'
                    new_job.record_count = 0
                    # new_job.env.cr.commit()
                if records:
                    record.job_records = json.dumps(records)
                    # self.update_salesforce_data(salesforce,record, record.sf_model, record.odoo_model, records)
                # record.state = 'done'
                record.write({'state': 'done'})
                _logger.info('%s records are fetched ', record.record_count)
            except Exception as e:
                self.env.cr.rollback()
                record.state = 'failed'
                _logger.info('Commit to the DB,job failed')
                self.env['salesforce.sync.history'].create_log_param(record.sf_model, '',
                                                                     'failed', 'salesforce_to_odoo', e)

            finally:
                # for every record commit the changes,it affect only this record environment
                # because it is a different thread
                record.env.cr.commit()
                _logger.info('Commit to the DB')

        new_jobs = self.search([('state', 'in', ['new'])]) if all_job else False
        if not for_new:
            for_new = True

        if new_jobs:
            is_the_last_step = True
            self.env['sf.queue.jobs'].process_queue_jobs(for_new=for_new)

        salesforce.last_sync_date = fields.Date.today()
        #: After all the records are fetched ,start a cron and save the data
        if not is_the_last_step:
            cron_record = self.env.ref('salesforce_connector.sf_ir_cron_records_sync_process_1')
            if cron_record:
                model_names = list(type(self).all_sf_models)
                records = self.env['sf.queue.jobs'].search([('sf_model', 'in', model_names),
                                                            ('import_status', '=', 'not_imported')])
                try:
                    sorted_records_by_count = records.sorted(key=lambda r: r.record_count)
                    # ex_record_ids = [(r.id, r.record_count) for r in sorted_records_by_count]
                    all_records = []
                    salesforce = self.env['salesforce.connector'].browse(1)
                    if salesforce:
                        m = salesforce.max_rec_per_job
                    else:
                        m = 250

                    while True:
                        sub_rec = []
                        total = 0
                        for rec in sorted_records_by_count:
                            total = total + rec.record_count
                            if total <= m:
                                sub_rec.append(rec.id)
                            else:
                                all_records.append(sub_rec)
                                sub_rec = [rec.id]
                                total = rec.record_count
                                # if this record size is greater than the what we have specified then
                                # break that record into multiple records
                                if total > m:
                                    sf_records = json.loads(rec.job_records)
                                    total = len(sf_records)
                                    initial = 0
                                    next = m
                                    break_upper_limit = total // m
                                    _logger.info(f'Breaking up record in {break_upper_limit}')
                                    new_job_records_ids = []
                                    for i in range(break_upper_limit):
                                        new_job = rec.copy()
                                        new_job_records_ids.append(new_job.id)
                                        next_job_batch_record = sf_records[initial:next] or []
                                        # set record count for the new job
                                        new_job.record_count = len(next_job_batch_record)
                                        new_job.job_records = json.dumps(next_job_batch_record)
                                        # set job_records for the new job
                                        sf_records = sf_records[next:]
                                    # if still left something in sf_records create a
                                    if sf_records:
                                        rec.record_count = len(sf_records)
                                        rec.job_records = json.dumps(sf_records)
                                    else:
                                        rec.unlink()
                                    # set total to 0
                                    total = 0
                        # if sub_rec:
                        #     all_records.append(sub_rec)
                        break

                except Exception as e:
                    all_records = records.ids
                    _logger.info('Exception Occur %s, going single record processing ', e)

                next_exc_time = datetime.now() + timedelta(microseconds=200)
                cron_record.sudo().write({'nextcall': next_exc_time})
                cron_record.sudo().write({'active': True,
                                          'numbercall': 1
                                          })
                code_to_run = f"model.process_saving_records(records={all_records})"
                type(self).all_sf_models = set()
                cron_record.sudo().write({'code': code_to_run})

        # salesforce.env.cr.commit()

    def process_failed_records(self):
        cron_record = self.env.ref('salesforce_connector.sf_ir_cron_job_process')
        if cron_record:
            next_exc_time = datetime.now()
            cron_record.sudo().write({'nextcall': next_exc_time,
                                      'active': True,
                                      'numbercall': 1
                                      })
            cron_record.sudo().write({'code': 'model.process_queue_jobs(for_new=False)'})

    def update_salesforce_data(self, salesforce, record, sf_model, odoo_model, data):
        other = 0
        val = []
        for rec in data:
            json_data = salesforce._prepare_create_data(rec, odoo_model, sf_model)
            if '__not_needed_record' in json_data and len(json_data) == 1:
                other = other + 1
                continue

            if json_data:
                if sf_model == 'Opportunity':
                    json_data.update({'type': 'opportunity'})
                val.append(json_data)
        if val:
            try:
                salesforce._create_records_in_odoo(odoo_model.model, sf_model, val)
            except Exception as e:
                raise e
        else:
            if other != len(data):
                self.env['salesforce.sync.history'].create_log_param(sf_model, '',
                                                                     'failed',
                                                                     'salesforce_to_odoo', 'Field Mapping can not be done!')
                record.state = 'failed'

    def update_fields_on_records(self, model, sf_model):
        """
        This method update created by, last modified by, salesperson id by looking up salesforce user in odoo as well as
        in the salesforce if id is not found
        `The field name of above three fields should be`
        `sf_salesperson_id`, `sf_created_by_id`, `sf_last_modified_by_id`

        :param model: model record
        :param sf_model: the name of the salesforce model
        :return:
        """
        try:
            _logger.info('Started updating dates and users')
            # update fields on record such as create date and user_id
            # replace '.' with '_' in res.partner to make res_partner which is the actual table name in db
            model = model.model.replace('.', '_')
            # found where sf_ids are not updated
            records_q = f"""
                SELECT sf_salesperson_id,sf_created_by_id,sf_last_modified_by_id from {model} 
                WHERE sf_salesperson_id != 'NULL' or 
                sf_created_by_id !='NULL' or 
                sf_last_modified_by_id != 'NULL';
                """
            # print(records_q)
            self.env.cr.execute(records_q)
            results = self.env.cr.dictfetchall()
            # print()
            #: found unique sf_ids using set
            salesforce_ids = set()
            if results:
                for record in results:
                    if record['sf_salesperson_id']:
                        salesforce_ids.add(record['sf_salesperson_id'])
                    if record['sf_created_by_id']:
                        salesforce_ids.add(record['sf_created_by_id'])
                    if record['sf_last_modified_by_id']:
                        salesforce_ids.add(record['sf_last_modified_by_id'])

                existed_users_id = {}
                #: search res.users for the sf_ids
                users = self.env['res.users'].search(['|', ('active', '=', True), ('active', '=', False),
                                                      ('salesforce_user_id', 'in', list(salesforce_ids))])

                #: make a dict with sf_id : res_user.id
                for user in users:
                    existed_users_id[user.salesforce_user_id] = user.id
                #: found which sf_id don't have user
                remaining_users = salesforce_ids.difference(set(existed_users_id.keys()))
                remaining_users_info = {}
                #: call API for that sf_id and fetch the details of that ID
                if remaining_users:
                    remaining_users_info = self.env['salesforce.connector'].get_user_info(tuple(remaining_users))

                if remaining_users_info:
                    #: loop through the newly fetched ids
                    for remain_user in remaining_users_info:
                        new_user = self.env['res.users'].create({
                                'name': remain_user['Name'],
                                'salesforce_user_id': remain_user['Id'],
                                'email': remain_user['Username']+'.ODOO',
                                'login': remain_user['Username']+'.ODOO',
                                'active': remain_user['IsActive'],
                                'sel_groups_1_8_9': 1,
                        })
                        if new_user:
                            existed_users_id[remain_user['Id']] = new_user.id

                #: update the user_ids wherever necessary
                for user in existed_users_id:
                    user_id_q = f"UPDATE {model} SET user_id = {existed_users_id[user]} WHERE sf_salesperson_id = '{user}'"
                    create_id_q = f"UPDATE {model} SET create_uid = {existed_users_id[user]} WHERE sf_created_by_id = '{user}'"
                    modify_id_q = f"UPDATE {model} SET write_uid = {existed_users_id[user]} WHERE sf_last_modified_by_id = '{user}'"
                    self.env.cr.execute(user_id_q)
                    self.env.cr.execute(create_id_q)
                    self.env.cr.execute(modify_id_q)

                update_create_date = f"UPDATE {model} SET create_date = sf_created_date WHERE sf_created_date is not NULL"
                set_sf_create_date = f"UPDATE {model} SET sf_created_date = NULL WHERE sf_created_date is not NULL"

                #: put null wherever the res.users id are updated
                set_users = f"""
                            UPDATE {model} SET sf_salesperson_id = NULL,sf_created_by_id = NULL,
                            sf_last_modified_by_id = NULL 
                            WHERE sf_created_by_id is not null or 
                            sf_last_modified_by_id is not null or
                            sf_salesperson_id is not null
                            """
                self.env.cr.execute(update_create_date)
                self.env.cr.execute(set_sf_create_date)
                self.env.cr.execute(set_users)
                _logger.info('finished updating dates and users')

            if sf_model in ['Account', 'Contact']:
                self.get_account_records_image()

        except Exception as e:
            print(e)
            self.env['salesforce.sync.history'].create_log_param(
                    sf_model, '', 'failed',
                    'salesforce_to_odoo',
                    sf_model + ' record updation failed,record created ' + str(e))

    def get_account_records_image(self):
        salesforce = self.env['salesforce.connector'].browse(1)
        if not salesforce.sales_force:
            salesforce.connect_to_salesforce()

        photo_urls = self.env['res.partner'].search([('sf_photo_url', '!=', None)])
        try:
            sf_instance_url = f"https://{salesforce.sales_force.sf_instance}"
            for photo_url in photo_urls:
                #: create url for the account profile pic
                url = f"https://{salesforce.sales_force.sf_instance}{photo_url.sf_photo_url}"
                #: get the response for the url
                img_response = salesforce.sales_force._call_salesforce('GET', url)
                if img_response.status_code == 200 and not img_response.url.startswith(sf_instance_url):
                    base64_image = encodebytes(img_response.content)
                    res = photo_url.write({'image_1920': base64_image})
                    if res:
                        _logger.info('account record image updated- size %s', len(img_response.content))
                    else:
                        _logger.info('%s account record image failed to update status code %s', img_response.status_code)
                else:
                    _logger.info('Profile pic is placeholder, not updating, Skipping')
            update_photo_url = f"UPDATE res_partner SET sf_photo_url = null WHERE sf_photo_url is not NULL"
            self.env.cr.execute(update_photo_url)
        except Exception as e:
            _logger.info('Error occurred while updating image %s', e)


class SaveSalesforceData(models.Model):
    _name = 'sf.sync.data'
    _rec_name = 'field_name'
    _description = 'This is used to Sync/Save all the records in odoo'
    _order = 'id desc'

    field_name = fields.Char('salesforce_connector')
    include_custm = fields.Boolean('Include Custom Fields')
    accounts = fields.Boolean('Save Accounts')
    contacts = fields.Boolean('Save Contacts')
    individuals = fields.Boolean('Save Individuals')
    partner_ntwrk_con = fields.Boolean('Save Partner Network Connection')
    pricebook = fields.Boolean('Save Pricebook')
    rep__c = fields.Boolean('Save Rep__c')
    leads = fields.Boolean('Save Leads')
    opportunities = fields.Boolean('Save Opportunities')
    task = fields.Boolean('Save Task')
    from_date = fields.Date('From Date', store=True, required=True, compute="_compute_date",
                            default=fields.Date.today() + relativedelta(days=-7))
    to_date = fields.Date('To Date', store=True, required=True, compute="_compute_date", default=fields.Date.today())
    process_extra_fields = fields.Boolean('Process Dates and users?', default=True)
    re_import = fields.Boolean('Re-save already saved records?', default=False)

    max_rec_to_fetch = fields.Integer('Max Sales docs to fetch', default=100)
    max_tasks_to_covert = fields.Integer('Max Tasks per job', default=500)

    max_sale_attachments_to_process = fields.Integer('Max Sales URL records to process',default=300)
    sale_attachments_left = fields.Char('Total Opportunity records left to process', compute='left_for_attachment')
    tasks_left_to_convert = fields.Char('Total tasks left to convert', compute='tasks_left_for_conversion')

    # total sale order attachments present in the system
    total_sale_order_attachments = fields.Integer('Total Sale Order Attachments', compute='get_total_so_attachments')
    total_so_attachments_left_to_map = fields.Integer('Total Sale Order Attachments left to process',
                                                      compute='get_left_so_attachments')
    process_processed_order = fields.Boolean('Process Already Processed Order ', default=False)
    sf_records_ratio = fields.Html('All Sf Models Records Count', compute='get_salesforce_to_odoo_ratio', store=True)

    def get_salesforce_to_odoo_ratio(self):
        sf = self.env['salesforce.connector'].browse(1)
        if not sf.sales_force:
            sf.connect_to_salesforce()
        sf_models = self.env['sf.model.mapping'].search([])
        self.sf_records_ratio = ''
        new_total = []
        for sf_model in sf_models:
            try:
                # fetch total records count from salesforce
                query = "SELECT COUNT(Id) FROM {sf_model} where Id !=null".format(sf_model=sf_model.sf_model),
                records = sf.sales_force.query_all(query)['records']
                records_count = records[0].get('expr0', 0)
                # fetch total salesforce records from the mapped model
                salesforce_id = 'sf_id'
                if sf_model.o_model.model == 'res.partner':
                    if sf_model.sf_model == 'Contact':
                        salesforce_id = 'sf_contact_id'
                    if sf_model.sf_model == 'Account':
                        salesforce_id = 'sf_account_id'
                    if sf_model.sf_model == 'Individual':
                        salesforce_id = 'sf_individual_id'
                # set initial domain
                domain = [(salesforce_id, '!=', False),('active','in',[True,False])]
                if sf_model.o_model.model == 'crm.lead':
                    if sf_model.sf_model == 'Lead':
                        domain.append(('type','=','lead'))
                    if sf_model.sf_model == 'Opportunity':
                        domain.append(('type','=','opportunity'))

                sf_odoo_records = self.env[sf_model.o_model.model].search_count(domain)
                new_total.append(f'<p style="font-size:1.2rem;">{sf_model.sf_model}: <span style="color:green;">{sf_odoo_records}</span>'
                                 f'/<b>{records_count} </b></p>')
            except Exception as e:
                _logger.info(f'Error occur while counting records {e}')
                continue

        self.sf_records_ratio = ''.join(new_total)

    def refresh_total_records(self):
        self.get_salesforce_to_odoo_ratio()

    def get_left_so_attachments(self):
        total_so = self.env['sales.docs.url'].search([('title','ilike','sales order%'),('is_so_mapped', '=', False)])
        self.total_so_attachments_left_to_map = len(total_so)

    def get_total_so_attachments(self):
        total_so = self.env['sales.docs.url'].search([('title','ilike','sales order%')])
        self.total_sale_order_attachments = len(total_so)

    def left_for_attachment(self):
        # total salesforce opportunities
        total_saleforce_opps = self.env['crm.lead'].search([('type', '=', 'opportunity'), ('sf_id', '!=', False)])
        # ('sales_import_status', '=', 'not_imported')
        not_processes_ones = total_saleforce_opps.filtered(lambda opp: opp.sales_import_status == 'not_imported')
        self.sale_attachments_left = f'{len(not_processes_ones)} out of {len(total_saleforce_opps)}'

    def tasks_left_for_conversion(self):
        all_salesforce_tasks = self.env['salesforce.tasks'].search([('what_Type', '!=', False)])

        left_to_convert = all_salesforce_tasks.filtered(lambda task: not task.is_converted and task.what_Type)
        self.tasks_left_to_convert = f'{len(left_to_convert)} out of {len(all_salesforce_tasks)}'

    @api.onchange('max_rec_to_fetch')
    def on_change_max_rec_fetch(self):
        if self.max_rec_to_fetch and self.max_rec_to_fetch > 400:
            raise ValidationError(_('Max rec count can not be greater then 400'))

    def _compute_date(self):
        self.from_date = fields.Date.today() - relativedelta(days=-30)
        self.to_date = fields.Date.today()

    @api.onchange('from_date', 'to_date')
    def _validate_range_date(self):
        if self.from_date and self.to_date:
            if self.from_date > self.to_date or self.from_date == self.to_date:
                raise ValidationError(_('Date must be in valid range.!!'))

    def save_salesforce_data(self):
        flag = False
        type_of_record = []
        if self.accounts:
            flag = True
            type_of_record.append('Account')
        if self.contacts:
            flag = True
            type_of_record.append('Contact')
        if self.individuals:
            flag = True
            type_of_record.append('Individual')
        if self.partner_ntwrk_con:
            flag = True
            type_of_record.append('PartnerNetworkConnection')
        if self.pricebook:
            flag = True
            type_of_record.append('Pricebook2')
        if self.rep__c:
            flag = True
            type_of_record.append('Rep__c')
        if self.opportunities:
            flag = True
            type_of_record.append('Opportunity')
        if self.leads:
            flag = True
            type_of_record.append('Lead')
        if self.task:
            flag = True
            type_of_record.append('Task')

        if not flag:
            raise Warning(_("No Option Checked.",))

        if self.env.context.get('is_range_wise', False):
            self.start_cron_for_saving_data(type_of_record, True)
        else:
            self.start_cron_for_saving_data(type_of_record)

    def start_cron_for_saving_data(self, for_sf_model, is_range_wise=False):
        # Started cron for given sf_model like opportunity,Accounts,Individual
        cron_record = self.env.ref('salesforce_connector.sf_ir_cron_records_sync_process_1')
        if cron_record:
            import_status = ['not_imported', 're_import']
            #: if we re-import already imported records then we will search by both import_status
            #: i.e; imported and not_imported
            if self.re_import:
                import_status.append('imported')

            if is_range_wise:
                records = self.env['sf.queue.jobs'].search([('sf_model', 'in', for_sf_model),
                                                            ('import_status', 'in', import_status),
                                                            ('from_date', '>=', self.from_date),
                                                            ('from_date', '<=', self.to_date),
                                                            ('record_count', '>', 0)])
            else:
                records = self.env['sf.queue.jobs'].search([('sf_model', 'in', for_sf_model),
                                                            ('import_status', 'in', import_status),
                                                            ('record_count', '>', 0)])
            if self.re_import:
                #: if we re-importing the records then change the import_status to re_import
                for rec in records:
                    rec.import_status = 're_import'
            try:
                sorted_records_by_count = records.sorted(key=lambda r: r.record_count)
                # ex_record_ids = [(r.id, r.record_count) for r in sorted_records_by_count]
                all_records = []
                salesforce = self.env['salesforce.connector'].browse(1)
                if salesforce:
                    m = salesforce.max_rec_per_job
                else:
                    m = 250

                while True:
                    sub_rec = []
                    total = 0
                    for rec in sorted_records_by_count:
                        total = total + rec.record_count
                        if total <= m:
                            sub_rec.append(rec.id)
                        else:
                            all_records.append(sub_rec)
                            sub_rec = [rec.id]
                            total = rec.record_count
                            # if this record size is greater than the what we have specified then
                            # break that record into multiple records
                            if total > m:
                                sf_records = json.loads(rec.job_records)
                                total = len(sf_records)
                                initial = 0
                                next = m
                                break_upper_limit = total // m
                                _logger.info(f'Breaking up record in {break_upper_limit}')
                                new_job_records_ids = []
                                for i in range(break_upper_limit):
                                    new_job = rec.copy()
                                    new_job_records_ids.append(new_job.id)
                                    next_job_batch_record = sf_records[initial:next] or []
                                    # set record count for the new job
                                    new_job.record_count = len(next_job_batch_record)
                                    new_job.job_records = json.dumps(next_job_batch_record)
                                    # set job_records for the new job
                                    sf_records = sf_records[next:]
                                # if still left something in sf_records create a
                                if sf_records:
                                    rec.record_count = len(sf_records)
                                    rec.job_records = json.dumps(sf_records)
                                else:
                                    rec.unlink()
                                # set total to 0
                                total = 0
                    # if sub_rec:
                    #     all_records.append(sub_rec)
                    break
            except Exception as e:
                all_records = records.ids
                _logger.info('Exception Occur %s, going single record processing ', e)

            if records:
                next_exc_time = datetime.now() + timedelta(milliseconds=5)
                cron_record.sudo().write({'nextcall': next_exc_time,
                                          'active': True,
                                          'numbercall': 1
                                          })
                code_to_run = f"model.process_saving_records(records={all_records})"
                cron_record.sudo().write({'code': code_to_run})

    def process_saving_records(self, records=None):
        try:
            # cron_record = self.env.ref('salesforce_connector.sf_ir_cron_job_process')
            # set process_queue_jobs cron active to false so that it won't run again
            # we don't want it run again
            # cron_record.sudo().write({'active': False})
            if records:
                salesforce = self.env['salesforce.connector'].browse(1)
                #: pop a job_id pack from records
                job_id_pack = records.pop()
                if type(job_id_pack) != list:
                    job_id_pack = [job_id_pack]

                for job_id in job_id_pack:
                    job = self.env['sf.queue.jobs'].search([('id', '=', job_id)])
                    if job and job.job_records:
                        sf_records = []
                        try:
                            sf_records = json.loads(job.job_records)
                            _logger.info(f'Job contains {len(sf_records)}')
                            job.update_salesforce_data(salesforce, job, job.sf_model, job.odoo_model, sf_records)
                            job.import_status = 'imported'
                            if job.odoo_model and job.sf_model in ['Account', 'Contact', 'Individual', 'Lead',
                                                                   'Opportunity','Task']:
                                job.update_fields_on_records(job.odoo_model, job.sf_model)
                            _logger.info('%s job is processed', job.sf_model)
                            job.env.cr.commit()
                        except Exception as e:
                            job.env.cr.rollback()
                            job.import_status = 'not_imported'
                            _logger.info('%s Exception occur during commit in cron', e)
                            job.env['salesforce.sync.history'].create_log_param(
                                    job.sf_model, '', 'failed',
                                    'salesforce_to_odoo',
                                    job.sf_model + ' With error ' + str(e))
                        _logger.info('Processed %s records of %s ', len(sf_records), job.sf_model)
                        _logger.info('%s records are saved', len(sf_records))

        finally:
            cron_record = self.env.ref('salesforce_connector.sf_ir_cron_records_sync_process_2')
            if cron_record and records:
                next_exc_time = datetime.now() + timedelta(milliseconds=15)
                cron_record.write({'nextcall': next_exc_time,
                                   'active': True,
                                   'numbercall': 1})
                code_to_run = f"model.set_run_state_cron(records={records})"
                cron_record.write({'code': code_to_run})
            else:
                # when there are no more records to save then run `start_convert_task_to_activities` method
                # to convert tasks to activities and start the cron to fetch the opportunity attachments as well
                self.env.ref('salesforce_connector.sf_sync_record').start_convert_task_to_activities()
                # start converting salesforce tasks to activities
                self.env.ref('salesforce_connector.sf_sync_record').start_fetching_records_for_attachments()
                # start fetching records for opportunity attachments

    def set_run_state_cron(self, records):
        """
        This method is for helper cron job which will help calling in the main save cron
        so that it can run again ,it is acting like a helper cron job
        """
        cron_record = self.env.ref('salesforce_connector.sf_ir_cron_records_sync_process_1')
        if cron_record:
            next_exc_time = datetime.now() + timedelta(milliseconds=5)
            cron_record.write({'nextcall': next_exc_time,
                               'active': True,
                               'numbercall': 1
                               })
            code_to_run = f"model.process_saving_records(records={records})"
            cron_record.write({'code': code_to_run})

    def start_fetching_records_for_attachments(self):
        opp_s = self.env['crm.lead'].search([('type', '=', 'opportunity'), ('sf_id', '!=', False),
                                             ('sales_import_status', '=', 'not_imported')])
        all_records = []
        all_opp_s = opp_s.ids
        n = self.max_rec_to_fetch
        if opp_s:
            for i in range(0, len(all_opp_s), n):
                all_records.append(all_opp_s[i:i + n])

        cron_record = self.env.ref('salesforce_connector.sf_ir_cron_sales_doc_fetch_process_1')
        if cron_record and all_records:
            next_exc_time = datetime.now() + timedelta(milliseconds=5)
            cron_record.write({'nextcall': next_exc_time,
                               'active': True,
                               'numbercall': 1
                               })
            code_to_run = f"model.get_sale_order_document(records={all_records})"
            cron_record.write({'code': code_to_run})

    def start_saving_sales_docs_urls(self):
        sales_docs_url = self.env['sales.docs.url'].search(['&', ('status', '=', 'no'),
                                                            '|', ('type', 'in', ['application/pdf', 'pdf', 'PDF']),
                                                            ('title', 'ilike', '%.pdf')])

        all_records = []
        all_opp_s = sales_docs_url.ids
        n = self.max_rec_to_fetch
        if sales_docs_url:
            for i in range(0, len(all_opp_s), n):
                all_records.append(all_opp_s[i:i + n])

        cron_record = self.env.ref('salesforce_connector.sf_ir_cron_sales_doc_save_process_1')
        if cron_record and all_records:
            next_exc_time = datetime.now() + timedelta(milliseconds=5)
            cron_record.write({'nextcall': next_exc_time,
                               'active': True,
                               'numbercall': 1})
            code_to_run = f"model.save_sales_doc_attachments(records={all_records})"
            cron_record.write({'code': code_to_run})

    # start converting salesforce task to activities
    # group the task records into segments
    def start_convert_task_to_activities(self):
        """
        This is method that need to be called after fetching salesforce tasks, to convert them to odoo tasks
        we have to call this explicitly ,it won't run automatically
        :return:
        """
        all_salesforce_tasks = self.env['salesforce.tasks'].search([('is_converted', '=', False),
                                                                    ('what_Type', '!=', False)])

        all_records = []
        all_tasks = all_salesforce_tasks.ids
        n = self.max_tasks_to_covert
        if all_salesforce_tasks:
            for i in range(0, len(all_tasks), n):
                all_records.append(all_tasks[i:i + n])

        cron_record = self.env.ref('salesforce_connector.sf_tasks_conversion_process_1')
        if cron_record and all_records:
            next_exc_time = datetime.now() + timedelta(milliseconds=5)
            cron_record.write({'nextcall': next_exc_time,
                               'active': True,
                               'numbercall': 1
                               })
            code_to_run = f"model.convert_salesforce_tasks_to_activities(records={all_records})"
            cron_record.write({'code': code_to_run})

    def convert_salesforce_tasks_to_activities(self, records=None):
        try:
            related_res_model_names = {'Account': 'res.partner',
                                       'Opportunity': 'crm.lead'}
            if records:
                record_ids = records.pop()
                sf_tasks_recs = self.env['salesforce.tasks'].browse(record_ids)

                for sf_task_rec in sf_tasks_recs:
                    #: get the related opportunity record for this sales doc url
                    # sf_task_rec = self.env['salesforce.tasks'].browse([sf_task_rec_id])
                    if not sf_task_rec.What or not sf_task_rec.what_Type:
                        sf_task_rec.conversion_status = 'No Related model/record ID is present'
                        continue

                    if not sf_task_rec.user_id:
                        sf_task_rec.conversion_status = 'No User id present on this task'
                        continue

                    if not sf_task_rec.Type:
                        sf_task_rec.conversion_status = 'No Task type present'
                        continue

                    res_model_name = related_res_model_names[sf_task_rec.what_Type]
                    mail_activity_type_id = self.env['salesforce.task.type.mapping'].search([('task_name','=', sf_task_rec.Type.id)], limit=1)
                    if not mail_activity_type_id:
                        sf_task_rec.conversion_status = 'No Related mail activity type is present'
                        continue

                    search_domain = []
                    if res_model_name == 'crm.lead':
                        search_domain = [('sf_id','=', sf_task_rec.What), ('type','=','opportunity')]
                    elif res_model_name == 'res.partner':
                        search_domain = [('sf_account_id','=', sf_task_rec.What)]

                    opp_rec = self.env[res_model_name].search(search_domain, limit=1)
                    if not opp_rec:
                        sf_task_rec.conversion_status = 'No related record found'
                        continue
                    try:
                        res_model = self.env['ir.model'].search([('model', '=', res_model_name)])
                        mail_activity_values = {'res_model_id': res_model.id,
                                                'user_id': sf_task_rec.user_id.id,
                                                'res_id': opp_rec.id,
                                                'activity_type_id': mail_activity_type_id.mapped_task_name.id,
                                                'summary': sf_task_rec.Subject,
                                                'date_deadline': sf_task_rec.ActivityDate or datetime.now()
                                                }

                        create_uid = sf_task_rec.user_id
                        user_id = sf_task_rec.user_id

                        if sf_task_rec.create_uid:
                            create_uid = sf_task_rec.create_uid

                        activity_res = self.env['mail.activity'].with_user(create_uid).sudo().with_context({'mail_activity_quick_update': True}).create(mail_activity_values)
                        if activity_res:
                            activity_res.imported_task_id = sf_task_rec.id
                            sf_task_rec.activity_id = activity_res.id
                            sf_task_rec.is_converted = True
                            sf_task_rec.conversion_status = 'Activity Created'

                            _logger.info(f'Activity created for task rec {sf_task_rec.id}')
                            if sf_task_rec.Status.lower() == 'completed':
                                cTX = self.env.context.copy()
                                cTX['no_lead_score_popup'] = True
                                cTX['import_salesforce_tasks'] = True
                                cTX['CompletedDateTime'] = sf_task_rec.CompletedDateTime
                                comments = sf_task_rec.Description
                                mail_message_id = activity_res.with_user(user_id).sudo().with_context(cTX).action_feedback(feedback=comments)
                                if mail_message_id:
                                    activity_done_date = sf_task_rec.CompletedDateTime or datetime.now()
                                    query = f"Update mail_message set imported_task_id={sf_task_rec.id}," \
                                            f"date='{activity_done_date}',create_date='{activity_done_date}'," \
                                            f"write_date='{activity_done_date}' where id={mail_message_id}"
                                    self.env.cr.execute(query)
                                    sf_task_rec.activity_message_id = mail_message_id
                                    # sf_task_rec.is_converted = True
                                    sf_task_rec.conversion_status = 'Activity Created and set to done'
                                    _logger.info('Mail message date updated')

                            activity_exist = self.env['mail.activity'].sudo().browse(activity_res.ids)
                            if activity_exist:
                                create_date = sf_task_rec.create_date
                                query = f"Update mail_activity set create_date='{create_date}' where id={activity_exist.id}"
                                self.env.cr.execute(query)
                                _logger.info('Activity create date updated')

                    except Exception as e:
                        sf_task_rec.conversion_status = str(e)
                        self.env['salesforce.sync.history'].create_log_param(
                                'Task','', 'failed', 'salesforce_to_odoo',
                                f"task conversion failed for {opp_rec.name} with error {str(e)}")
        except Exception as e:
            self.env['salesforce.sync.history'].create_log_param(
                    'Task', '', 'failed', 'salesforce_to_odoo',
                    f"task conversion failed with error {str(e)}")
            _logger.info('task conversion failed with %s', str(e))

        finally:
            cron_record = self.env.ref('salesforce_connector.sf_tasks_conversion_helper_process_2')
            if cron_record and records:
                next_exc_time = datetime.now() + timedelta(milliseconds=1)
                cron_record.write({'nextcall': next_exc_time,
                                   'active': True,
                                   'numbercall': 1
                                   })
                code_to_run = f"model.helper_convert_salesforce_tasks(records={records})"
                cron_record.write({'code': code_to_run})
            elif cron_record and not records:
                # empty the argument list from the helper cron job
                next_exc_time = datetime.now() + timedelta(milliseconds=1)
                cron_record.write({'nextcall': next_exc_time})
                code_to_run = f"model.helper_convert_salesforce_tasks(records=None)"
                cron_record.write({'code': code_to_run})
                _logger.info('All tasks are converted!!')

    def helper_convert_salesforce_tasks(self, records):
        """
        This method is for helper cron job which will help calling in the main save cron
        so that it can run again ,it is acting like a helper cron job
        """
        cron_record = self.env.ref('salesforce_connector.sf_tasks_conversion_process_1')
        if cron_record and records:
            next_exc_time = datetime.now() + timedelta(milliseconds=1)
            cron_record.write({'nextcall': next_exc_time,
                               'active': True,
                               'numbercall': 1
                               })
            code_to_run = f"model.convert_salesforce_tasks_to_activities(records={records})"
            cron_record.write({'code': code_to_run})
        elif cron_record and not records:
            code_to_run = f"model.convert_salesforce_tasks_to_activities(records=None)"
            cron_record.write({'code': code_to_run})

    def start_for_sale_order_processing(self):
        so_mapped_values = [False]
        if self.process_processed_order:
            so_mapped_values.append(True)
        all_salesforce_urls = self.env['sales.docs.url'].search([('title','ilike','sales order%'),
                                                                 ('is_so_mapped', 'in', so_mapped_values)])
        all_records = []
        all_urls = all_salesforce_urls.ids
        n = self.max_sale_attachments_to_process
        if all_salesforce_urls:
            for i in range(0, len(all_urls), n):
                all_records.append(all_urls[i:i + n])

        cron_record = self.env.ref('salesforce_connector.sf_sale_order_opp_mapping_process_1')
        if cron_record:
            next_exc_time = datetime.now() + timedelta(milliseconds=1)
            cron_record.write({'nextcall': next_exc_time,
                               'active': True,
                               'numbercall': 1
                               })
            code_to_run = f"model.process_sale_order_file_name(records={all_records})"
            cron_record.write({'code': code_to_run})


class InheritedMailActivityForTasks(models.Model):
    _inherit = 'mail.activity'

    # inheriting this because we need the author id to be set for the activity that is made from salesforce task
    # otherwise it will show system/OdooBot
    def _action_done(self, feedback=False, attachment_ids=None):
        if self.env.context.get('import_salesforce_tasks'):
            messages = self.env['mail.message']
            activity_message = False
            for activity in self:
                record = self.env[activity.res_model].sudo().browse(activity.res_id)
                if 'date_done' in self._fields:
                    # update completion time, done , active fields
                    activity_values = {'date_done': self.env.context.get('CompletedDateTime', datetime.now()),
                                       'done': True,
                                       'active': False}
                    activity.with_user(activity.user_id).sudo().write(activity_values)

                record.with_user(activity.user_id).sudo().message_post_with_view(
                        'mail.message_activity_done',
                        values={
                                'activity': activity,
                                'feedback': feedback,
                                'display_assignee': False
                        },
                        subtype_id=self.env['ir.model.data'].xmlid_to_res_id('mail.mt_activities'),
                        mail_activity_type_id=activity.activity_type_id.id,
                        author_id=activity.user_id.partner_id.id,
                        email_from=activity.user_id.partner_id.email,
                        attachment_ids=[],
                )
                activity_message = record.message_ids[0]
                messages |= activity_message
            return activity_message, False
        return super(InheritedMailActivityForTasks, self)._action_done(feedback=feedback, attachment_ids=attachment_ids)


class OpportunitySalesDocs(models.Model):
    _name = 'opportunity.sales.docs'
    _description = 'Model for storing attachment url for salesforce opportunity sales docs'

    _rec_name = 'opp_name'
    opp_name = fields.Many2one('crm.lead', string='Opportunity')
    all_urls = fields.One2many('sales.docs.url', 'ref_sales_doc_opp', string='No of attachments')
    fetched_attachments = fields.Integer(string='No of fetched attachments', default=0, compute='count_fetched_att_s')
    is_attachments = fields.Boolean('Any attachments?', default=False)

    def count_fetched_att_s(self):
        for rec in self:
            if rec.all_urls:
                rec.fetched_attachments = len(rec.all_urls.filtered(lambda x: x.status == 'yes'))

    def fetch_record_type_file(self, salesforce, file_ids, sf_id):
        """
        Fetching those records having RecordType as File from salesforce.
        This method queries VersionData Object of salesforce to query
        :param salesforce:
        :param file_ids:
        :param sf_id:
        :return:
        """
        query = ''
        if len(file_ids) > 1:
            query = "SELECT Id,VersionData,Title,FileType FROM ContentVersion where ContentDocumentId in {att_ids}" \
                .format(att_ids=tuple(file_ids))
        elif len(file_ids) == 1:
            query = "SELECT Id,VersionData,Title,FileType FROM ContentVersion where ContentDocumentId = '{att_ids}'" \
                .format(att_ids=file_ids[0])
        if query and sf_id:
            att_records = salesforce.sales_force.query_all(query)['records']
            if att_records:
                all_urls = []
                for sf_at_rec in att_records:
                    if sf_at_rec.get('VersionData', ''):
                        attachment_url = sf_at_rec.get('VersionData', '')
                        if attachment_url:
                            new_att_record = {'name': attachment_url,
                                              'title': sf_at_rec.get('Title'),
                                              'type': sf_at_rec.get('FileType'),
                                              'record_type': 'File'
                                              }
                            if new_att_record:
                                all_urls.append((0, 0, new_att_record))

                if all_urls:
                    opp_id = self.env['crm.lead'].search([('sf_id', '=', sf_id)], limit=1)
                    sale_doc_url = {'opp_name': opp_id.id,
                                    'is_attachments': True,
                                    'all_urls': all_urls
                                    }
                    res = self.env['opportunity.sales.docs'].create(sale_doc_url)
                    if res:
                        opp_id.write({'sales_import_status': 'imported'})
                        self.env['salesforce.sync.history'].create_log_param(
                                'Opportunity', opp_id.sf_id, 'success',
                                'salesforce_to_odoo', f"File Record for opportunity {opp_id.name}")
                        _logger.info(f'File record saved for sf_id {sf_id}')
                    else:
                        _logger.info(f'File record saved failed for sf_id {sf_id} ')

    def fetch_record_type_attachment(self, salesforce, attachment_ids):
        """
        Fetching those records having RecordType as Attachment from salesforce.
        This method queries Attachment Object of salesforce
        :param salesforce:
        :param attachment_ids:
        :return:
        """
        query = ''
        if len(attachment_ids) > 1:
            query = "SELECT Id,ParentId,Name,ContentType,Body FROM Attachment where Id in {att_ids}" \
                .format(att_ids=tuple(attachment_ids))
        elif len(attachment_ids) == 1:
            query = "SELECT Id,ParentId,Name,ContentType,Body FROM Attachment where Id = '{att_ids}'" \
                .format(att_ids=attachment_ids[0])
        if query:
            att_records = salesforce.sales_force.query_all(query)['records']
            if att_records:
                all_urls = []
                for sf_at_rec in att_records:
                    if sf_at_rec.get('ParentId', False) and sf_at_rec.get('Body', ''):
                        attachment_url = sf_at_rec.get('Body', '')
                        if attachment_url:
                            new_att_record = {'name': attachment_url,
                                              'title': sf_at_rec.get('Name'),
                                              'type': sf_at_rec.get('ContentType'),
                                              'record_type': 'Attachment'
                                              }
                            if new_att_record:
                                all_urls.append((0, 0, new_att_record))

                if all_urls:
                    sf_id = att_records[0].get('ParentId', False)
                    opp_id = self.env['crm.lead'].search([('sf_id', '=', sf_id)], limit=1)
                    sale_doc_url = {'opp_name': opp_id.id,
                                    'is_attachments': True,
                                    'all_urls': all_urls
                                    }
                    res = self.env['opportunity.sales.docs'].create(sale_doc_url)
                    if res:
                        opp_id.write({'sales_import_status': 'imported'})
                        self.env['salesforce.sync.history'].create_log_param(
                                'Opportunity', opp_id.sf_id, 'success',
                                'salesforce_to_odoo', f"Attachment Record for opportunity {opp_id.name}")
                        _logger.info(f'Attachment record saved for sf_id {sf_id}')
                    else:
                        _logger.info(f'Attachment record saved failed for sf_id {sf_id} ')

    def get_sale_order_document(self, records=None):
        salesforce = self.env['salesforce.connector'].browse(1)
        if not salesforce.sales_force:
            salesforce.connect_to_salesforce()
        if salesforce.sales_force and records:
            record_ids = records.pop()
            sales_job_record = self.env['crm.lead'].browse(record_ids)
            # fetching the sales docs based on the salesforce id and not part number
            all_sf_ids = [sf_rec.sf_id for sf_rec in sales_job_record]
            if all_sf_ids:
                try:
                    query = "SELECT (SELECT Id,ParentId,Title,RecordType FROM CombinedAttachments where ParentId in {opp_id})" \
                            " FROM Opportunity WHERE Id in {opp_id}".format(opp_id=tuple(all_sf_ids))
                    #: All CombinedAttachments records
                    com_att_records = salesforce.sales_force.query_all(query)['records']
                    for rec in com_att_records:
                        if rec.get('CombinedAttachments', False):
                            attachments = rec['CombinedAttachments'].get('records')
                            attachment_ids = [at_rec['Id'] for at_rec in attachments if
                                              at_rec.get('RecordType') == 'Attachment']

                            file_ids = [at_rec['Id'] for at_rec in attachments if
                                        at_rec.get('RecordType') == 'File']
                            if attachment_ids:
                                self.fetch_record_type_attachment(salesforce, attachment_ids)
                            if file_ids:
                                opp_parent_id = attachments[0].get('ParentId', False)
                                self.fetch_record_type_file(salesforce, file_ids, opp_parent_id)
                    salesforce.env.cr.commit()

                except Exception as e:
                    sales_job_record.env.cr.rollback()
                    self.env['salesforce.sync.history'].create_log_param(
                            'Opportunity', '', 'failed', 'salesforce_to_odoo',
                            f"Attachment fetching failed with error {str(e)}")
                finally:
                    # call the helper cron job to start this job again if records are still remaining
                    cron_record = self.env.ref('salesforce_connector.sf_ir_cron_sales_doc_fetch_process_2')
                    if cron_record and records:
                        next_exc_time = datetime.now() + timedelta(milliseconds=1)
                        cron_record.write({'nextcall': next_exc_time,
                                           'active': True,
                                           'numbercall': 1
                                           })
                        code_to_run = f"model.helper_fetch_sales_docs(records={records})"
                        cron_record.write({'code': code_to_run})
                    else:
                        # after fetching all the records start saving them too
                        self.env.ref('salesforce_connector.sf_sync_record').start_saving_sales_docs_urls()
                        _logger.info('All fetching of sales docs of opportunity been done!!')

    def fetch_current_record_attachments(self):
        try:
            salesforce = self.env['salesforce.connector'].browse(1)
            if not salesforce.sales_force:
                salesforce.connect_to_salesforce()
            for rec in self:
                #: create url for fetching the attachment
                for sf_att_rec in rec.all_urls:
                    if sf_att_rec.type in ['application/pdf', 'pdf', 'PDF'] or sf_att_rec.title.find('.pdf') != -1 or sf_att_rec.title.find('.PDF') != -1:
                        url = f"https://{salesforce.sales_force.sf_instance}{sf_att_rec.name}"
                        #: get the response for the attachment
                        file_response = salesforce.sales_force._call_salesforce('GET', url)
                        if file_response.status_code == 200:
                            base64_data = encodebytes(file_response.content)
                            if base64_data:
                                new_attachment = [{'name': sf_att_rec.title,
                                                   'datas': base64_data,
                                                   'res_model': 'crm.lead',
                                                   'res_id': rec.opp_name.id}]

                                res = self.env['ir.attachment'].create(new_attachment)
                                if res:
                                    sf_att_rec.write({'attachment': [res.id], 'status': 'yes'})
                                    self.env['salesforce.sync.history'].create_log_param(
                                            'Opportunity', rec.opp_name.sf_id, 'success',
                                            'salesforce_to_odoo', f"{len(res)} Attachment save for opportunity {rec.opp_name.name}")
        except Exception as e:
            self.env['salesforce.sync.history'].create_log_param(
                    'Opportunity', '', 'failed', 'salesforce_to_odoo',
                    f"Attachment fetching failed with error {str(e)}")
            _logger.info('Attachment fetching failed with %s', str(e))

    def helper_fetch_sales_docs(self, records):
        """
        This method is for helper cron job which will help calling in the main fetch cron
        so that it can run again ,it is acting like a helper cron fetch job
        """
        cron_record = self.env.ref('salesforce_connector.sf_ir_cron_sales_doc_fetch_process_1')
        if cron_record:
            next_exc_time = datetime.now() + timedelta(milliseconds=1)
            cron_record.write({'nextcall': next_exc_time,
                               'active': True,
                               'numbercall': 1
                               })
            code_to_run = f"model.get_sale_order_document(records={records})"
            cron_record.write({'code': code_to_run})

    def helper_save_sales_docs(self, records):
        """
        This method is for helper cron job which will help calling in the main save cron
        so that it can run again ,it is acting like a helper cron job
        """
        cron_record = self.env.ref('salesforce_connector.sf_ir_cron_sales_doc_save_process_1')
        if cron_record and records:
            next_exc_time = datetime.now() + timedelta(milliseconds=1)
            cron_record.write({'nextcall': next_exc_time,
                               'active': True,
                               'numbercall': 1
                               })
            code_to_run = f"model.save_sales_doc_attachments(records={records})"
            cron_record.write({'code': code_to_run})

    def save_sales_doc_attachments(self, records=None):
        try:
            salesforce = self.env['salesforce.connector'].browse(1)
            if not salesforce.sales_force:
                salesforce.connect_to_salesforce()
                #: create url for fetching the attachment
            #: pop first batch of record ids from the batch of record ids
            record_ids = records.pop()
            sales_docs_urls = self.env['sales.docs.url'].browse(record_ids)
            for sf_att_rec in sales_docs_urls:
                #: get the related opportunity record for this sales doc url
                opp_rec = sf_att_rec.ref_sales_doc_opp.opp_name
                try:
                    if sf_att_rec.type in ['application/pdf', 'pdf', 'PDF'] or sf_att_rec.title.find('.pdf') != -1 or sf_att_rec.title.find('.PDF') != -1:
                        url = f"https://{salesforce.sales_force.sf_instance}{sf_att_rec.name}"
                        #: get the response for the attachment
                        file_response = salesforce.sales_force._call_salesforce('GET', url)
                        if file_response.status_code == 200:
                            base64_data = encodebytes(file_response.content)
                            if base64_data:
                                new_attachment = [{'name': sf_att_rec.title,
                                                   'datas': base64_data,
                                                   'res_model': 'crm.lead',
                                                   'res_id': opp_rec.id}]

                                res = self.env['ir.attachment'].create(new_attachment)
                                if res:
                                    _logger.info('Attachment saved from salesforce!!')
                                    sf_att_rec.write({'attachment': [res.id], 'status': 'yes'})
                                    self.env['salesforce.sync.history'].create_log_param(
                                            'Opportunity', opp_rec.sf_id, 'success',
                                            'salesforce_to_odoo',
                                            f"{len(res)} Attachment save for opportunity {opp_rec.name}")
                except Exception as e:
                    self.env['salesforce.sync.history'].create_log_param(
                            'Opportunity', opp_rec.sf_id, 'failed', 'salesforce_to_odoo',
                            f"Attachment saving failed for {opp_rec.name} with error {str(e)}")

            salesforce.env.cr.commit()
        except Exception as e:
            self.env['salesforce.sync.history'].create_log_param(
                    'Opportunity', '', 'failed', 'salesforce_to_odoo',
                    f"Attachment saving failed with error {str(e)}")
            _logger.info('Attachment saving failed with %s', str(e))

        finally:
            cron_record = self.env.ref('salesforce_connector.sf_ir_cron_sales_doc_save_process_2')
            if cron_record and records:
                next_exc_time = datetime.now() + timedelta(milliseconds=1)
                cron_record.write({'nextcall': next_exc_time,
                                   'active': True,
                                   'numbercall': 1
                                   })
                code_to_run = f"model.helper_save_sales_docs(records={records})"
                cron_record.write({'code': code_to_run})
            else:
                # after saving them start mapping for sage sale orders
                self.env.ref('salesforce_connector.sf_sync_record').start_for_sale_order_processing()
                _logger.info('All sales url been processed!!')


int_match_pattern = re.compile('\d+')


class SalesDocsUrls(models.Model):
    _name = 'sales.docs.url'
    _description = 'Model for storing sales doc attachment url'

    _rec_name = 'title'
    name = fields.Char('Doc URL')
    title = fields.Char('File Name')
    type = fields.Char('Doc type')
    ref_sales_doc_opp = fields.Many2one('opportunity.sales.docs', ondelete='cascade')
    attachment = fields.Many2many('ir.attachment', ondelete='cascade')
    record_type = fields.Selection([('Attachment', 'Attachment'), ('File', 'File')], string='Record Type')
    status = fields.Selection([('yes', 'yes'), ('no', 'no')], default='no', string='Fetch Status')
    rel_sale_order = fields.Many2one('sale.order', ondelete='cascade')
    is_so_mapped = fields.Boolean(default=False)

    def fetch_current_record_url(self):
        try:
            salesforce = self.env['salesforce.connector'].browse(1)
            if not salesforce.sales_force:
                salesforce.connect_to_salesforce()
            for rec in self:
                #: create url for fetching the attachment
                if rec.name:
                    url = f"https://{salesforce.sales_force.sf_instance}{rec.name}"
                    #: get the response for the attachment
                    file_response = salesforce.sales_force._call_salesforce('GET', url)
                    if file_response.status_code == 200:
                        base64_data = encodebytes(file_response.content)
                        if base64_data:
                            new_attachment = [{'name': rec.title,
                                               'datas': base64_data,
                                               'res_model': 'crm.lead',
                                               'res_id': rec.ref_sales_doc_opp.opp_name.id}]

                            res = self.env['ir.attachment'].create(new_attachment)
                            if res:
                                rec.write({'attachment': [res.id], 'status': 'yes'})
                                self.env['salesforce.sync.history'].create_log_param(
                                        'Opportunity', rec.ref_sales_doc_opp.opp_name.sf_id, 'success',
                                        'salesforce_to_odoo',
                                        f"{len(res)} Attachment save for opportunity {rec.ref_sales_doc_opp.opp_name.name}")
        except Exception as e:
            self.env['salesforce.sync.history'].create_log_param(
                    'Opportunity', '', 'failed', 'salesforce_to_odoo',
                    f"Attachment saving failed with error {str(e)}")
            _logger.info('Attachment saving failed with %s', str(e))

    def process_sale_order_file_name(self, records=None):
        all_records = records.pop()
        for rec_id in all_records:
            rec = self.env['sales.docs.url'].browse([rec_id])
            rec.map_file_to_sale_order()

        cron_record = self.env.ref('salesforce_connector.sf_sale_order_opp_mapping_process_2')
        if cron_record:
            next_exc_time = datetime.now() + timedelta(milliseconds=1)
            cron_record.write({'nextcall': next_exc_time,
                               'active': True,
                               'numbercall': 1
                               })
            code_to_run = f"model.helper_process_sale_order_file_name(records={records})"
            cron_record.write({'code': code_to_run})

    def map_file_to_sale_order(self):
        rec = self
        rec.rel_sale_order = False
        # if the file name of the attachment starts with sales order and there is a related opportunity.sales.docs
        if rec.title.lower().startswith('sales order') and rec.ref_sales_doc_opp:
            # extract out the sale order number from file name
            match_so_number = int_match_pattern.search(rec.title)
            # if there is a match for a number pattern
            if match_so_number:
                # grab the first group
                try:
                    so_number = int(match_so_number.group(0))
                    so_rec = self.env['ir.model.data'].search([('model', '=', 'sale.order'),
                                                               ('module', '=', '__import__'),
                                                               ('name', '=', so_number)], limit=1)
                    if so_rec:
                        _logger.info(f'{so_number} found in import records')
                        rec.rel_sale_order = so_rec.res_id
                        # correct duplicate order lines
                        self.delete_duplicate_order_lines(rec.rel_sale_order)
                        rec.rel_sale_order.with_context({'sage_data_processing': True,
                                                         'tracking_disable': True}).opportunity_id = rec.ref_sales_doc_opp.opp_name.id
                        _logger.info(f'new opportunity id linked to the imported sale order')
                        self.get_product_from_sale_order(rec.rel_sale_order.opportunity_id, rec.rel_sale_order)
                        # check for customer on sale order it might be wrong in some cases when there are similiar names
                        if rec.rel_sale_order.partner_id.id != rec.rel_sale_order.opportunity_id.partner_id.id:
                            rec.rel_sale_order.partner_id = rec.rel_sale_order.opportunity_id.partner_id.id
                            # sage_data_processing: so that we can disable tracking when we are prcoessing sage sale orders
                            rec.rel_sale_order.with_context(
                                    {'sage_data_processing': True, 'tracking_disable': True}).onchange_partner_id()
                        self.update_product_partner_id(rec.rel_sale_order)
                        self.get_related_purchase_order(rec.rel_sale_order)
                        rec.is_so_mapped = True
                except ValueError as e:
                    _logger.error(f'Error occurred during sale order attachment processing {str(e)}')


    def helper_process_sale_order_file_name(self, records):
        cron_record = self.env.ref('salesforce_connector.sf_sale_order_opp_mapping_process_1')
        if cron_record and records:
            next_exc_time = datetime.now() + timedelta(milliseconds=1)
            cron_record.write({'nextcall': next_exc_time,
                               'active': True,
                               'numbercall': 1
                               })
            code_to_run = f"model.process_sale_order_file_name(records={records})"
            cron_record.write({'code': code_to_run})

    def update_product_partner_id(self, sale_order):
        if sale_order:
            this_order_products = sale_order.order_line.mapped('product_id')
            for product in this_order_products:
                product.product_partner_id = sale_order.opportunity_id.partner_id.id
                _logger.info(f'Partner id changed for product {product.display_name}')

    def get_related_purchase_order(self, sale_order):
        if sale_order:
            so_products = sale_order.order_line.mapped('product_id')
            for product in so_products:
                rel_po = self.env['purchase.order.line'].search([('product_id','=', product.id)], limit=1)
                if rel_po and rel_po.order_id:
                    rel_po.order_id.sale_ids = [(4, sale_order.id)]
                    _logger.info(f'PO found for {sale_order.id}')

    def get_product_from_sale_order(self, opportunity, sale_order):
        """
        It returns the first of all board products found in the sale order
        :param sale_order:
        :param opportunity:
        :return:
        """
        if sale_order:
            board_products_lines = sale_order.order_line.filtered(lambda line: line.ref_product_is_board)
            if board_products_lines:
                so_product = board_products_lines[0].product_id
                opportunity.with_context({'sage_data_processing': True,'tracking_disable':True}).name = so_product.customer_part_number
                opportunity.with_context({'sage_data_processing': True,'tracking_disable':True}).rev_code = so_product.customer_part_number_rev_code
                opportunity.with_context({'sage_data_processing': True,'tracking_disable':True}).opportunity_product_template_id = so_product.product_tmpl_id.id

    def delete_duplicate_order_lines(self, sale_order):
        # key:product_id and value:{'qty': 10,'lead_time': '1 to 2 days'}
        order_line_set = defaultdict(list)
        order_lines_to_delete = []
        for order_line in sale_order.order_line:
            # if it is a new product store it as id: {qty:qty,lead_time:lead_time}
            if order_line.product_id.id not in order_line_set:
                order_line_set[order_line.product_id.id].append({'qty': order_line.product_uom_qty,
                                                                 'lead_time': order_line.lead_time
                                                                 })
            else:
                # if the order line has product_id that already existed in the order_line_set
                # check the quantity and lead time, if its a match with already existing order line add it
                # in the order_lines_to_delete list
                existing_lines = order_line_set[order_line.product_id.id]
                flag = False
                for existing_line in existing_lines:
                    if order_line.product_uom_qty == existing_line['qty'] and \
                            order_line.lead_time == existing_line['lead_time']:
                        order_lines_to_delete.append(order_line.id)
                        flag = True
                        break

                if not flag:
                    order_line_set[order_line.product_id.id].append({'qty': order_line.product_uom_qty,
                                                                     'lead_time': order_line.lead_time
                                                                     })

        if order_lines_to_delete:
            _logger.info(f'Order lines deleted from {sale_order.id}-{sale_order.name}')
            self.env['sale.order.line'].with_context({'sage_data_processing': True}).browse(order_lines_to_delete).unlink()
