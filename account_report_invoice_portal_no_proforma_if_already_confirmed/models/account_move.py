from odoo import models


class AccountMove(models.Model):
    _inherit = "account.move"

    def _get_invoice_legal_documents(self):
        # Override core's portal download. Core renders a proforma when there is
        # no stored PDF from Send & Print; render a normal invoice instead
        # for posted invoices.

        self.ensure_one()
        if self.invoice_pdf_report_id or self.state != "posted":
            return super()._get_invoice_legal_documents()

        content, _report_format = (
            self.env["ir.actions.report"]
            .with_company(self.company_id)
            ._render("account.account_invoices", self.ids)
        )

        return self.env["ir.attachment"].new(
            {
                "raw": content,
                "name": self._get_invoice_report_filename(),
                "mimetype": "application/pdf",
                "res_model": self._name,
                "res_id": self.id,
            }
        )
