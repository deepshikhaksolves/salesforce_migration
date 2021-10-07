odoo.define('business_rule_action.action_for_kanban_view', function (require) {
"use strict";


var kanban = require('web.KanbanRecord');
var rpc = require('web.rpc');

kanban.include({

    _openRecord: function () {
        if (this.$el.hasClass('o_currently_dragged')) {
            // this record is currently being dragged and dropped, so we do not
            // want to open it.
            return;
        }
        var editMode = this.$el.hasClass('oe_kanban_global_click_edit');

        if (this.getParent() && this.getParent().business_rule_action.lenght>1) {
            if(this.getParent() && this.getParent().getParent() && this.getParent().getParent().model && typeof(this.getParent().getParent().model)!=="string") {
                var record = this.getParent().getParent().model.get(this.db_id, {raw: true});
                var match = this.getParent().business_rule_action.filter((x) => { return x['res_ids'].includes(record.res_id)});
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