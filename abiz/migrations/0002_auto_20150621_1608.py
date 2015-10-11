# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatedArticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('article', models.ForeignKey(to='abiz.ArticleCategory')),
                ('category', models.ForeignKey(to='abiz.Article')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='articlecategory',
            name='articles',
            field=models.ManyToManyField(to='abiz.Article', through='abiz.CatedArticle'),
            preserve_default=True,
        ),
    ]
