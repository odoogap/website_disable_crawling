# -*- coding: utf-8 -*-
from odoo import models, fields


class Website(models.Model):
    _inherit = 'website'

    disable_crawling = fields.Boolean(string='Disable Crawling', default=False)
