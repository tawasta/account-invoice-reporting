from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    show_customer_address = fields.Boolean(
        string="Show customer address in invoice report",
        config_parameter="account_report_invoice_show_customer_info.show_customer_address",
    )
