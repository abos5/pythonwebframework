# -*- coding: utf-8 -*-
from django.contrib.admin import widgets
from django.forms.widgets import Widget
from django.utils.html import format_html
from django.forms.utils import flatatt
from django.utils.encoding import force_text
from django.utils.translation import ugettext as _
from abox import logger


class AboxSplitDateTime(widgets.AdminSplitDateTime):
    """
    A SplitDateTime Widget that save a line break
    """

    def format_output(self, rendered_widgets):
        return format_html('<p class="datetime">{0} {1} {2} {3}</p>',
                           _('Date:'), rendered_widgets[0],
                           _('Time:'), rendered_widgets[1])


class Ueditor(Widget):

    class Media:
        js = (
            "abox/ueditor/ueditor.config.js",
            "abox/ueditor/ueditor.all.js",
        )

    def __init__(self, attrs=None):
        # Use slightly better defaults than HTML's 20x2 box
        default_attrs = {
            'ueditor': {
                "initialFrameWidth": 800,
                "initialFrameHeight": 300,
            },
        }
        if attrs:
            default_attrs.update(attrs)
        super(Ueditor, self).__init__(default_attrs)

    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        content = u"<textarea {0} >{1}</textarea>"
        # use double braces to output ueditor configuration
        # should be fixed if bug found.
        scripts = u"""\
        <script type="text/javascript">
        'use strict';
        (function($){{
        $(function(){{
            var editor = new UE.ui.Editor({%(ueditor)s});
            editor.render('%(id)s');
        }});
        }})(django.jQuery);
        </script>
        """ % {
            'name': name,
            'id': final_attrs.get('id', ''),
            'ueditor': final_attrs.get('ueditor', {}),
        }
        if 'ueditor' in final_attrs:
            del final_attrs['ueditor']

        return format_html(
            "\n".join([
                content,
                scripts,
            ]),
            flatatt(final_attrs),
            force_text(value)
        )


# eof
