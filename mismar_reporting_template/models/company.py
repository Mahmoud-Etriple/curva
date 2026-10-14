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
        # domain="[('deprecated', '=', False)]",
    )
    gain_account_id = fields.Many2one(
        "account.account",
        string="Gain Account",
        # domain="[('deprecated', '=', False)]",
    )


class ResPartnerBank(models.Model):
    _inherit = "res.partner.bank"


    @api.onchange("bank_id")
    def _onchange_bank_id_set_bank_name(self):
        for rec in self:
            rec.bank_name = rec.bank_id.name if rec.bank_id else False

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get("bank_id"):
                bank = self.env["res.bank"].browse(vals["bank_id"])
                vals["bank_name"] = bank.name
        return super().create(vals_list)

    def write(self, vals):
        res = super().write(vals)
        if "bank_id" in vals:
            for rec in self:
                rec.bank_name = rec.bank_id.name if rec.bank_id else False
        return res
