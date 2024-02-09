# -*- coding: utf-8 -*-

from odoo.models import Model, AbstractModel
from odoo.fields import Char, Text, Boolean, Integer, Date, Many2many, Many2one, One2many, Monetary, Selection, Image


class Product(Model):
    _name = 'ristorante.product'
    _description = 'Los platos del menú'
    
    name = Char(string="Nombre", required="True")
    description = Text(string="Descripción")
    price = Integer(string="Price")
    photo = Image(max_width=200, max_height=200)

    
    menus = Many2many('ristorante.menu')


class Menu(Model):
    _name = 'ristorante.menu'
    _description = 'El menu del restaurante'

    name = Char(string="Nombre")
    description = Text(string="Descripción")
    isVip = Boolean()
    products = Many2many('ristorante.product', string="Productos")
    
    
class Reserva(Model):
    _name = 'ristorante.reserva'
    _description = 'La reserva de un cliente'
    
    id = Integer()
    name = Char()
    date = Date()
    
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
    
    reservas = One2many('ristorante.reserva', 'client', string="Reservas")
    


class Empleado(Persona):
    _name = 'ristorante.empleado'
    _description = 'Empleados del restaurante'
    
    salary = Integer(string="Salary")
    

class Cambrer(Model, Empleado):
    _name = 'ristorante.cambrer'
    _description = 'Cambrers del restaurant'
    
    ordres = One2many('ristorante.ordre', 'cambrer', string="Ordres")

class Cuiner(Model, Empleado):
    _name = 'ristorante.cuiner'
    _description  ='Cuiners del restaurant'

    ordres = One2many('ristorante.ordre', 'cuiner', string="Ordres")


class Taula(Model):
    _name = 'ristorante.taula'
    _description = 'Taules del restaurant'
    
    name = Char(string="Nom")
    n_seients = Integer(string="Nº Seients")
    isOcupat = Boolean(string="Ocupat")
    isVip = Boolean(string="VIP")
    isExterior = Boolean(string="Exterior")
    reservada = Boolean(string="Reservada")

    ordres = One2many('ristorante.ordre', 'taula', string="Ordre")


class Ordre(Model):
    _name = 'ristorante.ordre'
    _description = 'Ordres dels clients del restaurant'

    status = Selection([('option1', 'Pedido'), ('option2', 'Haciendo'), ('option3', 'Entregando')], string="Estado")

    cuiner = Many2one('ristorante.cuiner', string='Cuiner')
    cambrer = Many2one('ristorante.cambrer', string='Cambrer')
    taula = Many2one('ristorante.taula', string='Taula')
