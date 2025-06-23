# -*- coding: utf-8 -*-
{
    'name': "Calendar Event Privacy Default",

    'summary': "Odoo calendar events to private sensitivity",

    'description': """
Default new Odoo calendar events to private sensitivity for Microsoft Outlook sync.

Go to Settings → Technical → Security → Record Rules

Search for model: calendar.event

Disable the following by unchecking all access rights or archiving:

"All Calendar Event for employees"

"Own events"

"Private events"

Keep only this active:

Calendar: Hide Others’ Private Events

    """,

    'author': "CodeRomz",
    'website': "https://github.com/CodeRomz/calendar_event_privacy",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'version': '17.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['calendar'],

    "data": [
        "security/calendar_view_privacy_security.xml",
        "views/calendar_event_view.xml",
    ],

    "installable": True,
    "application": False,
    "auto_install": False,



}

