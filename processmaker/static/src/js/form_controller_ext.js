/** @odoo-module */

import { FormController } from '@web/views/form/form_controller';
import { formView } from '@web/views/form/form_view';
import { useModel } from "@web/views/model";
import { useService } from "@web/core/utils/hooks";


export class PMFormController extends FormController {
    /**
     * @override
     */
    getActionMenuItems() {
        const otherActionItems = [];
        if (this.archiveEnabled) {
            if (this.model.root.isActive) {
                otherActionItems.push({
                    key: "archive",
                    description: this.env._t("Archive"),
                    callback: () => {
                        const dialogProps = {
                            body: this.env._t(
                                "Are you sure that you want to archive all this record?"
                            ),
                            confirm: () => this.model.root.archive(),
                            cancel: () => { },
                        };
                        this.dialogService.add(ConfirmationDialog, dialogProps);
                    },
                });
            } else {
                otherActionItems.push({
                    key: "unarchive",
                    description: this.env._t("Unarchive"),
                    callback: () => this.model.root.unarchive(),
                });
            }
        }
        if (this.archInfo.activeActions.create && this.archInfo.activeActions.duplicate) {
            otherActionItems.push({
                key: "duplicate",
                description: this.env._t("Duplicate"),
                callback: () => this.duplicateRecord(),
            });
        }
        if (this.archInfo.activeActions.delete && !this.model.root.isVirtual) {
            otherActionItems.push({
                key: "delete",
                description: this.env._t("Delete"),
                callback: () => this.deleteRecord(),
                skipSave: true,
            });
        }
        otherActionItems.push({
            description: this.env._t("Create Resquest"),
            callback: () => this._onCreateResquest(this.model),
        });
        return Object.assign({}, this.props.info.actionMenus, { other: otherActionItems });
    }
    /**
     * Called when the user clicks on 'Create Request' in the action menus
     *
     * @overwrite
     * @private
     */
    async _onCreateResquest() {
        let resId = this.model.__bm_load_params__.res_id;
        let modelName = this.model.__bm_load_params__.modelName;
        await this.model.orm.call("pm.process", "action_create_new_request", [resId, modelName]).then((res) => {
            if (res.error) {
                alert(res["message"]);
            } else {
                location.reload();
            }
        }).catch(() => {
            throw Error("Ops, something wrong.....");
        });
    }
}
formView.Controller = PMFormController;
