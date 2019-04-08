# -*- coding: utf-8 -*-
import odoo
from odoo import http
from odoo.http import request


class Website(odoo.addons.website.controllers.main.Website):
    @http.route(['/robots.txt'], type='http', auth='public')
    def robots(self):
        # Disable crawling if global configuration is enabled
        if request.env['ir.config_parameter'].sudo().get_param('disable_crawling', '0') == '1':
            return request.render('website_disable_crawling.robots', mimetype='text/plain')

        # Disable crawling if website configuration is enabled
        domain = request and request.httprequest.url_root or self.env['ir.config_parameter'].sudo().get_param(
            'web.base.url')
        if domain[-1] == '/':
            domain = domain[:-1]

        domain = domain.replace('http://', '').replace('https://', '')
        website = request.env['website'].sudo().search([('domain', 'ilike', domain)], limit=1)
        if website and website.disable_crawling:
            return request.render('website_disable_crawling.robots', mimetype='text/plain')

        # Crawl website
        return request.render('website.robots', {'url_root': request.httprequest.url_root}, mimetype='text/plain')
