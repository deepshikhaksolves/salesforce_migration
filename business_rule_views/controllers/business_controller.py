import json

from odoo import http,_
from odoo.http import request
from odoo.addons.web.controllers.main import DataSet
from odoo.tools.safe_eval import safe_eval
from odoo.osv import expression
from odoo.exceptions import ValidationError


class BusinessController(DataSet, http.Controller):

    @http.route(['/web/dataset/call_kw', '/web/dataset/call_kw/<path:path>'], type='json', auth="user")
    def call_kw(self, model, method, args, kwargs, path=None):
        if (method == "create" or method == 'write') and kwargs.get('context',{}).get('business_rule_domain',False):
            record = request.env[model].create(args)
            busines_domain = kwargs.get('context', {}).get('business_rule_domain', False)
            res = self.is_failing(busines_domain ,record)
            record.unlink()
            if res:
                raise ValidationError(_("Values doesn't match with domain defined in business rule." + str(busines_domain)))
        call_kw_result = super(BusinessController, self).call_kw(model, method, args, kwargs, path)
        return call_kw_result

    def is_failing(self, domain, record):
        dom = domain
        ids = record.ids
        model = record.browse(()).sudo()
        return model.search_count(expression.AND([
            [('id', 'in', ids)],
            expression.normalize_domain(dom)
        ])) < len(ids)