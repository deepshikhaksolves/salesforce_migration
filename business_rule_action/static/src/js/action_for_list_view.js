odoo.define('business_rule_action.action_for_list_view', function (require) {
"use strict";

var ListRenderer = require('web.ListRenderer');
var rpc = require('web.rpc');

ListRenderer.include({

    _onRowClicked: function (ev) {
        // The special_click property explicitely allow events to bubble all
        // the way up to bootstrap's level rather than being stopped earlier.
        if (!ev.target.closest('.o_list_record_selector') && !$(ev.target).prop('special_click')) {
            var id = $(ev.currentTarget).data('id');

            if (id) {
                if (this.business_rule_action && this.business_rule_action.length>1) {
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
                        } else {
                            this._super.apply(this, arguments);
                        }
                    } else {
                        this._super.apply(this, arguments);
                    }
                } else {
                    this._super.apply(this, arguments);
                }

            }
        }
    },
})
});