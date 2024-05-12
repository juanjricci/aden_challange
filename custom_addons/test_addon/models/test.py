from odoo import models, fields, api

class Test(models.Model):
    _name = 'test.test'

    name = fields.Char(string="Name")
    date = fields.Date(string="Date")