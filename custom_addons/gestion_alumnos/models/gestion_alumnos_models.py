from odoo import models, fields

# Modelo Alumno
class Alumno(models.Model):
    _name = "gestion.alumnos.alumno"
    _description = "alumno model"

    nombre = fields.Char("Nombre", required=True)
    apellido = fields.Char("Apellido", required=True)
    fecha_de_nacimiento = fields.Date("Fecha de Nacimiento", required=True)
    legajo = fields.Integer("N° de Legajo")
    email = fields.Char("Email")
    telefono = fields.Float("Telefono", size=15, digits=(15, 0))
    direccion = fields.Char("Direccion")
    pais = fields.Char("Pais")

# Modelo Programa
class Programa(models.Model):
    _name = "gestion.alumnos.programa"
    _description = "programa model"

    nombre = fields.Char("Nombre", required=True)
    descripcion = fields.Char("Descripcion", required=True)

# Modelo Inscripción
class Inscripcion(models.Model):
    _name = 'gestion.alumnos.inscripcion'
    _description = 'inscripcion model'

    alumno_id = fields.Many2one('gestion.alumnos.alumno', "Alumno", required=True)
    programa_id = fields.Many2one('gestion.alumnos.programa', "Programa", required=True)
    fecha_inscripcion = fields.Date("Fecha de inscripcion", default=fields.Date.today)