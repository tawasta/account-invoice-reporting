from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    customer_marking = fields.Char(
        compute="_compute_customer_marking",
        store=True,
        help="Customer marking(s) of the related sale order(s). If the "
        "sale orders have different markings, all distinct values are "
        "shown, comma-separated.",
    )

    @api.depends("sale_order_ids.customer_marking")
    def _compute_customer_marking(self):
        for move in self:
            markings = move.sale_order_ids.mapped("customer_marking")
            unique_markings = list(
                dict.fromkeys(marking for marking in markings if marking)
            )
            move.customer_marking = ", ".join(unique_markings)
