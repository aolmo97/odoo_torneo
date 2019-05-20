# -*- coding: utf-8 -*-

from odoo import models, fields, api

class torneo(models.Model):
    _name = 'torneo.torneo'
    _rec_name= 'nombre_torneo'
    nombre_torneo = fields.Char(string="Nombre del torneo",required=True)
    categoria = fields.Selection([("Primera","Primera"),("Segunda","Segunda")],required=True)
    superficie = fields.Selection([("100m","100m"),("400m","400m")],required=True)
    fecha=fields.Date(string="Fecha",required=True)
    tenistas=fields.One2many('torneo.tenista','nombre_tenista')
class tenista(models.Model):
    _name = 'torneo.tenista'
    _rec_name= 'nombre_tenista'
    _sql_constraints=[("id_tenista",'UNIQUE(ranking)',"Error ya existe un tenista con ese ranking")]
    nombre_tenista = fields.Char(string="Nombre del tenista",required=True)
    ranking=fields.Integer(string="Numero del ranking",required=True)
    torneos=fields.Many2one('torneo.torneo','nombre_torneo')
    #fecha=fields.Date(string="Fecha",required=True)    

