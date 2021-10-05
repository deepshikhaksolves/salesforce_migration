odoo.define('business_rule_views.buisness_rule_view.js', function(require) {
    'use strict';

    var ListController = require('web.ListController')

    ListController.include({
        _onCreateRecord: function(ev) {
            // we prevent the event propagation because we don't want this event to
            // trigger a click on the main bus, which would be then caught by the
            // list editable renderer and would unselect the newly created row

            var self = this
            this._rpc({
                model: 'buisness.rule.view',
                method: "get_buisness_action",
                args: ['', this.modelName],
            }).then((result)=>{
                self.do_action(result);
            }
            );

            //        if (ev) {
            //            ev.stopPropagation();
            //        }
            //        var state = this.model.get(this.handle, {raw: true});
            //        if (this.editable && !state.groupedBy.length) {
            //            this._addRecord(this.handle);
            //        } else {
            //            this.trigger_up('switch_view', {view_type: 'form', res_id: undefined});
            //        }
        },
    });
    return ListController
});
