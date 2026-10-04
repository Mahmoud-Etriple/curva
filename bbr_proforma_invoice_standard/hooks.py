import base64
import logging

from odoo.modules.module import get_module_resource

_logger = logging.getLogger(__name__)

# Maps each known company (matched by its unique `name`) to the bundled
# letterhead image that should seed its `proforma_header_image` field on
# install. Companies not listed here (or added later) simply fall back to
# the logo/address block until someone uploads an image via the company
# form.
_COMPANY_HEADER_IMAGES = {
    'BBR KSA': 'header_bbr_ksa.png',
    'BBR Bahrain': 'header_bbr_bahrain.jpg',
    'شركة خزاما للخدمات التجارية': 'header_lavander.png',
}


def post_init_hook(env):
    """Seed the known companies' proforma header image on install."""
    for company_name, filename in _COMPANY_HEADER_IMAGES.items():
        company = env['res.company'].search([('name', '=', company_name)], limit=1)
        if not company or company.proforma_header_image:
            continue
        path = get_module_resource(
            'bbr_proforma_invoice_standard', 'static', 'img', filename)
        if not path:
            _logger.warning(
                "bbr_proforma_invoice_standard: header image %s not found", filename)
            continue
        with open(path, 'rb') as image_file:
            company.proforma_header_image = base64.b64encode(image_file.read())
