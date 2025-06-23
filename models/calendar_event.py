from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
import logging

_logger = logging.getLogger(__name__)

class CalendarEvent(models.Model):
    _inherit = "calendar.event"

    sensitivity = fields.Selection(
        selection=[
            ("normal", "Normal"),
            ("personal", "Personal"),
            ("private", "Private"),
            ("confidential", "Confidential"),
        ],
        string="Sensitivity",
        default="private",
        help="Outlook event sensitivity. Used during Microsoft 365 sync. Defaults to private.",
    )

    def _prepare_ms_event(self, **kwargs):
        """
        Injects sensitivity into the Microsoft Graph payload.
        Falls back to 'private' if not set.
        """
        try:
            ms_event = super()._prepare_ms_event(**kwargs)
            sensitivity_value = self.sensitivity or "private"
            ms_event["sensitivity"] = sensitivity_value
        except Exception as e:
            _logger.exception("Error while setting sensitivity on Microsoft sync: %s", e)
            raise
        else:
            _logger.info(
                "[MS Sync] Calendar Event ID %s set with sensitivity: %s",
                self.id,
                sensitivity_value,
            )
        finally:
            return ms_event

    # ──────────────────────────────────────────────────────────────
    # OPTIONAL UI Section: Comment/remove if you don’t need UI toggle
    # ──────────────────────────────────────────────────────────────
    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        res = super().fields_view_get(view_id, view_type, toolbar, submenu)
        if view_type == 'form' and 'sensitivity' in self._fields:
            try:
                from lxml import etree
                doc = etree.XML(res['arch'])
                for field in doc.xpath("//field[@name='start']"):
                    sensitivity_field = etree.Element("field", name="sensitivity", position="after")
                    field.addnext(sensitivity_field)
                res['arch'] = etree.tostring(doc, encoding='unicode')
            except Exception as e:
                _logger.warning("UI enhancement failed for sensitivity field: %s", e)
        return res
