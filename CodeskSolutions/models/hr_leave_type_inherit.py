from odoo import api, fields, models, _

class HRLeaveTypeInherit(models.Model):
    _inherit = 'hr.leave.type'

    allowed_units_per_months = fields.Integer('Allowed units per Months' , default=1)