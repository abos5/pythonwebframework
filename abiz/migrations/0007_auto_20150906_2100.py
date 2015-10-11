# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import abox.models


class Migration(migrations.Migration):

    dependencies = [
        ('abiz', '0006_auto_20150906_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlebody',
            name='content',
            field=abox.models.HtmlTextField(default=b'', blank=True),
        ),
    ]
