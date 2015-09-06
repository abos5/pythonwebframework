# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('article_id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=127)),
                ('summary', models.CharField(max_length=1023, blank=True)),
                ('create_datetime', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_modifed_datetime', models.DateTimeField(auto_now=True, null=True)),
                ('publish_datetime', models.DateTimeField(null=True)),
                ('sort_datetime', models.DateTimeField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ArticleBody',
            fields=[
                ('article', models.OneToOneField(db_constraint=False, primary_key=True, serialize=False, to='abiz.Article')),
                ('content', models.TextField(default=b'', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ArticleCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cate_name', models.CharField(max_length=63)),
                ('cate_description', models.CharField(max_length=127, null=True)),
                ('cate_parent', models.ForeignKey(related_name=b'cate_children', db_constraint=False, default=1, to='abiz.ArticleCategory', null=True)),
            ],
            options={
                'abstract': False,
                'db_table': '%(app_label)s_article_category',
            },
            bases=(models.Model,),
        ),
    ]
