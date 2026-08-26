from odoo import fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    show_hs_code_and_coo = fields.Boolean(
        string="Show HS Codes and Country Of Origin in print",
        default=lambda self: self.env.company.always_show_hs_code_and_coo,
        copy=False,
    )

    def set_show_hs_code_and_coo_on_print_as_true(self):
        """Helper function to set as True"""
        for order in self:
            order.show_hs_code_and_coo = True

    def set_show_hs_code_and_coo_on_print_as_false(self):
        """Helper function to set as False"""
        for order in self:
            order.show_hs_code_and_coo = False
