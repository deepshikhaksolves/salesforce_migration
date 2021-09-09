odoo.define('business_rule_action.load_current_data', function (require) {
"use strict";

var BasicRenderer = require('web.BasicRenderer');
var rpc = require('web.rpc');

BasicRenderer.include({

    async _render() {
        var self = this;
        await self._super(...arguments);
        var modelName = self.getParent().modelName;
        var res_ids = this.state.res_ids;
        await rpc.query({
                model: 'config.open.view',
                method: "get_record_according_to_domain",
                args: ['', modelName,res_ids],
            }).then(function (result) {
                self.business_rule_action = result;
            })
    },
})
});