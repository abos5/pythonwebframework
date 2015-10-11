# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abiz', '0007_auto_20150906_2100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlecategory',
            name='articles',
        ),
    ]
