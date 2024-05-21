from odoo import models, fields

# Modelo Programa
class Programa(models.Model):
    _name = "gestion.alumnos.programa"
    _description = "programa model"

    name = fields.Char("Nombre", required=True)
    descripcion = fields.Char("Descripcion", required=True)
    
    