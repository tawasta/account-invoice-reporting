# -*- coding: utf-8 -*-
from odoo import models, fields


class AccountInvoiceReport(models.Model):

    _inherit = 'account.invoice.report'

    invoice_partner_invoice_id = fields.Many2one(
        comodel_name='res.partner',
        string='Invoice Address',
        readonly=True
    )

    def _select(self):
        res = super(AccountInvoiceReport, self)._select()
        return res + \
            ', sub.invoice_partner_invoice_id as invoice_partner_invoice_id'

    def _sub_select(self):
        res = super(AccountInvoiceReport, self)._sub_select()
        return res + ', ai.partner_invoice_id as invoice_partner_invoice_id'

    def _group_by(self):
        res = super(AccountInvoiceReport, self)._group_by()
        return res + ', ai.partner_invoice_id'
