# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import abiz.fields


class Migration(migrations.Migration):

    dependencies = [
        ('abiz', '0002_auto_20150621_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=abiz.fields.RedTextField(max_length=127),
        ),
    ]
