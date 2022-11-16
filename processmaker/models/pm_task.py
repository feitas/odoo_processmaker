# -*- coding: utf-8 -*-
# Copyright 2022-2023 Feitas (https://www.wffeitas.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
import json
import logging


from odoo import models, fields, api
from odoo.tools.translate import _
from odoo.exceptions import ValidationError, UserError

from .process import TimeConverterDate

_logger = logging.getLogger(__name__)


class PmTask(models.Model):
    _name = 'pm.task'
    _description = 'Pm Task'

    name = fields.Char()
    pm_task_id = fields.Char('Activity Id')
    pm_del_index = fields.Integer('Del Index')
    process_id = fields.Many2one(
        'pm.process', string='Process', ondelete='SET NULL')
