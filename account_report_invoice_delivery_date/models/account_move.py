
from odoo import fields, models


class AccountMove(models.Model):

    _inherit = "account.move"

    date_delivered = fields.Date(
        help="The date when the invoiced product or service was considered "
        "delivered, for taxation purposes."
    )
