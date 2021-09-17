from odoo import models, fields, api
import os
import csv
from io import StringIO
import base64
from collections import defaultdict
import logging
_logger = logging.getLogger(__name__)


class ProcessSageData(models.Model):
	_name = 'process.sage.data.csv'
	_description = 'To process Sage csv files'
	_rec_name = 'field_name'
	field_name = fields.Char('CSV Process')
	csv_file = fields.Many2many('ir.attachment',string='Upload Single Sale Order Processed CSV')
	processed_file = fields.Many2many('ir.attachment',relation='sage_processes_csv_file',
	                                  string='Prcoessed Single Sale Order Processed CSV')
	external_id_map = fields.One2many('field.name.map.external.id', 'rel_process_id', string='Field mappings')
	import_model_name = fields.Many2one('ir.model',string='Import model name')

	def start_csv_processing(self):
		print('Start csv processing')
		if self.csv_file:
			p, ext = os.path.splitext(self.csv_file[0].name)
			if ext in ['.csv']:
				file_data = base64.b64decode(self.csv_file[0].datas).decode('utf-8')
				csv_reader = csv.DictReader(StringIO(file_data))

				field_names = csv_reader.fieldnames
				method = self.env.context.get('method')
				if hasattr(self, method):
					getattr(self, method)(csv_reader, field_names)

	def process_sale_order(self, csv_reader,file_write_data, field_names):
		for field_map in self.external_id_map.filtered(lambda x: x.import_model_name.id == self.import_model_name.id):
			field_names.append(f'{field_map.field_name}/dbid')

		csv_writer = csv.DictWriter(file_write_data, fieldnames=field_names)
		csv_writer.writeheader()

		new_record = False
		for row in csv_reader:
			# partner_id = row['partner_id/id']
			# if prev_partner_found and partner_id == '' and row['id'] == '':
			# 	csv_writer.writerow(row)
			# 	continue
			# elif not prev_partner_found and (partner_id == '' and row['id'] == ''):
			# 	continue

			# check if partner exists in this system, if do find its external_id and add it and write to another csv
			for field_map in self.external_id_map.filtered(lambda x: x.import_model_name.id == self.import_model_name.id):
				external_id, existing_record_id = self.find_record_external_id(row, field_map)
				if external_id and existing_record_id:
					row[field_map.field_name] = external_id
					row[f'{field_map.field_name}/dbid'] = existing_record_id
			csv_writer.writerow(row)
			# _logger.info(f'{i} row processed')

	def get_fields_list(self, csv_field_names):
		actual_field_names = set()
		field_to_csv_map = defaultdict(list)
		for csv_name in csv_field_names:
			converted_name = csv_name
			if '/' in csv_name:
				converted_name = csv_name.split('/')[0]
			field_to_csv_map[converted_name].append(csv_name)
			actual_field_names.add(converted_name)

		# model_import_fields = model_fields.filtered(lambda x: x.name in actual_field_names).mapped('ttype')
		all_fields = self.env['ir.model.fields'].search([('model_id', '=', self.import_model_name.id),
		                                    ('name','in', list(actual_field_names))])

		types = defaultdict(list)
		for field in all_fields:
			types[field.ttype].extend(field_to_csv_map[field.name])
		return types

	def process_supplier(self, csv_reader, field_names):
		good_rows_data = StringIO()
		bad_rows_data = StringIO()
		# for field_map in self.external_id_map.filtered(lambda x: x.import_model_name.id == self.import_model_name.id):
		# 	field_names.append(f'{field_map.field_name}/dbid')

		# good csv rows writer
		good_csv_writer = csv.DictWriter(good_rows_data, fieldnames=field_names)
		good_csv_writer.writeheader()
		# bad csv rows writer
		bad_csv_writer = csv.DictWriter(bad_rows_data, fieldnames=field_names)
		bad_csv_writer.writeheader()

		all_types = self.get_fields_list(field_names)

		filtered_map = self.external_id_map.filtered(lambda x: x.import_model_name.id == self.import_model_name.id)
		# if the csv has one2many or many2many, then we have to backtrack for the rows so that if last one2many record is
		# bad it means the parent record is bad too
		if all_types.get('one2many') or all_types.get('many2many'):
			# a var for flagging that its a new record, for one2many
			is_a_new_record = False
			bad_row = False
			bad_rows = []
			good_rows = []

			other_type_fields = []
			for field_type in all_types:
				if field_type not in ['one2many','many2many']:
					other_type_fields.extend(all_types[field_type])
			i = 0
			for row in csv_reader:
				if 'one2many' in all_types or 'many2many' in all_types:
					is_a_new_record = False
					# if any column beside the one2many/many2many then we will consider as new record
					if any([row[field] for field in other_type_fields]):
						is_a_new_record = True

				if is_a_new_record:
					if good_rows:
						for g_row in good_rows:
							good_csv_writer.writerow(g_row)
					if bad_rows:
						for b_row in bad_rows:
							bad_csv_writer.writerow(b_row)
					good_rows = []
					bad_rows = []
					is_a_new_record = False
					bad_row = False

				# check if partner exists in this system, if do find its external_id and add it and write to another csv
				if not bad_row:
					for field_map in filtered_map:
						if row and row[field_map.field_name]:
							if row[field_map.field_name].startswith('__export__.') or row[field_map.field_name].startswith('__import__.'):
								continue
						external_id, existing_record_id = self.find_record_external_id(row, field_map)
						if external_id and existing_record_id and external_id == -1 and existing_record_id == -1:
							continue

						if external_id and existing_record_id and external_id !=-1 and existing_record_id != -1:
							row[field_map.field_name] = external_id
							# row[f'{field_map.field_name}/dbid'] = existing_record_id
						else:
							bad_row = True
							bad_rows.append(row)
							break
				else:
					bad_rows.append(row)

				_logger.info(f'Processing {i} row')
				i=i+1
				# if any column external is not found then just put that whole row in the bad csv
				if bad_row:
					if good_rows:
						bad_rows.extend(good_rows)
						good_rows = []
				else:
					# if not bad row put it in good row
					good_rows.append(row)
			if bad_rows:
				bad_rows.extend(good_rows)
				for b_row in bad_rows:
					bad_csv_writer.writerow(b_row)
			else:
				if good_rows:
					for g_row in good_rows:
						good_csv_writer.writerow(g_row)

		else:
			bad_row = False
			i = 0
			for row in csv_reader:
				temp_row = row.copy()
				# check if partner exists in this system, if do find its external_id and add it and write to another csv
				for field_map in filtered_map:
					if row and row[field_map.field_name]:
						if row[field_map.field_name].startswith('__export__.') or row[field_map.field_name].startswith('__import__.'):
							continue

					external_id, existing_record_id = self.find_record_external_id(row, field_map)
					if external_id == -1 and existing_record_id == -1:
						continue
					if external_id and existing_record_id:
						row[field_map.field_name] = external_id
						# row[f'{field_map.field_name}/dbid'] = existing_record_id
					else:
						bad_row = True
						break

				# if any column external is not found then just put that whole row in the bad csv
				if bad_row:
					# its a bad row. write this bad row to the file
					bad_csv_writer.writerow(temp_row)
					bad_row = False
				else:
					# if not bad row put it in good row
					good_csv_writer.writerow(row)

				_logger.info(f'Processing {i} row')
				i = i + 1

		good_data = good_rows_data.getvalue()
		bad_data = bad_rows_data.getvalue()
		# write data to a attachment
		self.create_new_csv(good_data, f'{self.csv_file[0].name}_processed_good.csv')
		self.create_new_csv(bad_data, f'{self.csv_file[0].name}_processed_bad.csv')

	def create_new_csv(self, write_data, filename):
		base64_write_data = base64.encodebytes(write_data.encode('utf-8'))
		res = self.env['ir.attachment'].create({'name': filename,
		                                        'datas': base64_write_data,
		                                        'res_model': 'process.sage.data.csv'
		                                        })
		if res:
			self.processed_file = [(4,res.id)]
			print('File created')

	def find_record_external_id(self, row, field_map):
		external_id = False
		record_id = False

		if row and row[field_map.field_name]:
			domain = eval(field_map.domain)
			record = self.env[field_map.related_model.model].search(domain, limit=1)
			if record:
				external_id = record.get_external_id()[record.id]
				record_id = record.id
				# most of the times you won't get external id from above method because it works only if the id
				# exist in ir.model.data so to ensure it we have to use _export_rows ()
				if not external_id:
					external_id = record._export_rows(fields=[['id']])
					if external_id:
						external_id = external_id[0][0]

		else:
			return -1, -1
		return external_id,record_id


class GetExternalIdMap(models.Model):
	_name = 'field.name.map.external.id'
	_description = 'Search domains to find external id'

	field_name = fields.Char('CSV Field name')
	related_model = fields.Many2one('ir.model',string='rel model')
	domain = fields.Text('Search domain, use row["field_name"] syntax to use')
	rel_process_id = fields.Many2one('process.sage.data.csv')
	for_current_file = fields.Boolean('For Current File',help="Check this if this is related to current file")
	import_model_name = fields.Many2one('ir.model', string='For model')