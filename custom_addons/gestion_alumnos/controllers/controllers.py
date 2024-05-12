import json

from odoo import http
from odoo.http import Response, request

class Tracking(http.Controller):
    @http.route('/dataset/<int:programa_id>', type='http', auth="public")
    def tracking(self, programa_id):
        alumnos_inscritos = []

        # Buscar inscripciones para el programa especificado
        inscripciones = self.env['gestion.alumnos.inscripcion'].search([
            ('programa_id', '=', programa_id)
        ])

        # Recorrer las inscripciones y obtener datos de los alumnos
        for inscripcion in inscripciones:
            alumno = inscripcion.alumno_id

            alumno_data = {
                'nombre': alumno.nombre,
                'apellido': alumno.apellido,
                'legajo': alumno.legajo,
                'fecha_nacimiento': alumno.fecha_de_nacimiento.strftime('%Y-%m-%d'),
                'email': alumno.email,
                'telefono': alumno.telefono,
                'pais': alumno.pais
            }

            alumnos_inscritos.append(alumno_data)

        # Retornar la lista de alumnos inscritos en formato JSON
        return json.dumps(alumnos_inscritos)