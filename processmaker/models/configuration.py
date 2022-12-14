# -*- coding: utf-8 -*-
# Copyright 2022 Feitas (https://www.wffeitas.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class OdooConfiguration(models.TransientModel):
    _inherit = 'res.config.settings'

    pm_url = fields.Char(string='PM Url', required=False,
                         config_parameter='pm.url')
    pm_workspace = fields.Char(
        string='PM Workspace', required=False, config_parameter='pm.workspace')
    pm_client_id = fields.Char(
        string='PM Client Id', required=False, config_parameter='pm.client')
    pm_client_secret = fields.Char(
        string='PM Client secret', required=False, config_parameter='pm.client.secret')
    pm_username = fields.Char(string='PM Username',
                              required=False, config_parameter='pm.username')
    pm_password = fields.Char(string='PM Password',
                              required=False, config_parameter='pm.password')

    pm_user_name = fields.Char(string='Name of the user of PM', required=False)
    pm_access_token = fields.Char()
