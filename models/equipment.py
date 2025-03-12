from odoo import models, fields

class Equipment(models.Model):
    _name = 'equipment.register'
    _description = 'Equipment Register'

    name = fields.Char(string='Name', required=True)
    serial_number = fields.Char(string='Serial Number', required=True)
    description = fields.Text(string='Description')
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)
    create_uid = fields.Many2one('res.users', string='Created By', default=lambda self: self.env.user, readonly=True)
    employee_ids = fields.Many2many('res.users', string='Responsible Employees')