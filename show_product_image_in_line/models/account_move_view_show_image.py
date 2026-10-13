# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    invoice_product_image = fields.Image(related="product_id.image_1920", string="Image")


class AccountMove(models.Model):
    _inherit = "account.move"

    show_image_field = fields.Boolean(default=True, string="Show Product Image")
