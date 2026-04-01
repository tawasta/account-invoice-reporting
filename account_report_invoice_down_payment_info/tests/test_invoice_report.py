from lxml import html as lxml_html

from odoo.tests.common import TransactionCase


class TestInvoiceReport(TransactionCase):
    post_install = True

    #########################################################
    # Bunch of setup code to create test data for the tests #
    #########################################################
    def setUp(self):
        super().setUp()
        self.partner = self.env["res.partner"].create({"name": "Test Partner"})
        self.journal = self.env["account.journal"].create(
            {
                "name": "Test Journal",
                "code": "TST",
                "type": "sale",
                "company_id": self.env.company.id,
            }
        )
        self.income_account = self.env["account.account"].create(
            {
                "name": "Income Account",
                "code": "INC100",
                "account_type": "income",
                "company_id": self.env.company.id,
            }
        )
        self.receivable_account = self.env["account.account"].create(
            {
                "name": "Receivable",
                "code": "REC100",
                "account_type": "asset_receivable",
                "company_id": self.env.company.id,
            }
        )
        self.partner.property_account_receivable_id = self.receivable_account
        self.product = self.env["product.product"].create(
            {
                "name": "Test Product",
                "type": "consu",
                "list_price": 50,
            }
        )

    def _render_invoice(self, move):
        report = self.env.ref("account.account_invoices")
        html, _ = report._render("account.report_invoice", move.ids)
        return html.decode()

    def _create_invoice(self, is_downpayment=False, price_unit=100):
        return self.env["account.move"].create(
            {
                "move_type": "out_invoice",
                "partner_id": self.partner.id,
                "journal_id": self.journal.id,
                "invoice_line_ids": [
                    (
                        0,
                        0,
                        {
                            "name": "Line",
                            "quantity": 1,
                            "price_unit": price_unit,
                            "account_id": self.income_account.id,
                            "is_downpayment": is_downpayment,
                        },
                    )
                ],
            }
        )

    # Down payment false and price total >= 0 = should return false
    def test_downpayment_flag_false(self):
        move = self._create_invoice(is_downpayment=False, price_unit=100)
        self.assertFalse(move.compute_downpayment_info())

    # Down payment true and price total >= 0 = should return true
    def test_downpayment_flag_true(self):
        move = self._create_invoice(is_downpayment=True, price_unit=100)
        self.assertTrue(move.compute_downpayment_info())

    # Down payment true and price total < 0 = should return false
    def test_downpayment_flag_true_negative_total(self):
        move = self._create_invoice(is_downpayment=True, price_unit=-1)
        self.assertFalse(move.compute_downpayment_info())

    # Down payment false and price total < 0 = should return false
    def test_downpayment_flag_false_negative_total(self):
        move = self._create_invoice(is_downpayment=False, price_unit=-1)
        self.assertFalse(move.compute_downpayment_info())

    # Down payment text in the h2 element
    def test_report_downpayment_title(self):
        move = self._create_invoice(is_downpayment=True)
        move.action_post()
        html = self._render_invoice(move)
        doc = lxml_html.fromstring(html)
        h2_text = "".join(doc.xpath("//h2//text()")).strip()
        self.assertIn("Down payment", h2_text)

    # No down payment when not down payment
    def test_report_normal_invoice_title(self):
        move = self._create_invoice(is_downpayment=False)
        move.action_post()
        html = self._render_invoice(move)
        doc = lxml_html.fromstring(html)
        h2_text = "".join(doc.xpath("//h2//text()")).strip()
        self.assertIn("Invoice", h2_text)

    # Table appears when down payment is true
    def test_downpayment_extra_table(self):
        sale_order = self.env["sale.order"].create(
            {
                "partner_id": self.partner.id,
            }
        )
        self.env["sale.order.line"].create(
            {
                "order_id": sale_order.id,
                "product_id": self.product.id,
                "product_uom_qty": 2,
                "price_unit": 50,
            }
        )
        move = self.env["account.move"].create(
            {
                "move_type": "out_invoice",
                "partner_id": self.partner.id,
                "journal_id": self.journal.id,
                "invoice_origin": sale_order.name,
                "invoice_line_ids": [
                    (
                        0,
                        0,
                        {
                            "name": "Down payment",
                            "quantity": 1,
                            "price_unit": 100,
                            "account_id": self.income_account.id,
                            "is_downpayment": True,
                        },
                    )
                ],
            }
        )

        move.action_post()
        html = self._render_invoice(move)
        self.assertIn("Test Product", html)
        self.assertIn("2", html)
        self.assertIn("50", html)

    # No table when down payment is false
    def test_no_extra_table_for_normal_invoice(self):
        move = self._create_invoice(is_downpayment=False)
        move.action_post()
        html = self._render_invoice(move)
        doc = lxml_html.fromstring(html)
        tables = doc.xpath("//table[contains(@class, 'mt-2')]")
        self.assertFalse(tables, "Extra table should not appear for normal invoice")
