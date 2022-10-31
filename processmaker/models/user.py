import logging

from odoo import models, fields, api
from odoo.exceptions import ValidationError


_logger = logging.getLogger(__name__)

class ResUsersExt(models.Model):
    _inherit = 'res.users'

    pm_user_id = fields.Integer('PM User ID')

    def upload_to_pm(self):
        print(self.env['pm.process']._call('users'))