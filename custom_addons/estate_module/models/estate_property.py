from odoo import models, fields


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Property"

    name = fields.Char("Estate Prop Name")