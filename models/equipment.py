from odoo import models, fields

class Equipment(models.Model):
    _name = 'equipment.register'
    _description = 'Equipment Register'

    name = fields.Char(string='Įrangos pavadinimas', required=True)
    serial_number = fields.Char(string='Unikalus įrangos identifikatorius', required=True)
    description = fields.Text(string='Papildoma informacija apie įrangą')
    company_id = fields.Many2one('res.company', string='Įrangą valdanti įmonė', default=lambda self: self.env.company)
    create_uid = fields.Many2one('res.users', string='Sukūręs vartotojas', default=lambda self: self.env.user, readonly=True)
    employee_ids = fields.Many2many('res.users', string='Atsakingi darbuotojai')
    acquisition_date = fields.Date(string= 'Įsigijimo data', default=fields.Date.today)