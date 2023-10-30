# -*- coding: utf-8 -*-
"""
Odoo Proprietary License v1.0.

see License:
https://www.odoo.com/documentation/user/16.0/legal/licenses/licenses.html#odoo-apps
# Copyright ©2023 Bernard K. Too<bernard.too@optima.co.ke>
"""
from odoo import fields, models


class ReportConfigSettings(models.TransientModel):
    _inherit = ["res.config.settings"]

    df_style = fields.Many2one(related="company_id.df_style", readonly=False)
