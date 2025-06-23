# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class calendar_event_privacy(models.Model):
#     _name = 'calendar_event_privacy.calendar_event_privacy'
#     _description = 'calendar_event_privacy.calendar_event_privacy'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

