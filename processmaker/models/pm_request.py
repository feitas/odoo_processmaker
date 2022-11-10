# -*- coding: utf-8 -*-
# Copyright 2018-2019 SayDigital (https://www.saydigital.it)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

import time

from odoo import models, fields, api
from odoo.tools.translate import _
from odoo.exceptions import ValidationError


class PmRequest(models.Model):
    _name = 'pm.request'
    _description = 'Pm Request'

    name = fields.Char()
    pm_callable_id = fields.Char(string='Process Maker Node Identifier ID')
    pm_activity_id = fields.Char(
        string='Process Maker Request ID', required=False)
    pm_user = fields.Char(string="Process Maker User ID")
    related_model = fields.Char(string='Related Model')
    related_id = fields.Char(string='Related Record ID')
    status = fields.Selection([('ACTIVE', 'IN PROGRESS'), ('ERROR', 'ERROR'), (
        'CANCELED', 'CANCELED'), ('COMPLETED', 'COMPLETED')], string='Status', default='ACTIVE')

    def start_activity(self):
        pass
