from odoo import models, fields

class EquipmentFilterWizard(models.TransientModel):
    _name = 'equipment.filter.wizard'
    _description = 'Įrangos filtravimas'

    date_from = fields.Date(string='From')
    date_to = fields.Date(string = 'To')
    employee_id = fields.Many2one('res.users', string='Employee')

    def generate_report(self):
        domain = []
        if self.date_from:
            domain.append(('acquisition_date', '>=', self.date_from))
        if self.date_to:
            domain.append(('acquisition_date', '<=', self.date_to))
        if self.employee_id:
            domain.append(('employee_ids', 'in', self.employee_id.id))
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'equipment.register',
            'view_mode': 'tree',
            'domain': domain,
        }
        