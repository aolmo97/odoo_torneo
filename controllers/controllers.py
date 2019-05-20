# -*- coding: utf-8 -*-
from odoo import http

# class Torneo(http.Controller):
#     @http.route('/torneo/torneo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/torneo/torneo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('torneo.listing', {
#             'root': '/torneo/torneo',
#             'objects': http.request.env['torneo.torneo'].search([]),
#         })

#     @http.route('/torneo/torneo/objects/<model("torneo.torneo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('torneo.object', {
#             'object': obj
#         })