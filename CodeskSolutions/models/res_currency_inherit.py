from odoo import api, fields, models, _

class CurrencyInherit(models.Model):
    _inherit = 'res.currency'

    secondary_currency = fields.Many2one('res.currency','Foreign Currency')
    sale_price = fields.Monetary('Secondary Sale Price', currency_field='secondary_currency')
    buy_price = fields.Monetary('Secondary Buy Price',currency_field='secondary_currency')
    base_sale_price = fields.Monetary('Base Sale Price' ,currency_field='secondary_currency')
    base_buy_price = fields.Monetary('Base Buy Price', currency_field='secondary_currency')
    tolerance = fields.Integer('Tolerance')
    evaluation = fields.Monetary('Evaluation', currency_field='secondary_currency')

