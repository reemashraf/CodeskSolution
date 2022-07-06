from odoo import api, fields, models, _

class ProductTemplateInherit(models.Model):
    _inherit = 'product.template'

    has_bonus = fields.Boolean("Has Bonus")
    ordered_quantity = fields.Integer("Ordered Quantity")
    bonus_quantity = fields.Integer("Bonus Quantity")
    category_bonus = fields.Boolean(related='categ_id.has_bonus')