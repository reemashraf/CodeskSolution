from odoo import api, fields, models, _
from dateutil import parser
from odoo.exceptions import UserError

class HrLeaveInherit(models.Model):
    _inherit = 'hr.leave'


    def check_validity(self, vals_list):
        '''
        This function is responsible for checking if the employee have max limit holidays in this month
        '''
        for rec in vals_list :
            employee_id = rec.get('employee_id')
            holiday_type = rec.get('holiday_status_id')
            max_holidays = self.env['hr.leave.type'].browse([holiday_type]).allowed_units_per_months
            date = parser.parse(rec.get('request_date_from'))
            month = date.month
            year = date.year
            # get all employee holidays in this month
            holidays = self.env['hr.leave'].search([('employee_id', '=', employee_id),('state','=','validate'),
            ('date_from','>=',parser.parse('{y}-{m}-01'.format(y=year ,m=month))),('date_from', '<=',parser.parse('{y}-{m}-31'.format(y=year ,m=month)))])
            duration_sum = 0
            for holiday in holidays :
                duration_sum += holiday.number_of_days
            if duration_sum + rec.get('number_of_days',0) < max_holidays:
                return True
            else:
                return False


    @api.model_create_multi
    def create(self, vals_list):
        if self.check_validity(vals_list):
            return super().create(vals_list)
        else:
           raise UserError('Can\'t Create Time Off Request as this Employee has its maximum limit for this month')




