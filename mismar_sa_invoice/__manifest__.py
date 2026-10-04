{
    'name': 'Mismar Invoice SA',
    'author': 'Mismar',
    'website': 'https://www.mismar.ai',
    'version': '18.0.1.0.1',
    'depends': ['account','l10n_sa_edi','l10n_gcc_invoice','mismar_reporting_template'],
    'category': 'Accounting',
    'data': [
        # 'security/ir.model.access.csv',
        'views/view.xml',
        'report/einv_report.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}