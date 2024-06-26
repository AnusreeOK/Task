from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    minimum_cost = fields.Float(string='Minimum Cost')
    brand_name = fields.Char(string='Brand Name')
