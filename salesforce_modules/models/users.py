# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CallCenter(models.Model):
    _name = 'model_call_center'
    _description = "Salesforce Call Center"

    name = fields.Char('Name')

class WorkspaceId(models.Model):
    _name = 'model_workspace'
    _description = "Salesforce Workspace"

    name = fields.Char('Name')

# class Indivisual(models.Model):
#     _name = 'model_indivisual'
#     _description = "Salesforce Indivisual Id"

#     name = fields.Char('Name')

class salesforce_user(models.Model):
    _inherit = 'res.users'
    _description = 'salesforce users'

    about_me = fields.Char(string = "About Me", size=1000)
    # isactive field aready present in odoo
    street = fields.Char()
    street2 = fields.Char()
    zip = fields.Char(change_default=True)
    city = fields.Char()
    state_id = fields.Many2one("res.country.state", string='State', ondelete='restrict',
                               domain="[('country_id', '=?', country_id)]")
    country_id = fields.Many2one('res.country', string='Country', ondelete='restrict')
    partner_latitude = fields.Float(string='Geo Latitude', digits=(16, 5))
    partner_longitude = fields.Float(string='Geo Longitude', digits=(16, 5))
    ReceivesAdminInfoEmails = fields.Boolean(string="Admin Info Emails")
    alias = fields.Text(string="Alias")
    forecast_enabled = fields.Boolean(string="Allow Forecasting")
    # banner photo is already present in odoo
    CallCenterId  = fields.Many2one('model_call_center',string="Call Center")
    CEO__c = fields.Char('CEO')
    DigestFrequency = fields.Selection([('1', '1')],'Chatter Email Highlights Frequency')
    # CompanyName already present in odoo
    ContactId = fields.Many2one('res.partner',string='Contact')
    customer__c = fields.Selection([('Savoy', 'Savoy')], 'Customer')
    DefaultGroupNotificationFrequency = fields.Selection([('1', '1')],'Default Notification Frequency when Joining Groups')
    DelegatedApproverId = fields.Many2one('res.users',string='Delegated Approver')
    Department = fields.Many2one('hr.department',string='Department')
    diretor_comercial__c = fields.Many2one('res.users',string='Diretor Comercial')
    Division = fields.Many2one('hr.department',string='Division')
    EmailEncodingKey = fields.Selection([('1', '1')],'Email Encoding')
    # SenderEmail = fields.Char('Email Sender Address') already in odoo i.e (login)
    # SenderName = fields.Char('Email Sender Name',size=80) already in odoo i.e (name)
    # Signature = Already present in odoo
    EndDay = fields.Selection([('1', '1'),('2', '2')], 'End of Day')
    Extension = fields.Char('Extension')
    Fax = fields.Char('Fax')
    IsProfilePhotoActive = fields.Boolean('Has Profile Photo')
    WorkspaceId = fields.Many2one('model_workspace',string='IDE Workspace')
    IndividualId = fields.Many2one('res.users',string='Individual')
    ReceivesInfoEmails = fields.Boolean('Info Emails')
    UserSubtype = fields.Selection([('1', '1')],'Internal Subtype')
    IsSystemControlled = fields.Boolean('Is Controlled By System')
    IsPortalEnabled = fields.Boolean('Is Portal Enabled')
    LanguageLocaleKey = fields.Selection([('1', '1')],'Language')
    LocaleSidKey = fields.Selection([('1', '1')],'Locale')
    ManagerId = fields.Many2one('res.users',string='Manager')
    MobilePhone = fields.Char('Mobile')
    # Name = already present in odoo
    CommunityNickname = fields.Char('Nickname',size=40)
    OutOfOfficeMessage = fields.Char('Out of office message',size=40)
    PasswordResetAttempt = fields.Integer('Password Reset Attempt')
    PasswordResetLockoutDate = fields.Date('Password Reset Lockout Date')
    Phone   = fields.Char('Phone')
    PortalRole  = fields.Selection([('1', '1'),('2', '2')], 'Portal Role Level')
    ProfileId   = fields.Many2one('Profile')
    reservations_to_vencer__c   = fields.Char('reserves to expire',size=32768)
    UserRoleId  = fields.Many2one('res.users',string='Role')
    FederationIdentifier    = fields.Char('SAML Federation ID',size=512)
    IsExtIndicatorVisible   = fields.Boolean('Show external indicator')
    StartDay    = fields.Selection([('1', '1'),('2', '2')], 'Start of Day')
    StayInTouchNote = fields.Char('Stay-in-Touch Email Note',size=512)
    StayInTouchSignature = fields.Char('Stay-in-Touch Email Signature',size=512)
    StayInTouchSubject  = fields.Char('Stay-in-Touch Email Subject',size=512)
    heads__c    = fields.Text('test')
    TimeZoneSidKey  = fields.Selection([('1', '1'),('2', '2')], 'Time Zone')
    Title   = fields.Char('Title',size=80)
    MediumBannerPhotoUrl    = fields.Char('Url for Android banner photo')
    BannerPhotoUrl    = fields.Char('Url for banner photo')
    SmallBannerPhotoUrl    = fields.Char('Url for IOS banner photo')
    MediumPhotoUrl    = fields.Char('Url for medium profile photo')
    # Username    = Already present in odoo
    Working_Capacity__c = fields.Integer('Working Capacity')

