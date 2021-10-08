odoo.define('business_rule_views.business_rule_save.js', function(require) {
    'use strict';

    var FormController = require('web.FormController');
    var core = require('web.core');
    var _t = core._t;
    var Domain = require('web.Domain');

    FormController.include({
         _onSave: function (ev) {
            ev.stopPropagation();
            if (this.model.loadParams.context.business_rule_domain){
                 var element = this.model.localData[this.handle]
                 var business_data = this._businesRuleModifiers(element,this.model.loadParams.context.business_rule_domain)
                 if (business_data){
                    this._disableButtons();
                    this.saveRecord().then(this._enableButtons.bind(this)).guardedCatch(this._enableButtons.bind(this));
                } else {
                    this.do_warn("Values doesn't match with domain defined in business rule" + String(this.model.loadParams.context.business_rule_domain))
                }
            } else {
                this._super.apply(this, arguments);
            }

    },

        _onCreate: function(ev) {
            // we prevent the event propagation because we don't want this event to
            // trigger a click on the main bus, which would be then caught by the
            // list editable renderer and would unselect the newly created row
            var self = this;
            var super_method = self._super;
            if ($(ev.currentTarget).hasClass('o_form_button_create')){
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

        _businesRuleModifiers : function(element,business_domain){
            var evaluated = true;
            const mod = business_domain;
            var evalContext = this.model._getEvalContext(element);
            evaluated = new Domain(mod, evalContext).compute(evalContext);
            return evaluated
        },
        });
    return FormController
});
