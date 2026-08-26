from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    always_show_hs_code_and_coo = fields.Boolean(
        string="Always show HS code and Country Of Origin in invoice PDF",
        default=False,
    )
