from odoo import api, fields, models, _

class AccountMoveLineInherit(models.Model):
    _inherit = 'account.move.line'

    bonus_quantity = fields.Integer("Bonus Quantity", compute='_get_bonus_quantity',readonly='False')
    bonus_line = fields.Boolean("Bonus_Line" , default=False) # in order not to get in infinite loop while creating new line

    @api.onchange('quantity')
    def _get_bonus_quantity(self):
        '''
        this Function responsible for getting and setting bonus quantity value
        '''
        for rec in self :
            if rec.product_id.product_tmpl_id.has_bonus:
                rec.bonus_quantity = (rec.product_id.product_tmpl_id.bonus_quantity) * int(rec.quantity / rec.product_id.product_tmpl_id.ordered_quantity)
            else:
                rec.bonus_quantity = 0
