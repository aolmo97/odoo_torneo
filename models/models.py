# -*- coding: utf-8 -*-

from odoo import models, fields, api

class torneo(models.Model):
    _name = 'torneo.torneo'
    _rec_name= 'nombre_torneo'
    nombre_torneo = fields.Char(string="Nombre del torneo",required=True)
    categoria = fields.Selection([("Primera","Primera"),("Segunda","Segunda")],required=True)
    superficie = fields.Selection([("100m","100m"),("400m","400m")],required=True)
    fecha=fields.Date(string="Fecha",required=True)
    
