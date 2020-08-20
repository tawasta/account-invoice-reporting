# -*- coding: utf-8 -*-

from odoo import fields, models


class AccountInvoiceReport(models.Model):

    _inherit = 'account.invoice.report'

    business_segment = fields.Many2one(
        'business_segment.segment',
        string="Business Segment of the Partner",
        readonly="True"
    )
    business_segment_subsegment = fields.Many2one(
        'business_segment.segment',
        string="Business sub-segment of the Partner",
        readonly="True"
    )

    def _select(self):
        res = super(AccountInvoiceReport, self)._select()
        return res + ', sub.business_segment as business_segment, \
                sub.business_segment_subsegment as business_segment_subsegment'

    def _sub_select(self):
        res = super(AccountInvoiceReport, self)._sub_select()
        return res + ', partner.business_segment as business_segment, \
                partner.business_segment_subsegment as business_segment_subsegment'

    def _group_by(self):
        res = super(AccountInvoiceReport, self)._group_by()
        return res + ', partner.business_segment, partner.business_segment_subsegment'
