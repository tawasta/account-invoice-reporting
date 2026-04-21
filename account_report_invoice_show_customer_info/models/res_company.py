from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    show_customer_address = fields.Boolean(
        string="Show customer address in invoice report",
        help="Shows the customer address field in the invoice report",
    )
