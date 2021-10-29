odoo.define('business_rule_action.action_for_calendar_view', function (require) {
"use strict";


var calendar = require('web.CalendarRenderer');
var rpc = require('web.rpc');

calendar.include({

    _onEditEvent: function (event) {
        this._unselectEvent();
        var id = event.data.id && parseInt(event.data.id).toString() === event.data.id ? parseInt(event.data.id) : event.data.id;
        var self = this;
        var modelName = this.getParent().modelName;
        self.cal_event = event;

        if (id) {
            return rpc.query({
                model: 'config.open.view',
                method: "get_record_according_to_domain",
                args: ['', modelName,[id]],
            }).then(function (result) {
                if(result.length > 1) {
                    var match = result.filter((x) => { return x['res_ids'].includes(id)});
                    if(match && match.length){
                        return self.do_action({
                            type: "ir.actions.act_window",
                            res_model: match[0]['model'],
                            res_id: id,
                            context:match[0]['context'],
                            views: [[match[0]['view_id'], 'form']],
                            target: "current",
                        });
                    } else {
                        self._super.apply(this, arguments);
                    }
                } else {
                    self._super.apply(this, arguments);
                }
            })
        } else {
            self._super.apply(this, arguments);
        }
    },
})
});