# -*- coding: utf-8 -*-
from odoo import fields, models, api
from odoo.exceptions import AccessDenied


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    disable_crawling = fields.Boolean(string='Disable Crawling', related='website_id.disable_crawling')

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        get_param = self.env['ir.config_parameter'].sudo().get_param
        res.update(
            disable_crawling=get_param('disable_crawling', default='0'),
        )
        return res

    def set_values(self):
        if not self.user_has_groups('website.group_website_designer'):
            raise AccessDenied()
        super(ResConfigSettings, self).set_values()
        set_param = self.env['ir.config_parameter'].sudo().set_param
        set_param('disable_crawling', self.disable_crawling and '1' or '0')
