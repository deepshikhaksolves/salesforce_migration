from odoo import models, fields, api

class Condition(models.Model):
    _name = 'condition'

    Conditional = fields.Selection([
        ('User', 'User'), ('Group', 'Group')
    ], string='Conditional')
    name = fields.Char(string='Condition')
    # CreatedById created by default
    # LastModifiedById created by default
    GroupApiName = fields.Char(string='Group Name (apiName)',size=255)
    OwnerId = fields.Many2one('res.users', string='Owner')
    RecordTypeId = fields.Integer(string='Record Type')
    selectedUserListJSON = fields.Text(string='selectedUserListJSON')
    # Transition not clear
    User = fields.Many2one('res.users', string='User')
    Value = fields.Char(string='Value', size=255)
    