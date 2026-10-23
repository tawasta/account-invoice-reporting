from odoo import _, models


class AccountMove(models.Model):
    _inherit = "account.move"

    def _is_downpayment_invoice(self):
        """Tell whether the invoice is a down payment, so the report can label it."""
        self.ensure_one()
        return self.move_type == "out_invoice" and self._is_downpayment()

    def _get_report_invoice_title(self):
        """Return the title word the report must print for this invoice."""
        self.ensure_one()
        if self._is_downpayment_invoice():
            return _("Down payment")
        return _("Invoice")

    def _get_report_invoice_orders(self):
        """Return the sale orders this invoice was generated from."""
        # Sudo: printing the report only requires invoicing access, but the orders
        # shown are the ones this invoice's own lines were generated from.
        return self.sudo().line_ids.mapped("sale_line_ids.order_id")

    def _get_report_invoice_order_lines(self, order):
        """Return the ordered products to list under a down payment invoice."""
        product_line_ids = []
        for line in order.order_line:
            is_display_line = line.display_type in ("line_section", "line_note")
            if line.is_downpayment or is_display_line:
                continue
            product_line_ids.append(line.id)
        # Browse through the order's own lines to keep their environment (sudo), as
        # the person printing the report may have no access to sale orders.
        return order.order_line.browse(product_line_ids)
