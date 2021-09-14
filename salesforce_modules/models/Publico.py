from odoo import models, fields, api


class Publico(models.Model):
    _name = 'model_publico'
    _description = 'Salesforce Publico'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'Name'

    Contract_id = fields.Many2one('hr.contract', string="Contract")
    Brokerage_id = fields.Many2one('broker', string="Broker")
    # CreatedById already in odoo
    Name = fields.Char(string="Code")
    FDescription = fields.Char(string="Description")
    Entity_Name = fields.Char(string="Entity Name")
    Entity_Type = fields.Selection([
        ('Contract','Contract'),
        ('Financial_Group','Financial Group'),
        ('Carrier','Operator'),
        ('Broker','Broker')
    ],string="Entity Type")
    Full_Description = fields.Char(string="Full Description")
    # Financial_Group_id = fields.Many2one('Financial Group',string="Financial Group")#Financial Group Model not found
    # LastModifiedById already in odoo
    carrier_id = fields.Many2one('account.account', string="Operator")
    OwnerId = fields.Many2one('res.users', string="Owner")
    Related_Entity_Id = fields.Char(string="Related Entity Id", size=100)
    FRelated_Entity_Id = fields.Char(string="Related Entity Id")
    Type = fields.Selection([
        ('Contract','Contract'),
        ('Broker','Broker'),
        ('Financial Group','Financial Group')
    ],string="Type")
