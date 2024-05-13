import json

from odoo import http
from odoo.http import Response, request

class Tracking(http.Controller):
    # @http.route('/dataset/<int:programa_id>', type='http', auth="public")
    # def tracking(self, programa_id):
    #     return "Hola mundo - " + str(programa_id)
    
    # @http.route('/programas/<model("gestion.alumnos.programa"):programa_id>', auth="public")
    # def tracking(self, programa_id):
    #     return http.request.render({
    #         "programa":programa_id
    #     })

    # @http.route("/check_method_get", auth='none',method=['GET'])
    # def check_method_get(self,**values):
    #     output = {
    #         'results':{
    #             'code':200,
    #             'message':'OK'
    #         }
    #     }
    #     return json.dumps(output['results'])
    


    # @http.route('/programas/<int:programa_id>', auth='public', method=['GET'])
    # def get_alumnos_inscritos(self, programa_id):
    #     programa = http.request.env['gestion.alumnos.programa']
    #     data = json.loads(programa)
    #     # programas = programa.sudo().search([('programa_id', '=', programa_id)])
    #     # programas_json = {
    #     #     'programas' : programas
    #     # }
    #     return json.dumps(programa)}

    # @http.route('/programas', auth='public', method=['GET'])
    # def get_alumnos_inscritos(self):
    #     programa = http.request.env['gestion.alumnos.programa'].sudo().search([])
    #     return programa

    @http.route('/api/programas', auth='public')
    def get_programas(self):
        # Obtener registros del modelo 'gestion.alumnos.programa'
        programas = http.request.env['gestion.alumnos.programa'].search([])

        # Convertir registros a formato JSON
        data = []
        for programa in programas:
            data.append({
                'id': programa.id,
                'nombre': programa.nombre,
                'descripcion': programa.descripcion,
            })

        # Devolver respuesta JSON
        return json.dumps(data)