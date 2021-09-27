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
    _name = 'res.users'
    _inherit = ['res.users', 'mail.thread', 'mail.activity.mixin']
    _description = 'salesforce users'

    about_me = fields.Char(string="About Me", size=1000,track_visibility='onchange')
    # isactive field aready present in odoo
    street = fields.Char(track_visibility='onchange')
    street2 = fields.Char(track_visibility='onchange')
    zip = fields.Char(change_default=True,track_visibility='onchange')
    city = fields.Char(track_visibility='onchange')
    state_id = fields.Many2one("res.country.state", string='State', ondelete='restrict',
                               domain="[('country_id', '=?', country_id)]",track_visibility='onchange')
    country_id = fields.Many2one('res.country', string='Country', ondelete='restrict',track_visibility='onchange')
    partner_latitude = fields.Float(string='Geo Latitude', digits=(16, 5),track_visibility='onchange')
    partner_longitude = fields.Float(string='Geo Longitude', digits=(16, 5),track_visibility='onchange')
    ReceivesAdminInfoEmails = fields.Boolean(string="Admin Info Emails",track_visibility='onchange')
    alias = fields.Text(string="Alias",track_visibility='onchange')
    forecast_enabled = fields.Boolean(string="Allow Forecasting",track_visibility='onchange')
    # banner photo is already present in odoo
    CallCenterId = fields.Many2one('model_call_center', string="Call Center",track_visibility='onchange')
    CEO__c = fields.Char('CEO',track_visibility='onchange')
    DigestFrequency = fields.Selection([('1', '1')], 'Chatter Email Highlights Frequency',track_visibility='onchange')
    # CompanyName already present in odoo
    ContactId = fields.Many2one('res.partner', string='Contact',track_visibility='onchange')
    customer__c = fields.Selection([('Savoy', 'Savoy')], 'Customer',track_visibility='onchange')
    DefaultGroupNotificationFrequency = fields.Selection([('1', '1')],
                                                         'Default Notification Frequency when Joining Groups',track_visibility='onchange')
    DelegatedApproverId = fields.Many2one('res.users', string='Delegated Approver',track_visibility='onchange')
    Department = fields.Many2one('hr.department', string='Department',track_visibility='onchange')
    diretor_comercial__c = fields.Many2one('res.users', string='Diretor Comercial',track_visibility='onchange')
    Division = fields.Many2one('hr.department', string='Division',track_visibility='onchange')
    EmailEncodingKey = fields.Selection([('1', '1')], 'Email Encoding',track_visibility='onchange')
    # SenderEmail = fields.Char('Email Sender Address') already in odoo i.e (login)
    # SenderName = fields.Char('Email Sender Name',size=80) already in odoo i.e (name)
    # Signature = Already present in odoo
    EndDay = fields.Selection([('1', '1'), ('2', '2')], 'End of Day',track_visibility='onchange')
    Extension = fields.Char('Extension',track_visibility='onchange')
    Fax = fields.Char('Fax',track_visibility='onchange')
    IsProfilePhotoActive = fields.Boolean('Has Profile Photo',track_visibility='onchange')
    WorkspaceId = fields.Many2one('model_workspace', string='IDE Workspace',track_visibility='onchange')
    IndividualId = fields.Many2one('res.users', string='Individual',track_visibility='onchange')
    ReceivesInfoEmails = fields.Boolean('Info Emails',track_visibility='onchange')
    UserSubtype = fields.Selection([('1', '1')], 'Internal Subtype',track_visibility='onchange')
    IsSystemControlled = fields.Boolean('Is Controlled By System',track_visibility='onchange')
    IsPortalEnabled = fields.Boolean('Is Portal Enabled',track_visibility='onchange')
    LanguageLocaleKey = fields.Selection([('1', '1')], 'Language',track_visibility='onchange')
    LocaleSidKey = fields.Selection([('1', '1')], 'Locale',track_visibility='onchange')
    ManagerId = fields.Many2one('res.users', string='Manager',track_visibility='onchange')
    MobilePhone = fields.Char('Mobile',track_visibility='onchange')
    # Name = already present in odoo
    CommunityNickname = fields.Char('Nickname', size=40,track_visibility='onchange')
    OutOfOfficeMessage = fields.Char('Out of office message', size=40,track_visibility='onchange')
    PasswordResetAttempt = fields.Integer('Password Reset Attempt',track_visibility='onchange')
    PasswordResetLockoutDate = fields.Date('Password Reset Lockout Date',track_visibility='onchange')
    Phone = fields.Char('Phone',track_visibility='onchange')
    PortalRole = fields.Selection([('1', '1'), ('2', '2')], 'Portal Role Level',track_visibility='onchange')
    ProfileId = fields.Many2one('Profile',track_visibility='onchange')
    reservations_to_vencer__c = fields.Char('reserves to expire', size=32768,track_visibility='onchange')
    UserRoleId = fields.Many2one('res.users', string='Role',track_visibility='onchange')
    FederationIdentifier = fields.Char('SAML Federation ID', size=512,track_visibility='onchange')
    IsExtIndicatorVisible = fields.Boolean('Show external indicator',track_visibility='onchange')
    StartDay = fields.Selection([('1', '1'), ('2', '2')], 'Start of Day',track_visibility='onchange')
    StayInTouchNote = fields.Char('Stay-in-Touch Email Note', size=512,track_visibility='onchange')
    StayInTouchSignature = fields.Char('Stay-in-Touch Email Signature', size=512,track_visibility='onchange')
    StayInTouchSubject = fields.Char('Stay-in-Touch Email Subject', size=512,track_visibility='onchange')
    heads__c = fields.Text('test',track_visibility='onchange')
    TimeZoneSidKey = fields.Selection([('1', '1'), ('2', '2')], 'Time Zone',track_visibility='onchange')
    Title = fields.Char('Title', size=80,track_visibility='onchange')
    MediumBannerPhotoUrl = fields.Char('Url for Android banner photo',track_visibility='onchange')
    BannerPhotoUrl = fields.Char('Url for banner photo',track_visibility='onchange')
    SmallBannerPhotoUrl = fields.Char('Url for IOS banner photo',track_visibility='onchange')
    MediumPhotoUrl = fields.Char('Url for medium profile photo',track_visibility='onchange')
    # Username    = Already present in odoo
    Working_Capacity__c = fields.Integer('Working Capacity',track_visibility='onchange')
