from odoo import models


class AccountMove(models.Model):
    _inherit = "account.move"

    def _get_invoice_pdf_proforma(self):
        # Core returns a proforma for the portal download when there is no
        # stored PDF generated via clicking backend Send & Print yet.
        # Render a normal invoice instead for posted invoices.

        self.ensure_one()
        if self.state != "posted":
            return super()._get_invoice_pdf_proforma()

        report = self.partner_id.invoice_template_pdf_report_id or self.env.ref(
            "account.account_invoices"
        )
        action_report = self.env["ir.actions.report"].with_company(self.company_id)
        content, report_type = action_report._pre_render_qweb_pdf(
            report.report_name, self.ids
        )
        content_by_id = action_report._get_splitted_report(
            report.report_name, content, report_type
        )

        return {
            "filename": self._get_invoice_report_filename(report=report),
            "filetype": "pdf",
            "content": content_by_id[self.id],
        }
