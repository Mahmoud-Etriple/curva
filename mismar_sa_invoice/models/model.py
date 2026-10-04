from odoo import _, api, fields, models

class AccountEinv(models.Model):
    _inherit = 'res.partner'

    arabic_name = fields.Char(string="Name AR")
    english_name = fields.Char(string="Name EN")
    arabic_project = fields.Char(string="Project AR")
    english_project = fields.Char(string="Project EN")
    commercial_records = fields.Char(string="Commercial Record")
    contract_no = fields.Char(string="Contract No.")
    quotation_no = fields.Char(string="Quotation No.")
    po_no = fields.Char(string="Po No.")

class CompanyEinv(models.Model):
    _inherit = 'res.company'

    invoice_stamp_sa = fields.Binary(string="Invoice Stamp", attachment=True, store=True)


class ResPartnerBank(models.Model):
    _inherit = 'res.partner.bank'

    iban = fields.Char(string="IBAN", help="International Bank Account Number")