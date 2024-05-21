import json

from odoo import http
from odoo.http import Response, request

class Tracking(http.Controller):
 
    # @http.route('/api/programas/<int:programa_id>', auth='public')
    # def get_programas(self, programa_id):
    #     # Obtener registros del modelo 'gestion.alumnos.programa'
    #     programas = http.request.env['gestion.alumnos.programa'].search([
    #         ('id', '=', programa_id)
    #     ])

    #     # Convertir registros a formato JSON
    #     data = []
    #     for programa in programas:
    #         data.append({
    #             'id': programa.id,
    #             'nombre': programa.nombre,
    #             'descripcion': programa.descripcion,
    #         })

    #     # Devolver respuesta JSON
    #     return json.dumps(data)
    
    @http.route('/api/inscriptos/programa/<int:programa_id>', auth='public')
    def get_programas(self, programa_id):
        # Obtener registros del modelo 'gestion.alumnos.programa'
        programas = http.request.env['gestion.alumnos.inscripcion'].search([
            # '|',
            ('programa_id', '=', programa_id),
            # ('fecha_de_inscripcion', '>=', '2023-01-01')
        ])

        # Convertir registros a formato JSON
        data = []
        for programa in programas:
            data.append({
                'id': programa.alumno_id.id,
                'nombre': programa.alumno_id.nombre,
                'apellido': programa.alumno_id.apellido,
                'fecha_de_nacimiento': str(programa.alumno_id.fecha_de_nacimiento),
                'legajo': programa.alumno_id.legajo,
                'email': programa.alumno_id.email,
                'telefono': programa.alumno_id.telefono,
                'direccion': programa.alumno_id.direccion,
                'pais': {
                    'id': programa.alumno_id.pais.id,
                    'name': programa.alumno_id.pais.name
                    },
                'programa_id': programa.programa_id.id,
            })

        # Devolver respuesta JSON
        return json.dumps(data)
    
    