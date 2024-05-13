import json

from odoo import http
from odoo.http import Response, request

class Tracking(http.Controller):
    @http.route('/dataset/<int:programa_id>', type='http', auth="public")
    def tracking(self, programa_id):
        return "Hola mundo - " + str(programa_id)
    
    # @http.route('/programas/<model("gestion.alumnos.programa"):programa_id>', auth="public")
    # def tracking(self, programa_id):
    #     return http.request.render({
    #         "programa":programa_id
    #     })