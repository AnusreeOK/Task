from odoo import models, fields

class AccountMove(models.Model):
    _inherit = 'account.move'

    delivery_charge = fields.Monetary(string='Delivery Charge')
