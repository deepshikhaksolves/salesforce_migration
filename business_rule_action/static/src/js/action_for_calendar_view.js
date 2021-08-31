odoo.define('business_rule_action.action_for_calendar_view', function (require) {
"use strict";


var calendar = require('web.CalendarRenderer');
var rpc = require('web.rpc');

calendar.include({
    willStart: function () {
        var self = this;
        var defs = [this._super.apply(this, arguments)];
        var modelName = self.model;

        defs.push(rpc.query({
                model: 'config.open.view',
                method: "get_record_according_to_domain",
                args: ['', modelName],
            }).then(function (result) {
                self.business_rule_action = result;
            }))
        return Promise.all(defs);
    },

    _onEditEvent: function (event) {
        this._unselectEvent();
        var id = event.data.id && parseInt(event.data.id).toString() === event.data.id ? parseInt(event.data.id) : event.data.id;

        if (this.business_rule_action && id) {
            var match = this.business_rule_action.filter((x) => { return x['res_ids'].includes(id)});
            if(match && match.length){
                return this.do_action({
                    type: "ir.actions.act_window",
                    res_model: match[0]['model'],
                    res_id: id,
                    context:match[0]['context'],
                    views: [[match[0]['view_id'], 'form']],
                    target: "current",
                });
            } else{
                this.trigger_up('openEvent', {
                    _id: event.data.id,
                    title: event.data.title,
                });
            }
        } else {
            this.trigger_up('openEvent', {
                _id: event.data.id,
                title: event.data.title,
            });
        }
    },
})
});