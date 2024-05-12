from odoo import models, fields, api, _

class LabPatient(models.Model):
    _name = 'lab.patient'
    _rec_name = 'patient'
    _description = 'Patient'

    patient = fields.Many2one('res.partner', string='Partner', required=True)
    patient_id = fields.Char(string='Patient ID', readonly=True)
    name = fields.Char(string='Patient Name', default=lambda self: _('New'))
    title = fields.Selection([
        ('ms', 'Miss'),
        ('mister', 'Mister'),
        ('mrs', 'Mrs'),
    ], string='Title', default='mister', required=True)