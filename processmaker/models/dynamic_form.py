from odoo import models, fields, api
from odoo.tools.translate import _
import time
from odoo.exceptions import ValidationError

import logging

_logger = logging.getLogger(__name__)


class DynamicForm(models.Model):
    _name = 'pm.dynamic_form'
    _description = 'Dynamic Form'

    name = fields.Char('Name', required=True)
    process_id = fields.Many2one(
        'pm.process', string='Process', required=True)

    # For Process Maker
    dynamic_form_items = fields.One2many(
        'pm.dynamic_form_item', 'dynamic_form_id')
    pm_screen_id = fields.Char('PM Screen Id')
    pm_screen_name = fields.Char('PM Screen Name')
    pm_screen_label = fields.Char('PM Screen Label')
    pm_screen_type = fields.Char('PM Screen Type')


class DynamicFormItems(models.Model):
    _name = 'pm.dynamic_form_item'
    _description = 'Dynamic Form Item'

    name = fields.Char('Name')
    dynamic_form_id = fields.Many2one(
        'pm.dynamic_form', string='Dynamic Form')
    pm_screen_item_name = fields.Char('PM Screen Item Name')
    pm_screen_item_label = fields.Char('PM Screen Item Label')
    pm_screen_item_type = fields.Char('PM Screen Item Type')
