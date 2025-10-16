from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    module_account_report_invoice_bank_transfer = fields.Boolean(
        string="Bank Transfer Info", help="Add a bank transfer section for invoices"
    )
    module_account_report_invoice_barcode = fields.Boolean(
        string="Barcode", help="Show barcode in invoice PDF"
    )
    module_account_report_invoice_business_code = fields.Boolean(
        string="Business Code", help="Show business code in invoice PDF"
    )
    module_account_report_invoice_customer_contact = fields.Boolean(
        string="Customer Contact", help="Show customer contact in invoice PDF"
    )
    module_account_report_invoice_delivery_date = fields.Boolean(
        string="Delivery Date", help="Adds Delivery date to invoice PDF print"
    )
    module_account_report_invoice_eori = fields.Boolean(
        string="EORI", help="Adds customer's EORI code to Account Invoice print"
    )
    module_account_report_invoice_hide_customer_code = fields.Boolean(
        string="Hide Customer Code", help="Hide customer code from invoice PDF print"
    )
    module_account_report_invoice_hide_incoterm_under_note = fields.Boolean(
        string="Hide Incoterm Under Note",
        help="Invoice PDF - Hide incoterm located under the note",
    )
    module_account_report_invoice_hide_invoice_name = fields.Boolean(
        string="Hide Invoice Name",
        help="Configurable option for hiding invoice name on print",
    )
    module_account_report_invoice_hide_origin = fields.Boolean(
        string="Hide Origin", help="Hide origin from invoice PDF print"
    )
    module_account_report_invoice_hide_payment_communication = fields.Boolean(
        string="Hide Payment Communication",
        help="Invoice PDF – Hide payment communication under note",
    )
    module_account_report_invoice_hide_payment_term_under_note = fields.Boolean(
        string="Hide Payment Term Under Note",
        help="Invoice PDF – Hide payment term under note",
    )
    module_account_report_invoice_line_subtotal_with_tax = fields.Boolean(
        string="Line Subtotal With Tax",
        help="Include taxes in the subtotal of Invoice PDF print",
    )
    module_account_report_invoice_payment = fields.Boolean(
        string="Payment Terminology",
        help="Changes 'invoice' to 'receipt' for PDF print and email template",
    )
    module_account_report_invoice_payment_term_header = fields.Boolean(
        string="Payment Term Header", help="Show payment term in invoice header"
    )
    module_account_report_invoice_payment_term_text = fields.Boolean(
        string="Payment Term Text",
        help="Show 'Payment terms:' text on Invoice PDF print",
    )
    module_account_report_invoice_quantity_decimals = fields.Boolean(
        string="Quantity Decimals",
        help="Change the number of decimals shown on invoice PDF product quantities",
    )
    module_account_report_invoice_reformat = fields.Boolean(
        string="Reformat Invoice Print",
        help="Reformat invoice print elements for cleaner look",
    )
    module_account_report_invoice_report_configurator = fields.Boolean(
        string="Report Configurator",
        help="Central control for all account_report_invoice_* modules",
    )
    module_account_report_invoice_sale_partner_id = fields.Boolean(
        string="Sale Partner ID", help="Show customer in invoice PDF"
    )
    module_account_report_invoice_salesperson = fields.Boolean(
        string="Salesperson", help="Show salesperson in invoice PDF"
    )
    module_account_report_invoice_show_invoice_address = fields.Boolean(
        string="Show Invoice Address",
        help="Show Invoice address text above Customer info in Invoice PDF print",
    )
