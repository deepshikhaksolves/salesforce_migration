odoo.define('business_rule_views.business_controllers.js', function(require) {
    'use strict';

    var KanbanController = require('web.KanbanController');

    KanbanController.include({
        _onButtonNew: function(ev) {
            // we prevent the event propagation because we don't want this event to
            // trigger a click on the main bus, which would be then caught by the
            // list editable renderer and would unselect the newly created row
            var self = this;
            var super_method = self._super;
            if ($(ev.currentTarget).hasClass('o-kanban-button-new')){
                this._rpc({
                model: 'buisness.rule.view',
                method: "get_buisness_action",
                args: ['', this.modelName],
            }).then((result)=>{
                if(result){
                     var state = this.model.get(this.handle, {raw: true});
                if (this.renderer.business_rule_action.length > 0 && this.renderer.business_rule_action[0].show_popup && !(this.editable && !state.groupedBy.length)){
                    self.do_action(result);
                }else{
                    super_method.apply(self,arguments);
                }
                } else {
                  super_method.apply(self,arguments);
                }

            }
            );
            } else {
                super_method.apply(self,arguments);
            }
        },
    });
    return KanbanController
  });