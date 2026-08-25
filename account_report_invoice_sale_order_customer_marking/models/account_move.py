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

    @api.depends("invoice_line_ids.sale_line_ids.order_id.customer_marking")
    def _compute_customer_marking(self):
        for move in self:
            orders = move.invoice_line_ids.sale_line_ids.order_id
            markings = orders.mapped("customer_marking")
            unique_markings = list(
                dict.fromkeys(marking for marking in markings if marking)
            )
            move.customer_marking = ", ".join(unique_markings)
