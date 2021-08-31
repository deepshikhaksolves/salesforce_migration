odoo.define('business_rule_action.action_for_list_view', function (require) {
"use strict";

var ListRenderer = require('web.ListRenderer');
var rpc = require('web.rpc');

ListRenderer.include({

    willStart: function () {
        var self = this;
        var defs = [this._super.apply(this, arguments)];
        var modelName = self.getParent().modelName;

        defs.push(rpc.query({
                model: 'config.open.view',
                method: "get_record_according_to_domain",
                args: ['', modelName],
            }).then(function (result) {
                self.business_rule_action = result;
            }))
        return Promise.all(defs);
    },

    _onRowClicked: function (ev) {
        // The special_click property explicitely allow events to bubble all
        // the way up to bootstrap's level rather than being stopped earlier.
        if (!ev.target.closest('.o_list_record_selector') && !$(ev.target).prop('special_click')) {
            var id = $(ev.currentTarget).data('id');

            if (id) {
                if (this.business_rule_action) {
                    if(this.getParent() && this.getParent().model && typeof(this.getParent().model)!=="string") {
                        var record = this.getParent().model.get(id, {raw: true});
                        var match = this.business_rule_action.filter((x) => { return x['res_ids'].includes(record.res_id)});
                        if(match && match.length){
                            return this.do_action({
                                type: "ir.actions.act_window",
                                res_model: match[0]['model'],
                                res_id: record.res_id,
                                context:match[0]['context'],
                                views: [[match[0]['view_id'], 'form']],
                                target: "current",
                            });
                        } else{
                            this.trigger_up('open_record', { id: id, target: ev.target });
                        }
                    } else {
                        this.trigger_up('open_record', { id: id, target: ev.target });
                    }
                } else {
                    this.trigger_up('open_record', { id: id, target: ev.target });
                }

            }
        }
    },
})
});