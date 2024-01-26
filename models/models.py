# -*- coding: utf-8 -*-

from odoo.models import Model, AbstractModel
from odoo.fields import Char, Text, Boolean, Integer, Date


class Product(Model):
    _name = 'ristorante.product'
    _description = 'Los platos del menú'
    
    name = Char(string="Name", required="True")
    description = Text(string="Description")
    #price = fields.Monetary(string="Price")
    
    #currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id.id)


class Menu(Model):
    _name = 'ristorante.menu'
    _description = 'El menu del restaurante'

    name = Char(string="Name")
    description = Text(string="Description")
    isVip = Boolean()
    
    #products = fields.One2many(Products, string="Products")
    
    
class Reserva(Model):
    _name = 'ristorante.reserva'
    _description = 'La reserva de un cliente'
    
    id = Integer()
    name = Char()
    #cliente = fields.One2one()


class Persona(AbstractModel):
    _name = 'ristorante.persona'
    _description = 'Información general de personas'
    
    dni = Char(string="DNI")
    name = Char(string="Name")
    birth_date = Date(string="Date of birth")
    phone = Integer(string="Phone")
    
    
class Client(Model, Persona):
    _name = 'ristorante.client'
    _description = 'Clientes del restaurante'
    
    #reservas
    

class Empleado(Persona):
    _name = 'ristorante.empleado'
    _description = 'Empleados del restaurante'
    
    #salary = fields.Monetary(string="Salary")
    

class Cambrer(Model, Empleado):
    _name = 'ristorante.cambrer'
    _description = 'Cambrers del restaurant'
    
    #id_ordre = fields.One2Many
    
    
class Ordre(Model):
    _name = 'ristorante.ordre'
    _description = 'Ordres dels clients del restaurant'

    id = Integer()
    #taula = fields.One2one()
    #menu = fields.Many2one()
    status = Boolean()
    
    
class Taula(Model):
    _name = 'ristorante.taula'
    _description = 'Taules del restaurant'
    
    nom = Char()
    n_seients = Integer()
    isOcupat = Boolean()
    isVip = Boolean()
    isExterior = Boolean()
    #reservada = fields.Boolean()