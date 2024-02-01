# -*- coding: utf-8 -*-

from odoo.models import Model, AbstractModel
from odoo.fields import Char, Text, Boolean, Integer, Date, Many2many, Many2one, One2many


class Product(Model):
    _name = 'ristorante.product'
    _description = 'Los platos del menú'
    
    name = Char(string="Nombre", required="True")
    description = Text(string="Descripción")
    #price = fields.Monetary(string="Price")
    
    #currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id.id)


class Menu(Model):
    _name = 'ristorante.menu'
    _description = 'El menu del restaurante'

    name = Char(string="Nombre")
    description = Text(string="Descripción")
    isVip = Boolean()
    products = Many2many('ristorante.product', relation="menu_product_rel", string="Productos")
    
    
class Reserva(Model):
    _name = 'ristorante.reserva'
    _description = 'La reserva de un cliente'
    
    id = Integer()
    name = Char()
    
    client = Many2one('ristorante.client', string="Cliente")


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

class Cuiner(Model, Empleado):
    _name = 'ristorante.cuiner'
    _description  ='Cuiners del restaurant'

    
class Ordre(Model):
    _name = 'ristorante.ordre'
    _description = 'Ordres dels clients del restaurant'

    status = Boolean()

    cuiner = Many2one('ristorante.cuiner', string='Cuiner')
    cambrer = Many2one('ristorante.cambrer', string='Cambrer')
    taula = Many2one('ristorante.taula', string='Taula')

    
    
class Taula(Model):
    _name = 'ristorante.taula'
    _description = 'Taules del restaurant'
    
    nom = Char()
    n_seients = Integer()
    isOcupat = Boolean()
    isVip = Boolean()
    isExterior = Boolean()
    #reservada = fields.Boolean()

    ordres = One2many('ristorante.ordre', 'taula', string="Ordre")