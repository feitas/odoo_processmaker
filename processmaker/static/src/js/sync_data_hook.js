/** @odoo-module **/

import { useService } from "@web/core/utils/hooks";

const { onWillStart, useComponent } = owl;

export function useSyncDataButton() {
    const component = useComponent();
    const user = useService("user");
    const action = useService("action");
    const pm_orm = useService("orm");

    onWillStart(async () => {
        component.isBpmManager = await user.hasGroup("processmaker.group_bpm_manager");
    });

    component.onClickSyncData = async () => {
        const sync_data_action = await pm_orm.call("pm.process", "update_processes");
        console.log(sync_data_action);
        if (sync_data_action === true) {
            await action.doAction({
                'type': 'ir.actions.client',
                'tag': 'reload',
            });
        }
    };
}