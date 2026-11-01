{
    'name': 'Journal Entry Number (Trx #)',
    'version': '18.0.1.0.0',
    'category': 'Accounting',
    'summary': 'Sequential Entry Number on every journal entry with Trx # print',
    'depends': ['account'],
    'data': [
        'data/sequence.xml',
        'views/account_move_views.xml',
        'report/report_journal_entry.xml',
    ],
    'post_init_hook': 'post_init_hook',
    'license': 'LGPL-3',
    'installable': True,
}
