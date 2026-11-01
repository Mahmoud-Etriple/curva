from . import models


def post_init_hook(env):
    """Give a number to all the existing entries (ordered by id)."""
    seq = env['ir.sequence'].search(
        [('code', '=', 'account.move.entry.number')], limit=1)
    env.cr.execute(
        "SELECT id FROM account_move WHERE entry_number IS NULL ORDER BY id")
    ids = [r[0] for r in env.cr.fetchall()]
    for move_id in ids:
        env.cr.execute(
            "UPDATE account_move SET entry_number = %s WHERE id = %s",
            (seq.next_by_id(), move_id))
    env.invalidate_all()
