from odoo import models, fields


# Modelo Inscripción
class Inscripcion(models.Model):
    _name = 'gestion.alumnos.inscripcion'
    _description = 'inscripcion model'

    alumno_id = fields.Many2one('gestion.alumnos.alumno', "Alumno", required=True)
    programa_id = fields.Many2one('gestion.alumnos.programa', "Programa", required=True)
    fecha_inscripcion = fields.Date("Fecha de inscripcion", default=fields.Date.today)
    
