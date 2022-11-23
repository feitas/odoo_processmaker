odoo.define('processmaker.DataSync', function (require) {
    "use strict";

    var ListController = require('web.ListController');
    var ListView = require('web.ListView');
    var viewRegistry = require('web.view_registry');

    var ProcessMakerListController = ListController.extend({
        buttons_template: 'ProcessMakerListView.buttons',
        events: _.extend({}, ListController.prototype.events, {
            'click .o_button_pm_sync_data': '_onDataSync',
        }),

        _onDataSync: function (e) {
            var self = this;
            this._rpc({
                model: 'pm.process',
                method: 'update_processes',
            }).then(function () {
                self.trigger_up('reload');
            });
        }
    });

    var ProcessMakerListView = ListView.extend({
        config: _.extend({}, ListView.prototype.config, {
            Controller: ProcessMakerListController,
        }),
    });

    viewRegistry.add('sync_data_tree', ProcessMakerListView);
});
