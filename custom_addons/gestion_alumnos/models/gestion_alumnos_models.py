import re
from odoo import models, fields, api
from odoo.exceptions import ValidationError

# Modelo Alumno
class Alumno(models.Model):
    _name = "gestion.alumnos.alumno"
    _description = "alumno model"

    nombre = fields.Char("Nombre", required=True)
    apellido = fields.Char("Apellido", required=True)
    fecha_de_nacimiento = fields.Date("Fecha de Nacimiento", required=True)
    legajo = fields.Integer("N° de Legajo", required=True)
    # defino un sql constraint para validar que el legajo sea unico
    _sql_constraints = [
        ('unique_legajo', 'unique(legajo)', 'El número de legajo ingresado ya existe')
    ]
    email = fields.Char("Email")
    telefono = fields.Char("Telefono")
    direccion = fields.Char("Direccion")
    # pais = fields.Char("Pais")
    pais = fields.Many2one('res.country', "Pais")
    # pais = fields.Selection([
        # ('ARG', 'Argentina'),
        # ('BOL', 'Bolivia'),
        # ('COL', 'Colombia'),
        # ('CRI', 'Costa Rica'),
        # ('ECU', 'Ecuador'),
        # ('SLV', 'El Salvador'),
        # ('USA', 'Estados Unidos'),
        # ('GUA', 'Guatemala'),
        # ('HON', 'Honduras'),
        # ('MEX', 'México'),
        # ('PAN', 'Panamá'),
        # ('PAR', 'Paraguay'),
        # ('PER', 'Perú'),
        # ('RDO', 'República Dominicana'),
    # ], 'País', default='ARG')

    # funcion para validar que el telefono solo sean digitos
    @api.constrains('telefono')
    def _check_phone_number(self):
        for record in self:
            if record.telefono and not re.match(r'^\+?\d+$', record.telefono):
                raise ValidationError("El telefono debe contener solo digitos.")
            
    # funcion para validar que el email sea de un formato válido
    @api.constrains('email')
    def _check_email(self):
        for record in self:
            if record.email and not re.match(r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.]+\.[a-zA-Z]{2,}$', record.email):
                raise ValidationError("Formato de email inválido.")
            
    # Cambio el display del objeto de Alumno
    def name_get(self):
        result = []
        for record in self:
            nombre = record.nombre
            apellido = record.apellido
            legajo = record.legajo
            desc = f"{apellido}, {nombre} - {str(legajo)}"
            result.append((record.id, desc))
        return result

