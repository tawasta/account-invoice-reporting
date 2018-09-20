# -*- coding: utf-8 -*-
from odoo import models, fields


class AccountInvoiceReport(models.Model):

    _inherit = 'account.invoice.report'

    invoice_vendor_reference = fields.Char(
        string='Vendor Reference',
        readonly=True
    )

    def _select(self):
        res = super(AccountInvoiceReport, self)._select()
        return res \
            + ', sub.invoice_vendor_reference as invoice_vendor_reference'

    def _sub_select(self):
        res = super(AccountInvoiceReport, self)._sub_select()
        return res + ', ai.reference as invoice_vendor_reference'

    def _group_by(self):
        res = super(AccountInvoiceReport, self)._group_by()
        return res + ', ai.reference'
