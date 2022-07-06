from odoo import api, fields, models, _

class AccountMoveInherit(models.Model):
    _inherit = 'account.move'

    def _create_bonus_lines(self):
        for inv in self.filtered(lambda x: x.move_type == 'out_invoice'):
            for line in inv.invoice_line_ids :
                print("hhhh")
                if not (line.bonus_line) and line.bonus_quantity != 0 and line.quantity > 0:
                    print("hereeee")
                    bonus_line = line.copy({
                        'exclude_from_invoice_tab': True,
                        'price_unit': 0.0,
                        'quantity': line.bonus_quantity,
                        'bonus_line': True,
                        'debit': 0, 'credit': 0, 'balance': 0})

    @api.model_create_multi
    def create(self, vals_list):
        move = super(AccountMoveInherit, self).create(vals_list)
        move._create_bonus_lines()
        return move


