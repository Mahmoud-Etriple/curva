from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    entry_number = fields.Char(
        string='Entry Number',
        readonly=True,
        copy=False,
        index=True,
    )

    def _compute_ref_from_lines(self):
        for move in self:
            labels = []
            for line in move.line_ids:
                name = (line.name or '').strip()
                if name and name not in labels:
                    labels.append(name)
            move.ref = ' / '.join(labels)

    @api.model_create_multi
    def create(self, vals_list):
        seq = self.env['ir.sequence']
        for vals in vals_list:
            if not vals.get('entry_number'):
                vals['entry_number'] = seq.next_by_code(
                    'account.move.entry.number')

        moves = super().create(vals_list)
        for move in moves:
            if move.move_type == 'entry' and not move.ref:
                move._compute_ref_from_lines()
        return moves

    def write(self, vals):
        res = super().write(vals)
        if 'line_ids' in vals:
            for move in self:
                if move.move_type == 'entry' and not move.ref:
                    move._compute_ref_from_lines()
        return res
