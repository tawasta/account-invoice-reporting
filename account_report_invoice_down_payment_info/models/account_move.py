from odoo import models


class AccountMove(models.Model):
    _inherit = "account.move"

    # Check that downpayment is true and price is zero or positive
    def compute_downpayment_info(self):
        invoice_downpayment = any(
            line.is_downpayment and line.price_total >= 0
            for line in self.invoice_line_ids
        )
        return invoice_downpayment

    def compute_refund(self):
        invoice_refund = any(line.is_refund for line in self.invoice_line_ids)
        return invoice_refund
