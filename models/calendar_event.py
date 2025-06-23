from odoo import api, fields, models, _
import logging

_logger = logging.getLogger(__name__)


class CalendarEvent(models.Model):
    _inherit = "calendar.event"

    calendar_view = fields.Selection(
        [
            ("public", "Public"),
            ("private", "Private"),
        ],
        string="Calendar Visibility",
        default="private",
        help=(
            "Controls whether other users see this event when they enable "
            "\"Everybody's calendar\". Does NOT affect the native "
            "Privacy field or external (Office 365) synchronisation."
        ),
    )

    # ---------------------------------------------------------------------
    # Optional logging (keeps code lightweight but traceable)
    # ---------------------------------------------------------------------
    @api.model_create_multi
    def create(self, vals_list):
        events = super().create(vals_list)
        for event in events:
            _logger.info(
                "Event %s created with calendar_view=%s",
                event.id,
                event.calendar_view,
            )
        return events

    def write(self, vals):
        res = super().write(vals)
        if "calendar_view" in vals:
            for event in self:
                _logger.info(
                    "Event %s calendar_view changed to %s",
                    event.id,
                    event.calendar_view,
                )
        return res
