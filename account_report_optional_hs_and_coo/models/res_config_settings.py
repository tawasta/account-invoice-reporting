from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    always_show_hs_code_and_coo = fields.Boolean(
        string="Always show HS code and Country Of Origin in invoice PDF",
        related="company_id.always_show_hs_code_and_coo",
        readonly=False,
    )
