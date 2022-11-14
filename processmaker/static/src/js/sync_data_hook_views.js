/** @odoo-module **/

import { registry } from "@web/core/registry";
import { useSyncDataButton } from "@processmaker/js/sync_data_hook";
import { ListController } from "@web/views/list/list_controller";
import { listView } from "@web/views/list/list_view";

export class ProcessMakerListController extends ListController {
    setup() {
        super.setup();
        useSyncDataButton();
    }
}

registry.category("views").add("pm_process_sync_dat_list", {
    ...listView,
    Controller: ProcessMakerListController,
    buttonTemplate: "ProcessMakerListView.buttons",
});

