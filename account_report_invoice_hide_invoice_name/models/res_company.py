from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    hide_invoice_name = fields.Boolean(
        string="Hide Invoice Name on PDF Print",
        help="Hides the name field (e.g. 'Invoice INV/2025/001') on invoice PDFs",
    )
