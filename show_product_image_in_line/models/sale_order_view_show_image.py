# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    order_line_image = fields.Image(related="product_id.image_1920", string="Image")


class SaleOrderImageEnable(models.Model):
    _inherit = "sale.order"

    show_image_field = fields.Boolean(default=True, string="Show Product Image")
