from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    brand_name = fields.Char(string='Brand', related='product_id.product_tmpl_id.brand_name', store=True)
    minimum_cost = fields.Float(string='Minimum Cost', related='product_id.product_tmpl_id.minimum_cost', store=True)

    @api.onchange('product_id')
    def _onchange_product_id(self):
        if self.product_id:
            self.brand_name = self.product_id.product_tmpl_id.brand_name
            if self.price_unit < self.product_id.product_tmpl_id.minimum_cost:
                self.price_unit = self.product_id.product_tmpl_id.minimum_cost
