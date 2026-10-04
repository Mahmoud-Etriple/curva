{
    'name': 'BBR Proforma Invoice (Standard Header)',
    'summary': 'Standalone Proforma Invoice report with a header built from '
               'standard company settings (logo, address, VAT, CR) instead '
               'of an uploaded letterhead image, correct per company.',
    'author': 'Hassan Al toney',
    'website': 'https://',
    'version': '18.0.1.0.0',
    'depends': ['sale', 'mismar_sa_invoice'],
    'category': 'Accounting',
    'data': [
        'views/res_company_views.xml',
        'report/proforma_invoice_standard_report.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
    'post_init_hook': 'post_init_hook',
}
