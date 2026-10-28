from odoo import _, api, fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    def _get_journal_entry_pdf_document(self):
        """Render the shared report for a miscellaneous journal entry."""
        self.ensure_one()
        report = self.env.ref('mismar_sa_invoice.account_journal_entries_custom_sa')
        content, _report_type = report._render_qweb_pdf(
            report.report_name,
            res_ids=self.ids,
        )
        clean_name = (self.name or 'Journal Entry').replace('/', '_')
        return {
            'filename': f'Journal Entry - {clean_name}.pdf',
            'filetype': 'application/pdf',
            'content': content,
        }

    def _get_invoice_legal_documents(self, filetype, allow_fallback=False):
        """Support journal entries even when an already-open UI uses Odoo's
        original ``/account/download_invoice_documents/.../pdf`` URL.
        """
        self.ensure_one()
        if self.move_type == 'entry' and filetype == 'pdf':
            return self._get_journal_entry_pdf_document()
        return super()._get_invoice_legal_documents(filetype, allow_fallback=allow_fallback)

    def _get_invoice_legal_documents_all(self, allow_fallback=False):
        self.ensure_one()
        if self.move_type == 'entry':
            return [self._get_journal_entry_pdf_document()]
        return super()._get_invoice_legal_documents_all(allow_fallback=allow_fallback)

    def action_invoice_download_pdf(self):
        """Always return Odoo's direct download URL action.

        ``_get_invoice_legal_documents`` above now supports journal entries, so
        the standard URL works for both kinds of move and is handled correctly
        by the dynamic Download menu.
        """
        return super().action_invoice_download_pdf()


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
