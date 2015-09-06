from django import template
# abox
from abox import logger
import abox.widgets


register = template.Library()


@register.filter()
def no_form_control_widget_types(widget_type):
    return widget_type in abox.widgets.NO_FORM_CONTROL_WIDGET_TYPES

# eof
