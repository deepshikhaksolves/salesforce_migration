from odoo import models, fields, api


class Publico(models.Model):
    _name = 'model_publico'
    _description = 'Salesforce Publico'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'Name'

    Contract_id = fields.Many2one('hr.contract', string="Contract",track_visibility='onchange')
    Brokerage_id = fields.Many2one('broker', string="Broker",track_visibility='onchange')
    # CreatedById already in odoo
    Name = fields.Char(string="Code",track_visibility='onchange')
    FDescription = fields.Char(string="Description",track_visibility='onchange')
    Entity_Name = fields.Char(string="Entity Name",track_visibility='onchange')
    Entity_Type = fields.Selection([
        ('Contract','Contract'),
        ('Financial_Group','Financial Group'),
        ('Carrier','Operator'),
        ('Broker','Broker')
    ],string="Entity Type",track_visibility='onchange')
    Full_Description = fields.Char(string="Full Description",track_visibility='onchange')
    Financial_Group_id = fields.Many2one('model_financial_group',string="Financial Group",track_visibility='onchange')
    # LastModifiedById already in odoo
    carrier_id = fields.Many2one('account.account', string="Operator",track_visibility='onchange')
    OwnerId = fields.Many2one('res.users', string="Owner",track_visibility='onchange')
    Related_Entity_Id = fields.Char(string="Related Entity Id", size=100,track_visibility='onchange')
    FRelated_Entity_Id = fields.Char(string="Related Entity Id",track_visibility='onchange')
    Type = fields.Selection([
        ('Contract','Contract'),
        ('Broker','Broker'),
        ('Financial Group','Financial Group')
    ],string="Type",track_visibility='onchange')
