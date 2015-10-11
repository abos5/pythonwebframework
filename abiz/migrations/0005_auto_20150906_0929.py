# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abiz', '0004_auto_20150829_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catedarticle',
            name='article',
            field=models.ForeignKey(to='abiz.Article'),
            # preserve_default=True,
        ),
        migrations.AlterField(
            model_name='catedarticle',
            name='category',
            field=models.ForeignKey(to='abiz.ArticleCategory'),
            # preserve_default=True,
        ),
    ]
