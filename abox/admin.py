# Other way of implementating formfield widget
"""
class SomeForm(models.ModelAdmin or models.TabularInline):
    \"""
    Should be implemented by other form
    \"""
    class Meta:
        widgets = {
            'field_a': SomeWidget,
            'field_b': SomeOtherWidget,
        }
"""
from django.contrib import admin
from django.db import models
from abox import widgets
import abox.models


# globally modify default widgets
FORMFIELD_OVERRIDES = {
    models.DateTimeField: {

        # widgets for over write should use a class
        'widget': widgets.AboxSplitDateTime,
    },
    abox.models.HtmlTextField: {
        'widget': widgets.Ueditor,
    }
}


class AboxModelAdmin(admin.ModelAdmin):
    """basic model admin for custom projects
    """

    formfield_overrides = FORMFIELD_OVERRIDES


class AboxTabularInline(admin.TabularInline):

    formfield_overrides = FORMFIELD_OVERRIDES



#eof
