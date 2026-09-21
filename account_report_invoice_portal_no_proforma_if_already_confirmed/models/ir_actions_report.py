from odoo import models


class IrActionsReport(models.Model):
    _inherit = "ir.actions.report"

    def _get_rendering_context(self, report, docids, data):
        data = super()._get_rendering_context(report, docids, data)

        # The portal sets 'proforma_invoice' in context when the invoice has no
        # stored PDF from Send & Print. Other proformas (e.g. the Send & Print
        # fallback) are left untouched.
        if not (data.get("proforma") and self.env.context.get("proforma_invoice")):
            return data

        if self._is_invoice_report(report):
            invoices = self.env["account.move"].browse(docids)
            if invoices and all(invoice.state == "posted" for invoice in invoices):
                data.pop("proforma")

        return data
