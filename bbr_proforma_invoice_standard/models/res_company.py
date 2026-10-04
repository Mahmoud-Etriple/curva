from odoo import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    proforma_header_image = fields.Binary(
        string="Proforma Header Image",
        attachment=True,
        help="Full-width letterhead image printed at the top of the "
             "standalone Proforma Invoice report. Falls back to the "
             "logo/address block below when left empty.",
    )
