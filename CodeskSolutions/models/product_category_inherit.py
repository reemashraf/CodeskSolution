from odoo import api, fields, models, _

class ProductCategoryInherit(models.Model):
    _inherit = 'product.category'

    has_bonus = fields.Boolean("Has Bonus Rules")
