from django.contrib import admin
from django.db import models
from abox import widgets
import abox.models


# widgets for over write should use a class
FORMFIELD_OVERRIDES = {
    models.DateTimeField: {
        'widget': widgets.AboxSplitDateTime,
    },
    abox.models.HtmlTextField: {
        'widget': widgets.Ueditor,
    }
}


class AboxModelAdmin(admin.ModelAdmin):
    """basic model admin for custom projects
    """

    # globally modify default widgets

    formfield_overrides = FORMFIELD_OVERRIDES


class AboxTabularInline(admin.TabularInline):

    formfield_overrides = FORMFIELD_OVERRIDES



#eof
