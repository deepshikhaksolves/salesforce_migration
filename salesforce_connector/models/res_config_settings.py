# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from simple_salesforce import Salesforce
from odoo.exceptions import Warning, ValidationError
from odoo.osv import osv


class SfResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    sf_username = fields.Char(string='Username', config_parameter='sf_username')
    sf_password = fields.Char(string='Password', config_parameter='sf_password')
    sf_security_token = fields.Char(string='Security Token', config_parameter='sf_security_token')
    sf_organization_id = fields.Char(string='Organization Id', config_parameter='organization_id')
    sf_domain_name = fields.Char(string='Salesforce Login Domain', config_parameter='sf_domain',help = 'e.g; if you are login through login.salesforce.com then enter login here,'
                                                                                'default login domain is login,if your domain have my.salesforce.com domain'
                                                                                ' then enter that or you have sandbox domain with cs47 or na1,enter that here')
    sf_version = fields.Selection([('50.0', '50.0'), ('49.0', '49.0'), ('48.0', '48.0'), ('47.0', '47.0'), ('46.0', '46.0'),('45.0', '45.0'), ('44.0', '44.0'), ('43.0', '43.0'), ('42.0', '42.0'),('41.0', '41.0'), ('40.0', '40.0'), ('others', 'Other')], string='Version',
                                  default = '49.0', config_parameter = 'sf_version')
    version = fields.Char('Salesforce Version', default='49.0', config_parameter='version')

    @api.onchange('sf_version')
    def _onchange_sf_version(self):
        if self.sf_version != 'others':
            self.version = self.sf_version
        else:
            self.version = '' if not self.version else self.version

    def test_credentials(self):
        """
    		        Tests the user SalesForce account credentials
    		        :return: None
    		    """


        try:
             # Salesforce(username=self.sf_username, password=self.sf_password, security_token=self.sf_security_token, version=self.version)
            Salesforce(username=self.sf_username, password = self.sf_password, organizationId = self.sf_organization_id,version = self.version,domain = self.sf_domain_name)
        except Exception as e:
            raise Warning(_(str(e)))


        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {'title': _('Success'),'type': 'success','message': 'Credentials Test Successful','sticky': True}}