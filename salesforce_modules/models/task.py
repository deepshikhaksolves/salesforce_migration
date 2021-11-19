from odoo import models, fields, api


class ModelTask(models.Model):
    _name = 'project.task'
    _inherit = ['project.task', 'mail.thread', 'mail.activity.mixin']
    _description = "Salesforce Task"

    # OwnerId         already in  odoo (user_id)
    CallDurationInSeconds = fields.Integer('Call Duration',track_visibility='onchange')
    CallObject = fields.Char('Call Object Identifier', size=255,track_visibility='onchange')
    CallDisposition = fields.Char('Call Result', size=255,track_visibility='onchange')
    CallType = fields.Selection([('1', '1'), ('2', '2')], 'Call Type',track_visibility='onchange')
    # Description     already in odoo (description)
    CompletedDateTime = fields.Date('Completed Date',track_visibility='onchange')
    # IsRecurrence    already in odoo (recurring_task)
    # CreatedById already present in odoo
    ActivityDate = fields.Date('Due Date',track_visibility='onchange')
    # LastModifiedById already in odoo
    WhoId = fields.Many2one('res.partner', string='Name',track_visibility='onchange')
    Phone = fields.Char('Phone',track_visibility='onchange')
    # Priority       already in odoo (priority)
    IsVisibleInSelfService = fields.Boolean('Public',track_visibility='onchange')
    RecurrenceInterval = fields.Integer('Recurrence Interval',track_visibility='onchange')
    # WhatId already in odoo (tag_ids)
    IsReminderSet = fields.Boolean('Reminder Set',track_visibility='onchange')

    RecurrenceRegeneratedType = fields.Selection([('1', '1'), ('2', '2')], 'Repeat This Task',track_visibility='onchange')
    Status = fields.Selection([('Open', 'Open'), ('Completed', 'Finished'), ('cancel', 'Called off')], 'Status',track_visibility='onchange')
    Subject = fields.Selection([('Call', 'Call'), ('Send Letter', 'Send Letter'), ('Send Quote', 'Send Quote'),
                                ('Prospecting Return', 'Prospecting Return'), ('Other', 'Other')], 'Subject',track_visibility='onchange')
    # RecordTypeId already in odoo
    TaskSubtype = fields.Selection([('1', '1'), ('2', '2')], 'Task Subtype',track_visibility='onchange')
    Type = fields.Selection([('Call', 'Call'), ('Meeting', 'Meeting'), ('Other', 'Other')], 'Type',track_visibility='onchange')
    Email = fields.Char('Email',track_visibility='onchange')

    attachment_ids = fields.One2many('ir.attachment', 'task_id', string='Task IDS')

