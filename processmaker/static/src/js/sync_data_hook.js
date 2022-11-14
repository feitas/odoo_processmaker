/** @odoo-module **/

import { useService } from "@web/core/utils/hooks";

const { onWillStart, useComponent, useEnv } = owl;

export function useSyncDataButton(_orm) {
    const component = useComponent();
    const user = useService("user");
    const action = useService("action");
    // const _orm = useService("orm");
    const _rpc = useService('rpc');
    const env = useEnv();


    onWillStart(async () => {
        component.isBpmManager = await user.hasGroup("processmaker.group_bpm_manager");
    });

    component.onClickSyncData = async () => {
        console.log(_orm);
        const context = {};
        const _action = await _orm.call("pm.process", "update_processes", [])
        console.log(_action);
        // const _action = {
        //     name: "Generate Leads",
        //     type: "ir.actions.act_window",
        //     res_model: "pm.process",
        //     target: "new",
        //     views: [[false, "form"]],
        // }
        action.doAction(_action);
        // await _rpc({
        //     model: 'pm.process',
        //     method: 'update_processes',
        //     domain: [['id', 'in', order_server_ids]],
        //     fields: ['name'],
        //     context: session.user_context,
        // });

        // await _rpc(
        //     '/hr/get_subordinates',
        //     {
        //         employee_id: employee_id,
        //         subordinates_type: type,
        //         context: Component.env.session.user_context,
        //     }
        // );
    };
}