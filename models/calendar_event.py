from odoo import models, fields, _
import logging

_logger = logging.getLogger(__name__)

class CalendarEvent(models.Model):
    _inherit = 'calendar.event'

    privacy = fields.Selection(
        selection=[
            ('public', 'Public'),
            ('private', 'Private'),
            ('confidential', 'Only internal users'),
        ],
        string='Privacy',
        default='private',  # Overridden from original 'public'
        required=True,
        help="People to whom this event will be visible. Defaults to Private to minimize exposure.",
    )
