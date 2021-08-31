odoo.define('business_rule_action.action_for_kanban_view', function (require) {
"use strict";


var kanban = require('web.KanbanRecord');
var rpc = require('web.rpc');

kanban.include({

    willStart: function () {
        var self = this;
        var defs = [this._super.apply(this, arguments)];
        var modelName = self.modelName;

        defs.push(rpc.query({
                model: 'config.open.view',
                method: "get_record_according_to_domain",
                args: ['', modelName],
            }).then(function (result) {
                self.business_rule_action = result;
            }))
        return Promise.all(defs);
    },

    _openRecord: function () {
        if (this.$el.hasClass('o_currently_dragged')) {
            // this record is currently being dragged and dropped, so we do not
            // want to open it.
            return;
        }
        var editMode = this.$el.hasClass('oe_kanban_global_click_edit');

        if (this.business_rule_action) {
            if(this.getParent() && this.getParent().getParent() && this.getParent().getParent().model && typeof(this.getParent().getParent().model)!=="string") {
                var record = this.getParent().getParent().model.get(this.db_id, {raw: true});
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
                    this.trigger_up('open_record', {
                        id: this.db_id,
                        mode: editMode ? 'edit' : 'readonly',
                    });
                }
            } else {
                this.trigger_up('open_record', {
                    id: this.db_id,
                    mode: editMode ? 'edit' : 'readonly',
                });
            }
        } else {
            this.trigger_up('open_record', {
                id: this.db_id,
                mode: editMode ? 'edit' : 'readonly',
            });
        }

    },

});
});