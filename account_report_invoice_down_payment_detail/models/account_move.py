from odoo import models


class AccountMove(models.Model):
    _inherit = "account.move"

    def is_down_payment_invoice(self):
        self.ensure_one()
        return any(
            line.is_downpayment and line.price_total >= 0
            for line in self.invoice_line_ids
        )

    def is_refund_invoice(self):
        self.ensure_one()
        return any(line.is_refund for line in self.invoice_line_ids)

    def get_down_payment_sale_orders(self):
        self.ensure_one()
        return self.invoice_line_ids.sale_line_ids.order_id
