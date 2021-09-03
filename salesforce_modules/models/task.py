from odoo import models, fields, api


class ModelTask(models.Model):
    _inherit = 'project.task'
    _description = "Salesforce Task"

    # OwnerId         already in  odoo (user_id)
    CallDurationInSeconds = fields.Integer('Call Duration')
    CallObject      = fields.Char('Call Object Identifier',size=255)
    CallDisposition = fields.Char('Call Result',size=255)
    CallType        = fields.Selection([('1','1'),('2','2')],'Call Type')
    # Description     already in odoo (description)
    CompletedDateTime   = fields.Date('Completed Date')
    # IsRecurrence    already in odoo (recurring_task)
    # CreatedById already present in odoo
    ActivityDate    = fields.Date('Due Date')
    # LastModifiedById already in odoo
    WhoId           = fields.Many2one('res.partner',string='Name')
    Phone           = fields.Char('Phone')
    # Priority       already in odoo (priority)
    IsVisibleInSelfService = fields.Boolean('Public')
    RecurrenceInterval = fields.Integer('Recurrence Interval')
    # WhatId already in odoo (tag_ids)
    IsReminderSet = fields.Boolean('Reminder Set')

    RecurrenceRegeneratedType = fields.Selection([('1','1'),('2','2')],'Repeat This Task')
    Status = fields.Selection([('Open','Open'),('Completed','Finished'),('cancel','Called off')],'Status')
    Subject = fields.Selection([('Call','Call'),('Send Letter','Send Letter'),('Send Quote','Send Quote'),('Prospecting Return','Prospecting Return'),('Other','Other')],'Subject')
    # RecordTypeId already in odoo
    TaskSubtype     = fields.Selection([('1','1'),('2','2')],'Task Subtype')
    Type            = fields.Selection([('Call','Call'),('Meeting','Meeting'),('Other','Other')],'Type')
    Email           = fields.Char('Email') 
    