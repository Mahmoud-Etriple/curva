from odoo import api, fields, models, _


class ResCompanyApplication(models.Model):
    _inherit = 'res.company'

    template_primary_color = fields.Char()
    template_secondary_color = fields.Char()
    templates_primary_font = fields.Char()
    templates_secondary_font = fields.Char()
    custom_image = fields.Binary(
        string='Custom Header Image',
        help='Upload a custom image for the company'
    )
    custom_footer_image = fields.Binary(
        string='Custom Footer Image',
        help='Upload a custom Footer for the company'
    )
    custom_image_filename = fields.Char(
        string='Custom Image Filename'
    )
    invoice_signature = fields.Binary(
        string="Invoice Signature",
    )
    bank_ids = fields.One2many(
        "res.partner.bank",
        "company_id",
        string="Bank Accounts",
    )

    invoice_stamp = fields.Binary(string="Invoice Stamp")
    loss_account_id = fields.Many2one(
        "account.account",
        string="Loss Account",
        domain="[('deprecated', '=', False)]",
    )
    gain_account_id = fields.Many2one(
        "account.account",
        string="Gain Account",
        domain="[('deprecated', '=', False)]",
    )