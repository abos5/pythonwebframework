from django import template
# abox
from abox import logger
import abox.widgets


register = template.Library()

"""
whether or not use the form control class in admin template
"""
NO_FORM_CONTROL_WIDGET_TYPES = [
    'adminradioselect',
    'checkboxselectmultiple',
    'readonlypasswordhashwidget',
    'adminfilewidget',
    'ueditor',
    'aboxsplitdatetime',
]


@register.filter()
def no_form_control_widget_types(widget_type):
    return widget_type in NO_FORM_CONTROL_WIDGET_TYPES

# eof
