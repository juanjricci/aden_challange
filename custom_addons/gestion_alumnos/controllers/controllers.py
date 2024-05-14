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
            ('programa_id', '=', programa_id)
        ])

        # Convertir registros a formato JSON
        data = []
        for programa in programas:
            data.append({
                'id': programa.id,
                'alumno_id': programa.alumno_id.id,
                'programa_id': programa.programa_id.id,
            })

        # Devolver respuesta JSON
        return json.dumps(data)
    
