from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    show_customer_address = fields.Boolean(
        string="Show customer address in invoice report",
        related="company_id.show_customer_address",
        readonly=False,
    )
