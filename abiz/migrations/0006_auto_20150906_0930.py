# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abiz', '0005_auto_20150906_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catedarticle',
            name='article',
            field=models.ForeignKey(to='abiz.Article', db_constraint=False),
            # preserve_default=True,
        ),
        migrations.AlterField(
            model_name='catedarticle',
            name='category',
            field=models.ForeignKey(to='abiz.ArticleCategory', db_constraint=False),
            # preserve_default=True,
        ),
    ]
