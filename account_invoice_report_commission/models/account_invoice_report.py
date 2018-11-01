# -*- coding: utf-8 -*-
from odoo import models, fields


class AccountInvoiceReport(models.Model):

    _inherit = 'account.invoice.report'

    invoice_commission_paid = fields.Boolean(
        string='Commission Paid',
        readonly=True
    )

    def _select(self):
        res = super(AccountInvoiceReport, self)._select()
        return res \
            + ', sub.invoice_commission_paid as invoice_commission_paid'

    def _sub_select(self):
        res = super(AccountInvoiceReport, self)._sub_select()
        return res + ', ai.commission_paid as invoice_commission_paid'

    def _group_by(self):
        res = super(AccountInvoiceReport, self)._group_by()
        return res + ', ai.commission_paid'
