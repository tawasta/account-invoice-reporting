# -*- coding: utf-8 -*-
from odoo import models, fields


class AccountInvoiceReport(models.Model):

    _inherit = 'account.invoice.report'

    invoice_number = fields.Char(
        string='Invoice Number',
        readonly=True
    )

    def _select(self):
        res = super(AccountInvoiceReport, self)._select()
        return res + ', sub.invoice_number as invoice_number'

    def _sub_select(self):
        res = super(AccountInvoiceReport, self)._sub_select()
        return res + ', ai.number as invoice_number'

    def _group_by(self):
        res = super(AccountInvoiceReport, self)._group_by()
        return res + ', ai.number'
