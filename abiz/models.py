from django.db import models
import abox.models


class Article(models.Model):
    article_id = models.AutoField(
        primary_key=True
    )
    title = models.CharField(max_length=127, blank=False)
    summary = models.CharField(max_length=1023, blank=True)
    create_datetime = models.DateTimeField(
        auto_now_add=True,
        null=True,
    )
    last_modifed_datetime = models.DateTimeField(
        auto_now=True,
        null=True
    )
    publish_datetime = models.DateTimeField(
        null=True,
    )
    sort_datetime = models.DateTimeField(
        null=True,
    )

    def __str___unicode__(self):
        return "%+32s" % (self.title)

    @property
    def next_pk(self):
        return self.pk + 1

    @property
    def previous_pk(self):
        previous_pk = self.pk - 1
        return previous_pk if previous_pk > 0 else 1


class ArticleBody(models.Model):
    article = models.OneToOneField(
        Article,
        primary_key=True,
        db_constraint=False,
    )
    content = abox.models.HtmlTextField(blank=True, default='')


class ArticleCategory(abox.models.Category):
    """
    an specific category table for article only
    table structure inherits from category(abstract model of category)
    """

    articles = models.ManyToManyField(
        Article,
        through='CatedArticle'
    )


class CatedArticle(models.Model):
    """
    where the relationship between article and article_category
    is stored
    """
    category = models.ForeignKey(
        ArticleCategory,
        db_constraint=False,
    )
    article = models.ForeignKey(
        Article,
        db_constraint=False,
    )

    def __str__(self):
        return ''


# Create your models here.
