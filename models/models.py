# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Product(models.Model):
    _name = 'ristorante.product'
    _description = 'Los platos del menú'
    
    name = fields.Char(string="Name", required="True")
    description = fields.Text(string="Description")
    #price = fields.Monetary(string="Price")
    
    #currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id.id)


class Menu(models.Model):
    _name = 'ristorante.menu'
    _description = 'El menu del restaurante'

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
    isVip = fields.Boolean()
    
    #products = fields.One2many(Products, string="Products")
    
    
class Reserva(models.Model):
    _name = 'ristorante.reserva'
    _description = 'La reserva de un cliente'
    
    id = fields.Integer()
    name = fields.Char()
    #cliente = fields.One2one()


class Persona(models.AbstractModel):
    _name = 'ristorante.persona'
    _description = 'Información general de personas'
    
    dni = fields.Char(string="DNI")
    name = fields.Char(string="Name")
    birth_date = fields.Date(string="Date of birth")
    phone = fields.Integer(string="Phone")
    
    
class Client(models.Model, Persona):
    _name = 'ristorante.client'
    _description = 'Clientes del restaurante'
    
    #reservas
    

class Empleado(models.AbstractModel, Persona):
    _name = 'ristorante.empleado'
    _description = 'Empleados del restaurante'
    
    #salary = fields.Monetary(string="Salary")
    

class Cambrer(models.Model, Empleado):
    _name = 'ristorante.cambrer'
    _description = 'Cambrers del restaurant'
    
    #id_ordre = fields.One2Many
    
    
class Ordre(models.Model):
    _name = 'ristorante.ordre'
    _description = 'Ordres dels clients del restaurant'

    id = fields.Integer()
    #taula = fields.One2one()
    #menu = fields.Many2one()
    status = fields.Boolean()
    
    
class Taula(models.Model):
    _name = 'ristorante.taula'
    _description = 'Taules del restaurant'
    
    nom = fields.Char()
    n_seients = fields.Integer()
    isOcupat = fields.Boolean()
    isVip = fields.Boolean()
    isExterior = fields.Boolean()
    #reservada = fields.Boolean()