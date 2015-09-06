
from django import template

register = template.Library()


@register.filter()
def any_foo(field):
    return field


@register.filter()
def disabled_switch(field):
    return "disabled" if not field else ""

# eof
