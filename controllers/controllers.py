# -*- coding: utf-8 -*-
# from odoo import http


# class CalendarEventPrivacy(http.Controller):
#     @http.route('/calendar_event_privacy/calendar_event_privacy', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/calendar_event_privacy/calendar_event_privacy/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('calendar_event_privacy.listing', {
#             'root': '/calendar_event_privacy/calendar_event_privacy',
#             'objects': http.request.env['calendar_event_privacy.calendar_event_privacy'].search([]),
#         })

#     @http.route('/calendar_event_privacy/calendar_event_privacy/objects/<model("calendar_event_privacy.calendar_event_privacy"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('calendar_event_privacy.object', {
#             'object': obj
#         })

